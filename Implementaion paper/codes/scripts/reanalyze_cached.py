"""Re-analyze the 2026-11-04 archived API JSON, without network calls.

Use from repository root: python3 scripts/reanalyze_cached.py
The frozen benchmark is not modified. Original computed results are retained in audit/.
"""
from pathlib import Path
import json, hashlib, sys, difflib, re, importlib.util
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.core import doi, openalex, crossref, combine
from src.metrics import evaluate
legacy_path=ROOT/'audit/original_scripts/core_legacy.py'
legacy_spec=importlib.util.spec_from_file_location('legacy_core',legacy_path)
legacy_module=importlib.util.module_from_spec(legacy_spec)
legacy_spec.loader.exec_module(legacy_module)


def read_cache(provider, identifier):
    p=ROOT/'data'/'processed'/'api_cache'/provider/(hashlib.sha256(identifier.encode()).hexdigest()+'.json')
    if not p.exists():
        raise FileNotFoundError(f'Missing archived API evidence: {p}')
    response=json.loads(p.read_text())
    if response.get('original_doi') != identifier:
        raise ValueError(f'Cache DOI mismatch for {identifier}')
    return response


def title_similarity(a,b):
    a=re.sub(r'[^a-z0-9 ]','',str(a).lower())
    b=re.sub(r'[^a-z0-9 ]','',str(b).lower())
    return round(difflib.SequenceMatcher(None,a,b).ratio(),3)


def pub_group(s):
    s=str(s).lower()
    if any(k in s for k in ('springer','nature','cureus','biomed')): return 'Springer Nature / BMC'
    if 'elsevier' in s: return 'Elsevier'
    if 'wiley' in s: return 'Wiley'
    if 'plos' in s: return 'PLOS'
    if 'ieee' in s: return 'IEEE'
    if 'national academy' in s: return 'PNAS'
    return 'Other'


