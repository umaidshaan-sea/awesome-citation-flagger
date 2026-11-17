# Prompt 03 — Literature to implementation bridge

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Mapping from sources to code to a minimal reproducible test.

| Source / concept | Selection | Implementation | Measured outcome |
|---|---|---|---|
| Priem et al. 2022, OpenAlex | `is_retracted` status baseline | `src/core.py::openalex` | 40/40 positive label matches |
| Crossref 2025 retraction integration | Typed Crossref `updated-by` status | `src/core.py::crossref` | 40/40 positive label matches after repair |
| Crossref registering updates | Different DOI can be a notice | `crossref` returned `evidence[]` | 32/40 have a distinct notice DOI |
| Reliability of abstention | API missing/unindexed not clean | `src/core.py::combine` and `src/metrics.py` | Four controls unresolved across all methods |

**Executable baseline:** `python3 scripts/reanalyze_cached.py`. **Data:** frozen `data/splits/benchmark_80_frozen.csv` and 160 archived cache responses. **Metrics:** conditional label recall, end-to-end F1, notice-link proportion, coverage. **Limits:** dataset leakage through Retraction Watch; independently verified labels absent.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/03_literature_bridge.md`.
