"""DOI normalization and status-vs-notice aware retraction classification.

A typed Crossref retraction can refer to the target DOI itself. This is a
status signal, *not* a separately resolvable notice DOI. Discarding it as
an error caused the legacy baseline's artificial false abstentions.
"""
import re
from urllib.parse import unquote

DOI_RE = re.compile(r'^10\.\d{4,9}/[-._;()/:a-z0-9]+$', re.I)
DOI_TOKEN_RE = re.compile(r'(?<![a-z0-9])10\.\d{4,9}/', re.I)


def doi(value):
    if value is None:
        return ''
    s = unquote(str(value)).strip().lower()
    s = re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi\s*:\s*)', '', s)
    s = s.strip().rstrip('.,;')
    # Avoid accidentally treating an unresolved multi-DOI list as one DOI.
    if len(DOI_TOKEN_RE.findall(s)) != 1:
        return ''
    return s if DOI_RE.fullmatch(s) else ''


def openalex(record):
    if not isinstance(record, dict) or not isinstance(record.get('is_retracted'), bool):
        return {'prediction': 'UNKNOWN', 'reason': 'missing_record_or_boolean', 'evidence': []}
    if record.get('doi') and not doi(record.get('doi')):
        return {'prediction': 'UNKNOWN', 'reason': 'invalid_response_doi', 'evidence': []}
    return {
        'prediction': 'RETRACTED' if record['is_retracted'] else 'NOT_RETRACTED',
        'reason': 'openalex_indicator_only_not_ground_truth', 'evidence': []
    }


def crossref(record, target):
    """Return a Crossref *status* signal plus optional distinct notice DOIs.

    Rules intentionally separate (A) retraction signal present from
    (B) separately identifiable notice. A self-referential DOI satisfies
    (A) but not (B). Reinstatement leads to UNKNOWN for editorial review.
    """
    if not isinstance(record, dict):
        return {'prediction': 'UNKNOWN', 'reason': 'missing_record', 'evidence': [], 'status_sources': []}
    target_doi = doi(target)
    if not target_doi or doi(record.get('DOI')) != target_doi:
        return {'prediction': 'UNKNOWN', 'reason': 'doi_mismatch', 'evidence': [], 'status_sources': []}
    relations = record.get('updated-by', [])
    if not isinstance(relations, list):
        return {'prediction': 'UNKNOWN', 'reason': 'invalid_relation_format', 'evidence': [], 'status_sources': []}
    notices = []
    seen = set()
    sources = set()
    has_retraction_signal = False
    reinstatement = False
    malformed_retraction = False
    for item in relations:
        if not isinstance(item, dict):
            continue
        relation_type = str(item.get('type', '')).lower().strip()
        if relation_type in ('reinstatement', 'retraction-withdrawal'):
            reinstatement = True
        if relation_type != 'retraction':
            continue
        reference_doi = doi(item.get('DOI'))
        if not reference_doi:
            malformed_retraction = True
            continue
        has_retraction_signal = True
        sources.add(str(item.get('source') or 'unattributed').lower())
        if reference_doi != target_doi and reference_doi not in seen:
            notices.append({
                'notice_doi': reference_doi, 'type': 'retraction',
                'source': item.get('source'),
                'date': item.get('updated', {}).get('date-time') if isinstance(item.get('updated'), dict) else None,
            })
            seen.add(reference_doi)
    if reinstatement:
        return {'prediction': 'UNKNOWN', 'reason': 'reinstatement_requires_manual_review',
                'evidence': notices, 'status_sources': sorted(sources)}
    if has_retraction_signal:
        return {'prediction': 'RETRACTED',
                'reason': 'typed_retraction_with_distinct_notice' if notices else 'typed_retraction_status_self_only',
                'evidence': notices, 'status_sources': sorted(sources)}
    if malformed_retraction:
        return {'prediction': 'UNKNOWN', 'reason': 'malformed_retraction_relation',
                'evidence': [], 'status_sources': sorted(sources)}
    return {'prediction': 'NOT_RETRACTED', 'reason': 'no_typed_retraction_in_record',
            'evidence': [], 'status_sources': []}


def combine(a, b):
    pa, pb = a['prediction'], b['prediction']
    if a['reason'] == 'reinstatement_requires_manual_review' or b['reason'] == 'reinstatement_requires_manual_review':
        p, reason = 'UNKNOWN', 'reinstatement_requires_manual_review'
    elif 'RETRACTED' in (pa, pb):
        p, reason = 'RETRACTED', 'positive_status_signal'
    elif pa == pb == 'NOT_RETRACTED':
        p, reason = 'NOT_RETRACTED', 'both_no_positive_signal'
    else:
        p, reason = 'UNKNOWN', 'insufficient_evidence'
    notices = b.get('evidence', []) if p == 'RETRACTED' else []
    explanation = ('distinct_notice_doi_available' if notices else ('typed_status_without_notice' if b.get('prediction') == 'RETRACTED' else 'indicator_only') if p == 'RETRACTED' else 'none')
    return {'prediction': p, 'reason': reason, 'evidence': notices, 'explanation_type': explanation}
