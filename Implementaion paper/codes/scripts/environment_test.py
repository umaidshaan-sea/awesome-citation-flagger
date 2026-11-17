import hashlib
import json
import platform
import random
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

SEED = 20261028
reports = []


def report(name, state, detail):
    reports.append({'check': name, 'status': state, 'detail': str(detail)})
    print(f'{state:4} | {name}: {detail}')


def normalize_doi(value):
    value = unquote(value.strip()).lower()
    for prefix in ('https://doi.org/', 'http://doi.org/', 'doi:'):
        if value.startswith(prefix):
            value = value[len(prefix):]
    return value.strip()


print('Environment smoke test | UTC', datetime.now(timezone.utc).isoformat())
report('runtime', 'PASS', f'Python {sys.version.split()[0]} | {platform.platform()}')

try:
    import requests
    import pandas
    import numpy as np
    import sklearn
    import matplotlib
    import packaging
    versions = {x: getattr(sys.modules[x], '__version__', 'unknown') for x in
                ('requests', 'pandas', 'numpy', 'sklearn', 'matplotlib', 'packaging')}
    report('imports', 'PASS', versions)
except Exception as exc:
    report('imports', 'FAIL', repr(exc))

p = subprocess.run([sys.executable, '-m', 'pip', 'check'], capture_output=True, text=True)
report('pip_check', 'PASS' if p.returncode == 0 else 'FAIL', (p.stdout + p.stderr).strip()[:500])
random.seed(SEED)
a = [random.random() for _ in range(3)]
random.seed(SEED)
report('random_seed', 'PASS' if a == [random.random() for _ in range(3)] else 'FAIL', f'seed={SEED}')
try:
    import numpy as np
    x = np.random.default_rng(SEED).integers(0, 100, 4)
    y = np.random.default_rng(SEED).integers(0, 100, 4)
    report('numpy_seed', 'PASS' if (x == y).all() else 'FAIL', x.tolist())
except Exception as exc:
    report('numpy_seed', 'FAIL', repr(exc))
example = ' HTTPS://DOI.ORG/10.1021/am300292v '
report('doi_normalize', 'PASS' if normalize_doi(example) == '10.1021/am300292v' else 'FAIL', normalize_doi(example))

try:
    import requests
    endpoints = {
        'crossref_api': 'https://api.crossref.org/works/10.1021/am300292v',
        'openalex_api': 'https://api.openalex.org/works/https://doi.org/10.1021/am300292v',
    }
    for name, url in endpoints.items():
        try:
            res = requests.get(url, timeout=20, headers={'User-Agent': 'CitationRetractionResearchEnvironmentTest/0.1 (academic smoke test)'})
            res.raise_for_status()
            payload = res.json()
            value = payload.get('message', {}) if name == 'crossref_api' else payload
            expected_key = 'DOI' if name == 'crossref_api' else 'is_retracted'
            good = isinstance(value, dict) and expected_key in value
            report(name, 'PASS' if good else 'FAIL', f'http={res.status_code}, expected_field={expected_key}, exists={good}')
        except Exception as exc:
            report(name, 'FAIL', f'{type(exc).__name__}: {str(exc)[:220]}')
except Exception as exc:
    report('api_import', 'FAIL', repr(exc))

out = Path('results/logs/environment_smoke_test.json')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({'timestamp_utc': datetime.now(timezone.utc).isoformat(), 'seed': SEED,
                           'python': sys.version, 'checks': reports}, indent=2))
print('Report:', out)
print('Overall:', 'PASS' if all(r['status'] == 'PASS' for r in reports) else 'FAIL / INVESTIGATE')
