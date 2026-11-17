import hashlib
import json
import random
from pathlib import Path
import pandas as pd
from .core import doi

REQUIRED = {'OriginalPaperDOI', 'RetractionNature', 'Record ID', 'RetractionDOI'}

def load_candidates(path, seed=20261028, positive_limit=10, correction_limit=10):
    df = pd.read_csv(path, dtype=str, low_memory=False).fillna('')
    missing = REQUIRED.difference(df.columns)
    if missing:
        raise ValueError(f'Missing Retraction Watch columns: {sorted(missing)}')
    df = df[~df['OriginalPaperDOI'].str.contains(';', regex=False)].copy()
    df['normalized_doi'] = df['OriginalPaperDOI'].map(doi)
    df = df[df['normalized_doi'] != ''].copy()
    df['nature'] = df['RetractionNature'].str.strip().str.lower()
    grouped = df.groupby('normalized_doi')['nature'].agg(lambda x: set(x))
    retracted = {d for d, kinds in grouped.items() if 'retraction' in kinds}
    correction_only = {d for d, kinds in grouped.items() if 'correction' in kinds and 'retraction' not in kinds and 'reinstatement' not in kinds and 'expression of concern' not in kinds}
    rng = random.Random(seed)
    pos = sorted(retracted); neg = sorted(correction_only)
    rng.shuffle(pos); rng.shuffle(neg)
    rows = [{'doi': d, 'candidate_category': 'RW_RETRACTION', 'gold_label': 'UNVERIFIED', 'gold_evidence_url': ''} for d in pos[:positive_limit]]
    rows += [{'doi': d, 'candidate_category': 'RW_CORRECTION_ONLY_NOT_VERIFIED_NEGATIVE', 'gold_label': 'UNVERIFIED', 'gold_evidence_url': ''} for d in neg[:correction_limit]]
    return pd.DataFrame(rows), {'source_sha256': hashlib.sha256(Path(path).read_bytes()).hexdigest(), 'rows': len(df), 'eligible_retracted_dois': len(retracted), 'correction_only_candidate_dois': len(correction_only), 'selected': len(rows), 'seed': seed}
