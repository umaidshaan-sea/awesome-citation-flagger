# Prompt 10 — Baseline validation and reproduction

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Reproduction commands and actual test outcomes.

```
python3 -m unittest discover -s tests -v
python3 scripts/reanalyze_cached.py
python3 scripts/render_corrected_artifacts.py
```

The corrected suite contains 21 tests (13 original, five correction regression tests and three archived-case invariant tests); they passed in the current audit. Offline replay checks 80 unique frozen DOIs, all expected archive hash-derived cache locations, 40 positive source labels and 40 presumed controls. Every positive cached Crossref record contains at least one typed retraction relation. The corrected baseline identifies 40/40; original self-DOI ambiguity-rule baseline recorded 24/40.

**Critical distinction:** passing source-code tests and reproducing archival API outputs does not verify whether the nominal labels reflect actual historical retractions. The audited outcome is conditional benchmark-label agreement only.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/10_baseline_reproduction.md`.
