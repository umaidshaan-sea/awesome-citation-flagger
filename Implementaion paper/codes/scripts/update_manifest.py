"""Generate SHA-256 inventory for shipped files; existence != scientific validity."""
import csv,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifact_manifest.csv'
rows=[]
for f in sorted(ROOT.rglob('*')):
    if not f.is_file() or f==OUT or '__pycache__' in f.parts or f.suffix=='.pyc':
        continue
    h=hashlib.sha256(f.read_bytes()).hexdigest()
    rows.append({'produced_path':str(f.relative_to(ROOT)), 'size_bytes':f.stat().st_size,
                 'sha256_hash':h,'verification_status':'FILE_HASH_VERIFIED_NOT_SCIENTIFIC_GROUND_TRUTH'})
with OUT.open('w',newline='',encoding='utf8') as stream:
    writer=csv.DictWriter(stream,fieldnames=['produced_path','size_bytes','sha256_hash','verification_status'])
    writer.writeheader();writer.writerows(rows)
print(f'Wrote {len(rows)} file hashes to {OUT}')
