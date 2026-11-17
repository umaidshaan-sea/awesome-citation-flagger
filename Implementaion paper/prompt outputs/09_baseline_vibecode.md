# Prompt 09 — Code provenance and baseline logic

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Source-level review of AI-assisted implementation.

Key modules: `src/core.py` normalizes DOIs and implements B0, corrected B1* and M*. `src/providers.py` retains original request/caching functions; the audited results use cached inputs rather than fresh requests. `src/metrics.py` calculates provisional label-agreement metrics. `scripts/reanalyze_cached.py` rereads every cached response and writes all 80 decisions. `scripts/render_corrected_artifacts.py` creates the active figures and tables.

**Original coding bug:** an article-DOI retraction relation was marked ambiguous if it lacked a separate notice; even records containing both a valid notice DOI and a self-DOI were discarded. **Code correction:** `crossref()` now reports a positive typed status and stores a separate notice DOI only if truly distinct. Added tests exercise self-only, mixed, reinstatement, multi-DOI and archived-case invariants (21 total passing).

Original source files are preserved in `audit/original_scripts/`. No human-authorship claim is inferred from the code's style or logs.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/09_baseline_vibecode.md`.

**Exact failure:** eight self-only and eight mixed records were flagged UNKNOWN because legacy ambiguous-flag precedence overrode any valid distinct notice.
