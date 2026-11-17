# Prompt 09 Output: Baseline Implementation and Prompt-to-Code Log

> **Phase III Baseline Deliverable:** Modular implementation of single-source baselines B0 (OpenAlex) and B1 (Crossref), dataset ingestion, caching, and evaluation metrics with verified code explanations and unit tests.

---

## 1. Official Handbook Prompt Specification
- **Prompt:** Vibe-code one baseline module at a time
- **Official SAVE Deliverable:** Working baseline plus code understanding and prompt-to-code log.
- **Evidence Status:** VERIFIED (grounded in inspected source files and passed test suite).
- **Substantive Artifact Links:**
  - Source Modules: [core.py](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/src/core.py), [data.py](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/src/data.py), [providers.py](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/src/providers.py), [metrics.py](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/src/metrics.py), [validate_rw.py](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/src/validate_rw.py)
  - Test Suite: [test_core.py](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/tests/test_core.py)
  - Unit Test Execution Log: [local_unit_tests_2026-10-30.txt](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/results/logs/local_unit_tests_2026-10-30.txt)

---

## 2. Baseline Architecture & Module Breakdown

### Module 1: `src/validate_rw.py` (Dataset Schema Auditor)
- **Purpose:** Parses and validates the official Retraction Watch CSV.
- **Logic:** Confirms required columns (`Record ID`, `OriginalPaperDOI`, `RetractionNature`, etc.); applies strict single-DOI regex `^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$`; filters out multi-DOI entries; outputs summary statistics and SHA-256 hash.
- **Input:** Path to `retraction_watch.csv`.
- **Output:** Validated dictionary and JSON summary log.
- **Unit Test:** `tests/test_validate_rw.py` (missing columns, missing file, valid fixture counts).

### Module 2: `src/data.py` (Candidate Sampling & Leakage Barrier)
- **Purpose:** Deterministically samples evaluation candidates under seed `20261028`.
- **Logic:** Isolates single-DOI retracted and unretracted records; creates stratified partitions across publication years; exports metadata manifest with cryptographic verification hash.
- **Input:** Validated DataFrame, positive count, negative count, seed.
- **Output:** `data/splits/` CSV candidates.
- **Unit Test:** `test_multi_doi_not_selected_even_when_regex_matches`.

### Module 3: `src/providers.py` (API Client & Persistent Disk Caching)
- **Purpose:** Manages polite, rate-limited HTTP requests to Crossref REST API and OpenAlex Works API.
- **Logic:** Implements exponential backoff, SHA-256 DOI file caching in `data/processed/api_cache/`, custom User-Agent headers, and timeout error trapping. Returns raw JSON dictionaries.
- **Input:** Normalized canonical DOI, provider identifier (`crossref` / `openalex`).
- **Output:** Dict containing HTTP status, response payload, timestamp, and cache flag.

### Module 4: `src/core.py` (Classification Rules & Consensus Engine)
- **Purpose:** Implements decision logic for Baseline B0, Baseline B1, and Proposed Consensus Method ($M_{\text{prop}}$).
- **Logic:**
  - `classify_openalex(oa_json)`: Inspects `is_retracted` boolean field.
  - `classify_crossref(cr_json)`: Inspects `relation` array for `type == 'retraction'` and `update-to` object.
  - `classify_union(cr_json, oa_json)`: Reconciles signals; attaches provenance evidence links; returns `RETRACTED`, `NOT_RETRACTED`, or `UNKNOWN`.
- **Input:** Raw JSON payloads from providers.
- **Output:** Prediction tuple `(label, reason, evidence_dict)`.
- **Unit Test:** `tests/test_core.py` (`test_crossref`, `test_oa`, `test_union`, `test_doi`).

### Module 5: `src/metrics.py` (Independent Evaluation Auditor)
- **Purpose:** Evaluates model predictions against independently verified ground-truth labels.
- **Logic:** Strictly blocks scoring if any instance has `UNVERIFIED` label. Computes TP, FP, TN, FN, Abstentions, Determinate F1, and End-to-End F1.
- **Input:** Predictions DataFrame, verified ground-truth DataFrame.
- **Output:** Comprehensive dictionary of evaluation metrics.
- **Unit Test:** `tests/test_audit_edges.py` (`test_abstention_cannot_inflate_f1_end_to_end`, `test_unverified_scoring_refused`).

---

## 3. Prompt-to-Code Engineering Log

```
+-----------------------------------------------------------------------------------+
| ITERATION 1: Core Classifier & Providers                                          |
| - Implemented canonical DOI normalization function                                |
| - Built OpenAlex and Crossref provider wrappers with disk caching                 |
| - Verified against synthetic test fixtures                                        |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| ITERATION 2: Dataset Ingestion & Schema Validation                                |
| - Built `src/validate_rw.py` to ingest 73k-row Retraction Watch CSV               |
| - Enforced strict single-DOI regex                                                |
| - Validated file integrity via SHA-256 computation                                |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| ITERATION 3: Metric Computation & Abstention Safeguards                           |
| - Defined `F1_determinate` and `F1_end_to_end`                                     |
| - Enforced refusal to score unverified labels                                     |
| - Verified all unit tests locally (13/13 PASS)                                    |
+-----------------------------------------------------------------------------------+
```

---

## 4. Actual Execution Evidence
```
Ran 13 tests in 0.012s
OK
- test_abstention_cannot_inflate_f1_end_to_end: PASS
- test_missing_source_unknown: PASS
- test_multi_doi_not_selected_even_when_regex_matches: PASS
- test_reinstatement_requires_review: PASS
- test_unverified_scoring_refused: PASS
- test_crossref: PASS
- test_doi: PASS
- test_oa: PASS
- test_score_refusal: PASS
- test_union: PASS
- test_missing_columns_fails: PASS
- test_missing_file_fails: PASS
- test_valid_fixture_counts_and_no_ground_truth_claim: PASS
```

---

## 5. Actual Outcome
- Baseline modules and consensus engine fully implemented and unit-tested.
- Code understanding and input/output shapes documented.
- 13/13 unit tests pass.
- **Official SAVE Deliverable:** Working baseline plus code understanding and prompt-to-code log recorded.
