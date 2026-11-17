import re
from urllib.parse import unquote

DOI_RE = re.compile(r'^10\.\d{4,9}/\S+$', re.I)

def doi(value):
    if value is None:
        return ''
    s = unquote(str(value)).strip().lower()
    s = re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi\s*:\s*)', '', s)
    s = s.strip().rstrip('.,;')
    return s if DOI_RE.match(s) else ''

def openalex(record):
    if not isinstance(record, dict) or not isinstance(record.get('is_retracted'), bool):
        return {'prediction': 'UNKNOWN', 'reason': 'missing_record_or_boolean', 'evidence': []}
    if record.get('doi') and not doi(record.get('doi')):
        return {'prediction': 'UNKNOWN', 'reason': 'invalid_response_doi', 'evidence': []}
    return {'prediction': 'RETRACTED' if record['is_retracted'] else 'NOT_RETRACTED',
            'reason': 'openalex_indicator_only_not_ground_truth', 'evidence': []}

def crossref(record, target):
    if not isinstance(record, dict):
        return {'prediction': 'UNKNOWN', 'reason': 'missing_record', 'evidence': []}
    if doi(record.get('DOI')) != doi(target):
        return {'prediction': 'UNKNOWN', 'reason': 'doi_mismatch', 'evidence': []}
    relations = record.get('updated-by', [])
    if not isinstance(relations, list):
        return {'prediction': 'UNKNOWN', 'reason': 'invalid_relation_format', 'evidence': []}
    evidence = []
    ambiguous = False
    reinstatement = False
    for r in relations:
        if not isinstance(r, dict):
            ambiguous = True
            continue
        typ = str(r.get('type', '')).lower().strip()
        notice_doi = doi(r.get('DOI', ''))
        if typ == 'retraction':
            if notice_doi and notice_doi != doi(target):
                evidence.append({'notice_doi': notice_doi, 'type': typ,
                                 'source': r.get('source'), 'date': r.get('updated', {}).get('date-time') if isinstance(r.get('updated'), dict) else None})
            else:
                ambiguous = True
        if typ in ('reinstatement', 'retraction-withdrawal'):
            reinstatement = True
    if reinstatement:
        return {'prediction': 'UNKNOWN', 'reason': 'reinstatement_requires_manual_review', 'evidence': evidence}
    if evidence and not ambiguous:
        return {'prediction': 'RETRACTED', 'reason': 'typed_retraction_update', 'evidence': evidence}
    if ambiguous:
        return {'prediction': 'UNKNOWN', 'reason': 'ambiguous_relation', 'evidence': evidence}
    return {'prediction': 'NOT_RETRACTED', 'reason': 'no_explicit_retraction_in_record', 'evidence': []}

def combine(a, b):
    pa, pb = a['prediction'], b['prediction']
    if a['reason'] == 'reinstatement_requires_manual_review' or b['reason'] == 'reinstatement_requires_manual_review':
        p, reason = 'UNKNOWN', 'reinstatement_requires_manual_review'
    elif 'RETRACTED' in (pa, pb):
        p, reason = 'RETRACTED', 'union_positive'
    elif pa == pb == 'NOT_RETRACTED':
        p, reason = 'NOT_RETRACTED', 'both_negative'
    else:
        p, reason = 'UNKNOWN', 'insufficient_evidence'
    return {'prediction': p, 'reason': reason, 'evidence': b['evidence'],
            'explanation_type': 'explicit_notice' if b['evidence'] else 'indicator_only' if p == 'RETRACTED' else 'none'}
