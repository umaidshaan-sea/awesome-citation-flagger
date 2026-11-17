import argparse
from pathlib import Path
import subprocess
import shutil

p = argparse.ArgumentParser()
p.add_argument('--source', default='data/raw/retraction-watch-data')
a = p.parse_args()
path = Path(a.source)
if not shutil.which('git'):
    raise SystemExit('git is unavailable. Install git or manually place retraction_watch.csv in data/raw/')
if (path/'.git').exists():
    subprocess.run(['git', '-C', str(path), 'pull', '--ff-only'], check=True)
else:
    path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['git', 'clone', '--depth', '1', 'https://gitlab.com/crossref/retraction-watch-data.git', str(path)], check=True)
subprocess.run(['git', '-C', str(path), 'rev-parse', 'HEAD'], check=True)
files=list(path.glob('*.csv'))
print('CSV files:', [str(x) for x in files])
if not files: raise SystemExit('No CSV found')
