"""Formal accuracy scoring gate: rejects unadjudicated labels."""
import argparse,sys
from pathlib import Path
import pandas as pd
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root))
from src.metrics import evaluate
p=argparse.ArgumentParser()
p.add_argument('adjudicated_csv',help='CSV with independently verified positive and negative labels')
a=p.parse_args()
frame=pd.read_csv(a.adjudicated_csv).fillna('')
if 'independent_ground_truth_verified' not in frame:
    raise SystemExit('Refusing accuracy claim: missing independent_ground_truth_verified column')
allowed={'true','1','yes'}
if not all(str(v).lower() in allowed for v in frame.independent_ground_truth_verified):
    raise SystemExit('Refusing accuracy claim: not all cases independently adjudicated')
res=evaluate(frame.to_dict('records'))
out=root/'results/processed/independently_verified_metrics.csv'
res.to_csv(out,index=False)
print(res.to_string(index=False))
print('Saved',out)
