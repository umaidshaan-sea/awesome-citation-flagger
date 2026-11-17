"""Optional live Crossref/OpenAlex *status* spot check, never a gold-label adjudication.
Run with network access from project root:
  python3 scripts/live_api_spotcheck.py             # 8 self-only + 4 404 controls
  python3 scripts/live_api_spotcheck.py --all       # all 80 benchmark DOIs
Live results go in results/live/ and NEVER overwrite the frozen archive.
"""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import quote
import argparse,hashlib,json,time
import pandas as pd
import requests
ROOT=Path(__file__).resolve().parents[1]

def query(url,session):
    timestamp=datetime.now(timezone.utc).isoformat()
    try:
        response=session.get(url,timeout=20,headers={'User-Agent':'CitationRetractionAudit/2.0 (scholarly metadata verification)'})
        raw=response.content
        payload=response.json() if response.ok else None
        return {'checked_at_utc':timestamp,'http_status':response.status_code,'sha256':hashlib.sha256(raw).hexdigest(), 'json':payload,'error':''}
    except Exception as exc:
        return {'checked_at_utc':timestamp,'http_status':None,'sha256':'','json':None,'error':repr(exc)}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--all',action='store_true',help='check all 80 DOIs; requires live internet access')
    args=parser.parse_args()
    df=pd.read_csv(ROOT/'results/processed/benchmark_results.csv').fillna('')
    if not args.all:
        df=df[((df.gold_label=='RETRACTED')&(df.status_self_only==True))|
              ((df.gold_label=='NOT_RETRACTED')&(df.crossref_http_status==404)&(df.openalex_http_status==404))]
    output=ROOT/'results/live'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    output.mkdir(parents=True,exist_ok=True)
    summary=[]
    session=requests.Session()
    for identifier in df.doi:
        for provider,url in [('crossref','https://api.crossref.org/works/'+quote(identifier,safe='/')),
                             ('openalex','https://api.openalex.org/works/https://doi.org/'+quote(identifier,safe='/'))]:
            item=query(url,session)
            data={'doi':identifier,'provider':provider,'retrieved_at_utc':item['checked_at_utc'],
                  'http_status':item['http_status'],'raw_sha256':item['sha256'],'error':item['error']}
            if item['json'] is not None:
                record=item['json'].get('message') if provider=='crossref' else item['json']
                (output/(provider+'_'+hashlib.sha256(identifier.encode()).hexdigest()+'.json')).write_text(json.dumps(record,indent=2))
                if provider=='crossref' and isinstance(record,dict):
                    rel=record.get('updated-by') or []
                    data['typed_retraction_count']=sum(isinstance(x,dict) and x.get('type')=='retraction' for x in rel)
                    data['record_title']='; '.join(record.get('title',[])[:1])
                if provider=='openalex' and isinstance(record,dict):
                    data['is_retracted']=record.get('is_retracted')
            summary.append(data)
            time.sleep(.35)
    pd.DataFrame(summary).to_csv(output/'live_responses.csv',index=False)
    errors=sum(bool(x['error']) for x in summary)
    print('Live request summary:',output,'successful:',len(summary)-errors,'failed:',errors)
    print('This is a transient metadata check; matching providers do not establish independent ground truth.')
    if errors:raise SystemExit(2)

if __name__=='__main__':main()
