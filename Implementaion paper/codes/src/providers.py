import hashlib
import json
import os
import time
from pathlib import Path
from urllib.parse import quote
import requests

HEADERS = {'User-Agent': 'CitationRetractionResearch/0.2 (academic experiment; contact: configure-your-email)'}

def fetch(provider, doi, cache_root='data/processed/api_cache', refresh=False):
    path = Path(cache_root) / provider / (hashlib.sha256(doi.encode()).hexdigest() + '.json')
    if path.exists() and not refresh:
        return json.loads(path.read_text(encoding='utf-8'))
    if provider == 'crossref':
        url = 'https://api.crossref.org/works/' + quote(doi, safe='')
    elif provider == 'openalex':
        url = 'https://api.openalex.org/works/https://doi.org/' + quote(doi, safe='')
    else:
        raise ValueError(provider)
    output = {'provider': provider, 'original_doi': doi, 'url': url, 'status': 'ERROR', 'http_status': None, 'fetched_at_utc': None, 'record': None}
    from datetime import datetime, timezone
    for attempt in range(3):
        try:
            response = requests.get(url, headers=HEADERS, timeout=20)
            output['http_status'] = response.status_code
            if response.status_code == 404:
                output['status'] = 'NOT_FOUND'
                break
            if response.status_code in (429, 500, 502, 503, 504):
                if attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                output['status'] = 'HTTP_ERROR'
                break
            response.raise_for_status()
            obj = response.json()
            record = obj.get('message') if provider == 'crossref' else obj
            output['record'] = record if isinstance(record, dict) else None
            output['status'] = 'OK' if output['record'] else 'INVALID_JSON'
            break
        except (requests.RequestException, ValueError) as exc:
            output['error'] = str(exc)
            if attempt < 2:
                time.sleep(2 ** attempt)
    output['fetched_at_utc'] = datetime.now(timezone.utc).isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2), encoding='utf-8')
    return output
