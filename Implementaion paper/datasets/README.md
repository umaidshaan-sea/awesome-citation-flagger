# Dataset Documentation: Crossref Retraction Watch & Evaluation Splits

## 1. Overview & Provenance
- **Dataset Name:** Retraction Watch Database (Crossref Open Data Snapshot)
- **Official Provider:** Crossref & The Center for Scientific Integrity
- **Repository URL:** `https://gitlab.com/crossref/retraction-watch-data.git`
- **Tracked Git Commit:** `fb5f174f8476824deaf340693f9a819ce5e29ded`
- **File Name:** `data/raw/retraction-watch-data/retraction_watch.csv`
- **File Size:** ~23.4 MB
- **SHA-256 Checksum:** `e5351ee51ab3f1da7fe98b3bd6c5c58049b8bff4705949ef6fd4f1a1315dd0ea`
- **Total Raw Rows:** 73,597
- **Eligible Single-DOI Rows:** 67,628 (unique original DOIs: 64,566)
- **License:** Open data under Creative Commons Public Domain Dedication (CC0) / Crossref open distribution terms.

## 2. Shared Data Provenance & Epistemic Audit Note
- **CRITICAL AUDIT NOTE:** OpenAlex `is_retracted` is directly populated using Retraction Watch data. Crossref distributes Retraction Watch data in partnership with The Center for Scientific Integrity.
- Consequently, Crossref and OpenAlex DO NOT constitute independent ground-truth sources.
- In this study, ground truth for the frozen evaluation split is independently corroborated against:
  1. Authoritative publisher retraction notices and errata pages (e.g., Nature, Science, Elsevier, Springer).
  2. Crossref explicit machine-readable `updated-by` relation records.

## 3. Data Dictionary (Key Columns)

| Column Name | Description | Validation Rule |
|---|---|---|
| `Record ID` | Retraction Watch internal primary key | Integer ID |
| `OriginalPaperDOI` | DOI of the retracted or affected article | Non-empty, single valid DOI regex `10.\d{4,9}/[-._;()/:A-Za-z0-9]+` |
| `RetractionDOI` | DOI of the formal retraction notice | Valid DOI regex or empty if unassigned |
| `RetractionNature` | Classification of the status event | `Retraction`, `Correction`, `Expression of Concern`, `Reinstatement` |
| `OriginalPaperDate` | Date of original publication | `MM/DD/YYYY` or `YYYY-MM-DD` |
| `RetractionDate` | Date of retraction notice | `MM/DD/YYYY` or `YYYY-MM-DD` |
| `Reason` | Categorized reasons for retraction | Semicolon-delimited descriptive taxonomy |
| `Journal` | Journal in which paper appeared | String |
| `Publisher` | Publisher name | String |

## 4. Exclusion & Preprocessing Criteria
1. **Multi-DOI Field Exclusion:** 17 records in the raw dataset contain multiple semicolon-delimited DOIs in `OriginalPaperDOI`. These are excluded from automated 1-to-1 evaluation to prevent resolution ambiguity.
2. **Missing DOI Exclusion:** 5,952 records lack a valid DOI (e.g., legacy pre-DOI publications). Excluded from automated API benchmarking.
3. **Reinstatement Handling:** Papers tagged as reinstated are isolated and require manual editorial review.

## 5. Directory Structure
```
data/
├── README.md               # This documentation file
├── raw/
│   └── retraction-watch-data/
│       └── retraction_watch.csv  # Official snapshot (73,597 rows)
├── processed/
│   ├── valid_dois_manifest.csv   # Pre-filtered eligible DOIs
│   └── selection_manifest.json   # Reproducible sampling metadata
└── splits/
    ├── benchmark_80_frozen.csv   # 40 positive + 40 negative control benchmark
    └── pilot_candidates_UNVERIFIED.csv # Preliminary exploratory subset
```
