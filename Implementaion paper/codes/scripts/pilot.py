import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import argparse
import json
from pathlib import Path
import pandas as pd
from src.data import load_candidates
from src.providers import fetch
from src.core import openalex, crossref, combine

p=argparse.ArgumentParser()
p.add_argument('--csv', default='data/raw/retraction-watch-data/retraction_watch.csv')
p.add_argument('--positive', type=int, default=10)
p.add_argument('--correction', type=int, default=10)
p.add_argument('--refresh', action='store_true')
a=p.parse_args()
rows, manifest = load_candidates(a.csv, positive_limit=a.positive, correction_limit=a.correction)
if rows.empty: raise SystemExit('No eligible DOI candidates; cannot run pilot.')
Path('data/splits').mkdir(parents=True, exist_ok=True)
rows.to_csv('data/splits/pilot_candidates_UNVERIFIED.csv', index=False)
Path('results/logs').mkdir(parents=True, exist_ok=True)
Path('results/logs/pilot_manifest.json').write_text(json.dumps(manifest, indent=2))
results=[]
for idx, item in enumerate(rows.to_dict('records'),1):
    d=item['doi']
    oa=fetch('openalex', d, refresh=a.refresh)
    cr=fetch('crossref', d, refresh=a.refresh)
    b0=openalex(oa['record'] if oa['status']=='OK' else None)
    b1=crossref(cr['record'] if cr['status']=='OK' else None, d)
    pr=combine(b0,b1)
    results.append({**item, 'openalex_prediction':b0['prediction'], 'crossref_prediction':b1['prediction'], 'combined_prediction':pr['prediction'], 'openalex_reason':b0['reason'], 'crossref_reason':b1['reason'], 'combined_reason':pr['reason'], 'crossref_evidence':json.dumps(b1['evidence']), 'explanation_type':pr['explanation_type'], 'openalex_fetch':oa['status'], 'crossref_fetch':cr['status']})
    print(f'{idx}/{len(rows)} {d} | OA {b0["prediction"]} | CR {b1["prediction"]} | P {pr["prediction"]}')
pd.DataFrame(results).to_csv('results/tables/pilot_predictions_UNSCORED.csv', index=False)
print('Pilot metadata saved; NO evaluation metrics: labels are unverified.')
print('outputs: data/splits/pilot_candidates_UNVERIFIED.csv, results/tables/pilot_predictions_UNSCORED.csv')
