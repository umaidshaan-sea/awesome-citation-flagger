# Prompt 06 — Dataset and baselines

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Archived dataset manifest, baseline definitions and exact provenance.

The unmodified Retraction Watch snapshot is `data/raw/retraction-watch-data/retraction_watch.csv` (SHA-256 `e5351ee51ab3f1da7fe98b3bd6c5c58049b8bff4705949ef6fd4f1a1315dd0ea`, 73,597 rows). The 80 unique DOI records in the frozen split consist of 40 RW-listed retractions and 40 hand-picked presumed controls. Crossref and OpenAlex archived response caches contain 80 JSON records each, with four 404 responses per provider on the same control DOIs.

**Baselines:** B0=OpenAlex boolean; B1*=Crossref any valid typed retraction relation; M*=positive if either baseline positive, negative if both negative, otherwise UNKNOWN, with reinstatement review. Distinct notice DOI is counted only when different from the input DOI.

**Independent verification state:** no complete external ground-truth adjudication file; 24 mismatches (1 positive, 23 controls) and four missing-record titles (see `results/processed/title_audit.csv`). Do not call all cases independently verified.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/06_dataset_comparators.md`.

**Manual verification:** `audit/independent_adjudication_queue.csv` contains 40 control and 8 self-only cases, all PENDING; live API was not successfully rerun.
