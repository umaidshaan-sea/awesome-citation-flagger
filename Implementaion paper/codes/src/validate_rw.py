"""Validate the Retraction Watch CSV without making ground-truth claims."""
import hashlib
import json
from pathlib import Path
import pandas as pd
from .core import doi

REQUIRED = ('Record ID', 'OriginalPaperDOI', 'RetractionDOI', 'RetractionNature')


def validate_csv(path):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f'Retraction Watch CSV not found: {path}')
    df = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f'Missing required CSV columns: {missing}. Actual columns: {df.columns.tolist()}')
    values = df['OriginalPaperDOI'].map(doi)
    usable = values.ne('')
    # Some DOI fields may contain multiple DOI strings; do not silently count them as one.
    multiple = df['OriginalPaperDOI'].str.contains(';', regex=False)
    single = usable & ~multiple
    natures = df['RetractionNature'].str.strip().str.lower()
    result = {
        'source_path': str(path),
        'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'rows': int(len(df)),
        'columns': df.columns.tolist(),
        'rows_with_valid_single_original_doi': int(single.sum()),
        'rows_with_multi_doi_field_excluded': int(multiple.sum()),
        'rows_with_missing_or_invalid_original_doi': int((~usable & ~multiple).sum()),
        'unique_eligible_original_dois': int(values[single].nunique()),
        'rows_tagged_retraction': int((natures == 'retraction').sum()),
        'rows_tagged_correction': int((natures == 'correction').sum()),
        'labels_verified': False,
        'heldout_split_frozen': False,
    }
    if not len(df):
        raise ValueError('Retraction Watch CSV is empty')
    if not single.any():
        raise ValueError('No unambiguous single original-paper DOIs found')
    return result
