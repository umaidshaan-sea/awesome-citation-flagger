# Prompt 01 — Establish the research workspace

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Audited research workspace and artifact inventory. The project question is how machine-readable Crossref retraction statuses, OpenAlex flags, and notice DOIs can be reconciled for citation checks. The final scope is explicit retractions only, not the broader topic of all outdated science.

**Workspace:** `data/raw/`, `data/splits/`, `data/processed/api_cache/`, `src/`, `scripts/`, `tests/`, `results/`, `paper/`, and `audit/` are retained. The 160 original archived API JSON files and the original Retraction Watch CSV were preserved. The final manuscript is `paper/manuscript.pdf`.

**Source policy:** Facts must trace to either supplied artifacts or cited external documentation. Original absolute `file:///Users/...` links were removed from active docs. An original paper and prompts are retained under `audit/original_...` as historical, superseded material. The workspace cannot establish the alleged original Git commit from the archive because `.git` history was not included.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/01_workspace.md`.
