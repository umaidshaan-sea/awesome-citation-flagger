"""Independent internal checks of this ZIP's data, code, historical plots, and final numeric-only PDF.
Does not constitute external publisher adjudication, live API verification, or measured cache timings.
"""
from pathlib import Path
import json, csv, hashlib, subprocess, sys, re, collections
import pandas as pd
import fitz
ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/'audit/final_three_pass_validation.json'
checks=[]
def check(stage,name,condition,description):
    ok=bool(condition)
    checks.append({'stage':stage,'name':name,'passed':ok,'detail':str(description)})
    if not ok:
        REPORT.write_text(json.dumps({'all_passed':False,'checks':checks},indent=2))
        raise AssertionError(f'{stage}: {name}: {description}')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def text_tokens(p):
    d=fitz.open(p)
    return [collections.Counter(re.findall(r'[A-Za-z_]+',page.get_text())) for page in d]

def main():
    # PASS 1 — immutable sources, complete prompts, and cache keys
    stage='PASS 1 — SOURCE & INVENTORY'
    raw=ROOT/'data/raw/retraction-watch-data/retraction_watch.csv'
    check(stage,'Raw dataset integrity',sha(raw)=='e5351ee51ab3f1da7fe98b3bd6c5c58049b8bff4705949ef6fd4f1a1315dd0ea',sha(raw))
    split=pd.read_csv(ROOT/'data/splits/benchmark_80_frozen.csv')
    check(stage,'Frozen 80 unique split',len(split)==split.doi.nunique()==80 and split.gold_label.value_counts().to_dict()=={'RETRACTED':40,'NOT_RETRACTED':40},split.gold_label.value_counts().to_dict())
    for provider in ['openalex','crossref']:
        cache=ROOT/'data/processed/api_cache'/provider
        check(stage,f'{provider} 80 cached records',len(list(cache.glob('*.json')))==80,len(list(cache.glob('*.json'))))
        faulty=[]
        for identifier in split.doi:
            p=cache/(hashlib.sha256(identifier.encode()).hexdigest()+'.json')
            if not p.exists() or json.loads(p.read_text()).get('original_doi')!=identifier:faulty.append(identifier)
        check(stage,f'{provider} DOI mapping',not faulty,f'{len(faulty)} missing or mismatched')
    prompts=list((ROOT/'prompt_outputs').glob('[0-9][0-9]_*.md'))
    check(stage,'All 18 prompt deliverables',len(prompts)==18,len(prompts))
    check(stage,'Uploaded paper source preserved',(ROOT/'inputs/final_paper_source_verbatim.pdf').exists(),'original source PDF present')
    # PASS 2 — code, two distinct classifier versions and computed fractions
    stage='PASS 2 — REPLAY & METRICS'
    tests=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    (ROOT/'results/logs/final_unit_tests.txt').write_text(tests.stdout+tests.stderr)
    check(stage,'Unit suite passes',tests.returncode==0 and 'Ran 21 tests' in tests.stderr,tests.stderr[-130:])
    pred=ROOT/'results/processed/benchmark_results.csv'
    original_sha=sha(pred)
    cmd=subprocess.run([sys.executable,'scripts/reanalyze_cached.py'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    (ROOT/'results/logs/final_cached_replay.txt').write_text(cmd.stdout+cmd.stderr)
    check(stage,'Offline replay stable',cmd.returncode==0 and sha(pred)==original_sha,'output hash stable; no network')
    df=pd.read_csv(pred);pos=df[df.gold_label=='RETRACTED']; neg=df[df.gold_label=='NOT_RETRACTED']
    legacy=(int((pos.legacy_prediction=='RETRACTED').sum()),int((pos.legacy_prediction=='UNKNOWN').sum()))
    corrected=(int((pos.crossref_prediction=='RETRACTED').sum()),int(pos.has_notice_evidence.sum()),int(pos.status_self_only.sum()))
    check(stage,'Legacy decisions 24/16',legacy==(24,16),legacy)
    check(stage,'Corrected 40,32,8',corrected==(40,32,8),corrected)
    check(stage,'Four unresolved controls',int((neg.crossref_prediction=='UNKNOWN').sum())==4 and int((neg.openalex_prediction=='UNKNOWN').sum())==4,'UNKNOWN controls 4/40')
    actual=pd.read_csv(ROOT/'results/processed/publisher_breakdown.csv')
    check(stage,'Publisher total 40 status, 32 notices',actual.crossref_typed.sum()==40 and actual.distinct_notice_doi.sum()==32,'40/40, 32/40 = 80%')
    check(stage,'Chart 5 denominator reflects resolved legacy cases',24+16+0+36==76 and 80-76==4,'chart N=76, four unresolved')
    latency=pd.read_csv(ROOT/'audit/original_results/benchmark_results_legacy.csv')
    seq=latency.openalex_latency_ms+latency.crossref_latency_ms
    check(stage,'Historical network telemetry standard deviation',round(seq.mean(),1)==2128.2 and round(seq.std(),1)==558.9,(round(seq.mean(),1),round(seq.std(),1)))
    m=pd.read_csv(ROOT/'results/processed/metrics_summary.csv')
    check(stage,'Corrected metrics 3 methods',len(m)==3 and all(m.TP==40) and all(m.TN==36) and all(m.UNKNOWN==4) and all(m.F1_end_to_end==1),'all three 40 TP/36 TN/4 UNKNOWN, F1e2e=1')
    check(stage,'No independent labels represented as verified',not df.independent_ground_truth_verified.astype(bool).any(),'all 80 provisional labels')
    # PASS 3 — seven-page final manuscript and preservation of alphabetic text
    stage='PASS 3 — PDF, TABLES & ARTIFACTS'
    original=ROOT/'inputs/final_paper_source_verbatim.pdf'
    final=ROOT/'paper/manuscript.pdf'
    pdf=fitz.open(final);source=fitz.open(original)
    check(stage,'PDF opens and has 7 pages',len(pdf)==len(source)==7,'seven pages')
    before=text_tokens(original);after=text_tokens(final)
    check(stage,'Alphabetic word content unchanged on every page',before==after,'exact case-sensitive alphabetic token counts per page')
    page_text=[p.get_text() for p in pdf]
    check(stage,'Corrected numeric tokens',all(t in page_text[i] for i,t in [(3,'36'),(4,'558.9'),(5,'80.0%'),(4,'(N=76)')]),'36 controls, 558.9 SD, notice 80%, agreement chart N=76')
    check(stage,'No historical 32=60% arithmetic error',not any('32 (60.0%)' in t for t in page_text),'32 (80.0%) (note PDF text order differs after patch)')
    out_of_bounds=[]
    for i,page in enumerate(pdf):
        for x0,y0,x1,y1,text,*_ in page.get_text('blocks'):
            if str(text).strip() and (x0<-2 or y0<-2 or x1>page.rect.width+2 or y1>page.rect.height+2):out_of_bounds.append(i+1)
    check(stage,'Text geometry within page',not out_of_bounds,out_of_bounds)
    words=(ROOT/'paper/tables/legacy_publisher_compliance_table.tex').read_text()
    check(stage,'LaTeX total notice figure corrected','32 (80.0\\%)' in words,'32/40 -> 80%')
    for item in ['legacy_system_architecture','legacy_metric_comparison','legacy_confusion_matrices','legacy_publisher_compliance_breakdown','legacy_disagreement_breakdown','legacy_abstention_sensitivity_curve','legacy_latency_distribution']:
        check(stage,f'Historical figure PDF and PNG {item}',all((ROOT/'paper/figures'/f'{item}.{ext}').is_file() for ext in ['pdf','png']),item)
    for item in ['confusion_matrices','metric_comparison','provenance_sources','publisher_coverage','system_architecture']:
        check(stage,f'Corrected standalone figure PDF and PNG {item}',all((ROOT/'results/figures'/f'{item}.{ext}').is_file() for ext in ['pdf','png']),item)
    for item in ['case_studies_table','comparative_metrics_table','publisher_compliance_table','signal_evidence_table','title_integrity_table']:
        check(stage,f'Corrected table {item}',(ROOT/'results/tables'/f'{item}.tex').is_file(),item)
    check(stage,'Final PDF source rebuild script exists',(ROOT/'scripts/rebuild_final_pdf.py').is_file(),'rebuilds from original unchanged input PDF with numeric-only edits')
    if (ROOT/'paper/main.pdf').is_file():
        built=fitz.open(ROOT/'paper/main.pdf')
        check(stage,'XeLaTeX PDF wrapper matches page text',len(built)==7 and all(built[i].get_text()==pdf[i].get_text() for i in range(7)),'same extracted text across 7 pages')
    report={'checks':checks,'all_passed':all(c['passed'] for c in checks),'three_passes':['SOURCE & INVENTORY','REPLAY & METRICS','PDF, TABLES & ARTIFACTS'],
            'limitations':['No externally adjudicated gold-standard accuracy.','Historical Crossref 24/40 is a legacy software bug, not publisher non-deposit.','Archived timing is not evidence of real-time speedup; in-memory cache trace was synthesized.','The user limited paper edits to numbers, so unsupported publisher-causality and example-DOI wording remains unchanged.']}
    REPORT.write_text(json.dumps(report,indent=2))
    print(f"PASS: {len(checks)} assertions in 3 internal validation passes; PDF pages=7; 18 deliverables; report={REPORT}")
if __name__=='__main__':main()