def main():
    frozen=pd.read_csv(ROOT/'data/splits/benchmark_80_frozen.csv').fillna('')
    if len(frozen)!=80 or frozen.doi.nunique()!=80 or frozen.gold_label.value_counts().to_dict()!={'RETRACTED':40,'NOT_RETRACTED':40}:
        raise AssertionError('Frozen split differs from the archived 40/40, 80-DOI benchmark')
    rows=[]
    for item in frozen.to_dict(orient='records'):
        identifier=item['doi']
        oa_response=read_cache('openalex',identifier)
        cr_response=read_cache('crossref',identifier)
        oa=openalex(oa_response.get('record'))
        cr=crossref(cr_response.get('record'),identifier)
        merged=combine(oa,cr)
        rec=cr_response.get('record') or {}
        title_list=rec.get('title') or []
        registered_title=str(title_list[0]) if isinstance(title_list,list) and title_list else ''
        rel=rec.get('updated-by') if isinstance(rec.get('updated-by'),list) else []
        src={str(x.get('source') or 'unattributed').lower() for x in rel if isinstance(x,dict) and str(x.get('type')).lower()=='retraction'}
        pub_notice=any(isinstance(x,dict) and str(x.get('type')).lower()=='retraction' and x.get('source')=='publisher' and doi(x.get('DOI')) and doi(x.get('DOI'))!=identifier for x in rel)
        rw_notice=any(isinstance(x,dict) and str(x.get('type')).lower()=='retraction' and x.get('source')=='retraction-watch' and doi(x.get('DOI')) and doi(x.get('DOI'))!=identifier for x in rel)
        notices=cr['evidence']
        typed=[x for x in rel if isinstance(x,dict) and str(x.get('type')).lower()=='retraction']
        self_count=sum(doi(x.get('DOI'))==identifier for x in typed)
        distinct_count=sum(bool(doi(x.get('DOI'))) and doi(x.get('DOI'))!=identifier for x in typed)
        legacy=legacy_module.crossref(cr_response.get('record'),identifier)
        legacy_bug_category=('SELF_ONLY' if self_count and not distinct_count else
                             'MIXED_SELF_AND_NOTICE' if self_count and distinct_count else
                             'DISTINCT_ONLY' if distinct_count else 'NO_TYPED_RELATION')
        rows.append({
            'doi':identifier,'frozen_title':item['title'],
            'title':registered_title if registered_title else item['title'],
            'publisher':item['publisher'],'publisher_group':pub_group(item['publisher']),
            'frozen_pub_year':item['pub_year'],'gold_label':item['gold_label'],
            'label_basis':'Retraction Watch listed' if item['gold_label']=='RETRACTED' else 'hand-selected presumed negative',
            'gold_evidence_url':item['gold_evidence_url'],
            'independent_ground_truth_verified':False,
            'crossref_record_title':registered_title,
            'frozen_title_similarity':title_similarity(item['title'],registered_title) if registered_title else None,
            'title_audit_flag':'MISSING_PROVIDER_RECORD' if not registered_title else 'TITLE_MISMATCH_REVIEW' if title_similarity(item['title'],registered_title)<0.55 else 'MATCH_OR_SIMILAR',
            'openalex_http_status':oa_response.get('http_status'),
            'crossref_http_status':cr_response.get('http_status'),
            'openalex_fetched_at_utc':oa_response.get('fetched_at_utc'),
            'crossref_fetched_at_utc':cr_response.get('fetched_at_utc'),
            'openalex_prediction':oa['prediction'],
            'crossref_prediction':cr['prediction'],
            'combined_prediction':merged['prediction'],
            'crossref_reason':cr['reason'],
            'combined_reason':merged['reason'],
            'explanation_type':merged['explanation_type'],
            'has_typed_retraction_signal':cr['prediction']=='RETRACTED',
            'has_notice_evidence':bool(notices),
            'notice_doi':notices[0]['notice_doi'] if notices else '',
            'status_sources':';'.join(sorted(src)),
            'publisher_distinct_notice':pub_notice,
            'retraction_watch_distinct_notice':rw_notice,
            'status_self_only':cr['reason']=='typed_retraction_status_self_only',
            'self_relation_count':self_count,'distinct_relation_count':distinct_count,
            'legacy_prediction':legacy['prediction'],'legacy_reason':legacy['reason'],
            'legacy_bug_category':legacy_bug_category,
        })
    df=pd.DataFrame(rows)
    resultdir=ROOT/'results/processed';resultdir.mkdir(parents=True,exist_ok=True)
    df.to_csv(resultdir/'benchmark_results.csv',index=False)
    metrics=evaluate(df.to_dict(orient='records'))
    metrics.to_csv(resultdir/'metrics_summary.csv',index=False)
    (resultdir/'metrics_summary.json').write_text(metrics.to_json(orient='records',indent=2))
    df[['doi','gold_label','frozen_title','crossref_record_title','frozen_title_similarity','title_audit_flag']].to_csv(resultdir/'title_audit.csv',index=False)
    title_summary=(pd.crosstab(df.gold_label,df.title_audit_flag)
        .reindex(index=['RETRACTED','NOT_RETRACTED'],columns=['MATCH_OR_SIMILAR','TITLE_MISMATCH_REVIEW','MISSING_PROVIDER_RECORD'],fill_value=0))
    title_summary.loc['TOTAL']=title_summary.sum()
    title_summary.to_csv(resultdir/'title_audit_by_class.csv')
    legacy_details=df[(df.gold_label=='RETRACTED') & (df.legacy_prediction=='UNKNOWN')][
        ['doi','gold_label','legacy_prediction','legacy_reason','legacy_bug_category',
         'self_relation_count','distinct_relation_count','crossref_prediction','notice_doi']]
    legacy_details.to_csv(resultdir/'legacy_rule_failures.csv',index=False)
    pos=df[df.gold_label=='RETRACTED']
    groups=[]
    for group,sub in pos.groupby('publisher_group'):
        groups.append({'publisher_group':group,'positive_cases':len(sub),
                       'crossref_typed':int(sub.has_typed_retraction_signal.sum()),
                       'distinct_notice_doi':int(sub.has_notice_evidence.sum()),
                       'self_only':int(sub.status_self_only.sum()),
                       'publisher_sourced_signal':int(sub.status_sources.str.contains('publisher').sum()),
                       'rw_sourced_signal':int(sub.status_sources.str.contains('retraction-watch').sum())})
    pd.DataFrame(groups).sort_values('publisher_group').to_csv(resultdir/'publisher_breakdown.csv',index=False)
    stats={
        'time_basis':'archived API snapshots fetched 2026-11-04 UTC; offline reconstruction on 2026-11-17',
        'sample_n':len(df),'positive_labels_n':len(pos),'negative_labels_n':len(df)-len(pos),
        'crossref_typed_positive_n':int(pos.has_typed_retraction_signal.sum()),
        'crossref_status_self_only_n':int(pos.status_self_only.sum()),
        'crossref_distinct_notice_n':int(pos.has_notice_evidence.sum()),
        'distinct_notice_pct_of_positives':round(100*pos.has_notice_evidence.mean(),2),
        'publisher_sourced_status_n':int(pos.status_sources.str.contains('publisher').sum()),
        'rw_sourced_status_n':int(pos.status_sources.str.contains('retraction-watch').sum()),
        'publisher_sourced_distinct_notice_n':int(pos.publisher_distinct_notice.sum()),
        'rw_sourced_distinct_notice_n':int(pos.retraction_watch_distinct_notice.sum()),
        'both_apis_404_on_negative_n':int(((df.gold_label=='NOT_RETRACTED') & (df.crossref_http_status==404) & (df.openalex_http_status==404)).sum()),
        'legacy_self_only_unknown_n':int(((pos.legacy_prediction=='UNKNOWN') & (pos.legacy_bug_category=='SELF_ONLY')).sum()),
        'legacy_mixed_unknown_n':int(((pos.legacy_prediction=='UNKNOWN') & (pos.legacy_bug_category=='MIXED_SELF_AND_NOTICE')).sum()),
        'legacy_distinct_only_true_positive_n':int(((pos.legacy_prediction=='RETRACTED') & (pos.legacy_bug_category=='DISTINCT_ONLY')).sum()),
        'title_mismatch_flagged_n':int((df.title_audit_flag=='TITLE_MISMATCH_REVIEW').sum()),
        'title_mismatch_positive_n':int(((df.gold_label=='RETRACTED') & (df.title_audit_flag=='TITLE_MISMATCH_REVIEW')).sum()),
        'title_mismatch_control_n':int(((df.gold_label=='NOT_RETRACTED') & (df.title_audit_flag=='TITLE_MISMATCH_REVIEW')).sum()),
        'missing_record_title_n':int((df.title_audit_flag=='MISSING_PROVIDER_RECORD').sum()),
        'records_with_independent_ground_truth':0,
        'claims_are_benchmark_label_agreement_not_independent_ground_truth_accuracy':True,
    }
    (resultdir/'audit_statistics.json').write_text(json.dumps(stats,indent=2))
    # Never mix the legacy 24/40 self-DOI ambiguity rule with a status baseline.
    assert stats['crossref_typed_positive_n']==40
    assert stats['crossref_distinct_notice_n']==32
    assert stats['crossref_status_self_only_n']==8
    assert stats['both_apis_404_on_negative_n']==4
    assert stats['legacy_self_only_unknown_n']==8 and stats['legacy_mixed_unknown_n']==8
    assert stats['legacy_distinct_only_true_positive_n']==24
    assert stats['title_mismatch_positive_n']==1 and stats['title_mismatch_control_n']==23
    assert set(metrics.TP)=={40} and set(metrics.UNKNOWN)=={4}
    print('Offline archived-API replay PASSED')
    print(json.dumps(stats,indent=2))
    print(metrics.to_string(index=False))

if __name__=='__main__':main()
