# Prompt 11 — Debugging and corrections log

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Real identified failures, minimal code fixes, and regression evidence.

1. **Self-DOI bug:** original `src/core.py` treated a typed `retraction` relation referencing the original DOI as ambiguous, even though it establishes a status signal. Fixed status decision without inventing a separate notice.
2. **Mixed self + notice bug:** original rule rejected some articles that contained both types of retraction records. Fixed by recording valid notice entries independently and maintaining the status assertion.
3. **Notice percentage error:** original Table 3 contained 32/40 notice links but labelled this 60%; recalculated to 80% everywhere.
4. **Publisher attribution error:** rejected self-DOI cases were described as absent publisher deposits, although the cached records include typed updates. Removed compliance claims.
5. **Control metadata error:** 24 low-similarity title pairs and four 404s found; retained frozen IDs and published audit ledger rather than silently swapping cases.
6. **Synthetic cache time:** original plotting script uses `numpy.random.uniform` for cache timings. Removed figure and speedup claims from the active paper.

**Regression tests:** `tests/test_correction_2026.py` and all original tests. **Trace:** `audit/CORRECTIONS_AND_LIMITATIONS.md`.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/11_debugging_fixes.md`.
