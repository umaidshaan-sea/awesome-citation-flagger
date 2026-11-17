import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.validate_rw import validate_csv

parser = argparse.ArgumentParser()
parser.add_argument('--csv', default='data/raw/retraction-watch-data/retraction_watch.csv')
parser.add_argument('--out', default='results/logs/dataset_validation.json')
args = parser.parse_args()
result = validate_csv(args.csv)
target = Path(args.out)
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
print(f'VALIDATED STRUCTURE ONLY | log={target} | ground_truth=UNVERIFIED')
