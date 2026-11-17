"""Three internal consistency passes; these do NOT verify independent ground truth."""
from pathlib import Path
from datetime import datetime, timezone
import csv,sys,hashlib,json,subprocess,re
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'audit/validation_passes.json'
EXPECTED='e5351ee51ab3f1da7fe98b3bd6c5c58049b8bff4705949ef6fd4f1a1315dd0ea'
checks=[]
def check(pass_name,name,expr,details):
    ok=bool(expr)
    checks.append({'pass':pass_name,'check':name,'passed':ok,'detail':str(details)})
    if not ok: raise AssertionError(f'{pass_name}/{name}: {details}')

def main():
    # Pass 1: internal source and package inventory (not independent adjudication).
    f=ROOT/'data/raw/retraction-watch-data/retraction_watch.csv'
    rawhash=hashlib.sha256(f.read_bytes()).hexdigest()
    check('PASS 1 — SOURCE','Raw data hash',rawhash==EXPECTED,rawhash)
    split=pd.read_csv(ROOT/'data/splits/benchmark_80_frozen.csv').fillna('')
    check('PASS 1 — SOURCE','DOI labels and uniqueness',len(split)==80 and split.doi.nunique()==80 and (split.gold_label=='RETRACTED').sum()==40,'40/40, 80 unique')
    for provider in ['crossref','openalex']:
        paths=list((ROOT/'data/processed/api_cache'/provider).glob('*.json'))
        check('PASS 1 — SOURCE',f'{provider} cache count',len(paths)==80,len(paths))
        missing=[]
        for identifier in split.doi:
            cache_file=ROOT/'data/processed/api_cache'/provider/(hashlib.sha256(identifier.encode()).hexdigest()+'.json')
            if not cache_file.exists():missing.append(identifier);continue
            a=json.loads(cache_file.read_text())
            if a.get('original_doi') != identifier:missing.append(identifier)
        check('PASS 1 — SOURCE',f'{provider} DOI cache mapping',not missing,f'missing/mismatch={missing}')
    prompts=list((ROOT/'prompt_outputs').glob('[0-9][0-9]_*.md'))
    check('PASS 1 — SOURCE','18 corrected prompt files',len(prompts)==18,len(prompts))
    # Pass 2: code behavior + outcome invariants, independently of paper claims.
    result=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-q'],cwd=ROOT,capture_output=True,text=True)
    check('PASS 2 — EXECUTION','Unit suite 21 pass',result.returncode==0 and 'Ran 21 tests' in result.stderr,result.stderr[-400:])
    before=hashlib.sha256((ROOT/'results/processed/benchmark_results.csv').read_bytes()).hexdigest()
    rebuild=subprocess.run([sys.executable,'scripts/reanalyze_cached.py'],cwd=ROOT,capture_output=True,text=True)
    after=hashlib.sha256((ROOT/'results/processed/benchmark_results.csv').read_bytes()).hexdigest()
    check('PASS 2 — EXECUTION','Stable deterministic replay',rebuild.returncode==0 and before==after,f'sha before={before}; after={after}; error={rebuild.stderr[-100:]}')
    df=pd.read_csv(ROOT/'results/processed/benchmark_results.csv').fillna('');pos=df[df.gold_label=='RETRACTED'];neg=df[df.gold_label=='NOT_RETRACTED']
    check('PASS 2 — EXECUTION','Crossref positive and links',int(pos.has_typed_retraction_signal.sum())==40 and int(pos.has_notice_evidence.sum())==32 and int(pos.status_self_only.sum())==8,'40 status/32 link/8 self-only')
    check('PASS 2 — EXECUTION','Four unresolved controls',int((neg.crossref_prediction=='UNKNOWN').sum())==4 and int((neg.openalex_prediction=='UNKNOWN').sum())==4,'4 404 control DOIs')
    check('PASS 2 — EXECUTION','Title flag audit by class',int(((pos.title_audit_flag=='TITLE_MISMATCH_REVIEW')).sum())==1 and int(((neg.title_audit_flag=='TITLE_MISMATCH_REVIEW')).sum())==23 and int((neg.title_audit_flag=='MISSING_PROVIDER_RECORD').sum())==4,'1 positive, 23 controls flagged; 4 missing controls')
    check('PASS 2 — EXECUTION','Legacy self and mixed cases',int(((pos.legacy_prediction=='UNKNOWN') & (pos.legacy_bug_category=='SELF_ONLY')).sum())==8 and int(((pos.legacy_prediction=='UNKNOWN') & (pos.legacy_bug_category=='MIXED_SELF_AND_NOTICE')).sum())==8 and int(((pos.legacy_prediction=='RETRACTED') & (pos.legacy_bug_category=='DISTINCT_ONLY')).sum())==24,'8 self-only, 8 mixed, 24 distinct-only')
    summaries=pd.read_csv(ROOT/'results/processed/metrics_summary.csv')
    check('PASS 2 — EXECUTION','Method metrics invariant',len(summaries)==3 and all(summaries.TP==40) and all(summaries.UNKNOWN==4) and all(summaries.F1_end_to_end==1.0),'3 identical corrected outcomes')
    # Pass 3: PDF, source material, image/table, bibliography and format.
    import fitz
    pdf=ROOT/'paper/manuscript.pdf'
    doc=fitz.open(pdf)
    check('PASS 3 — PRESENTATION','PDF valid and nonempty',len(doc)>=4 and sum(len(p.get_text()) for p in doc)>11000, f'pages={len(doc)} chars={sum(len(p.get_text()) for p in doc)}')
    outboxes=[]
    for pn,page in enumerate(doc):
        bounds=page.rect
        for block in page.get_text('blocks'):
            if len(block)>=5 and block[4].strip() and (block[0]<-1 or block[1]<-1 or block[2]>bounds.width+1 or block[3]>bounds.height+1):
                outboxes.append((pn+1,block[:4]))
    check('PASS 3 — PRESENTATION','PDF page text within page',not outboxes,outboxes)
    log=(ROOT/'paper/main.log').read_text(errors='ignore')
    check('PASS 3 — PRESENTATION','No LaTeX overfull or unresolved citations','Overfull \\hbox' not in log and 'Citation `' not in log and 'undefined references' not in log,'checked main.log')
    figs=list((ROOT/'paper/figures').glob('*.pdf'));tables=list((ROOT/'paper/tables').glob('*.tex'))
    check('PASS 3 — PRESENTATION','Five current figures and five tables',len(figs)==5 and len(tables)==5,f'{len(figs)} PDF figures; {len(tables)} TeX tables')
    clean_text=' '.join(page.get_text() for page in doc)
    check('PASS 3 — PRESENTATION','Paper explicitly states key corrected counts',all(w in clean_text for w in ['32 of 40','40 of 40','eight self-only','eight mixed','23 of 40']), 'all major claims present')
    check('PASS 3 — PRESENTATION','No synthetic cache latency figure in active figures',not (ROOT/'paper/figures/latency_distribution.pdf').exists(),'removed unsafe chart')
    data={'audited_on':'2026-11-17','method':'three internal consistency passes over archived source/code/PDF; not independent scientific validation','checks':checks,'all_passed':all(c['passed'] for c in checks),'limitations':['No external adjudication of 80 benchmark labels','No successful 2026-11-17 live API data collection (network inaccessible)','No independent proof of source GitLab commit','No hardware latency benchmark']}
    OUT.write_text(json.dumps(data,indent=2))
    print(f'PASS: {len(checks)} internal consistency assertions across 3 passes; log {OUT}')

if __name__=='__main__':main()
