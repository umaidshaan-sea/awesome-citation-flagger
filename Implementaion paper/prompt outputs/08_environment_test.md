# Prompt 08 — Reproducible environment test

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Executable local environment and results, with device claims separated from archived history.

The current audited environment successfully ran `python3 -m unittest discover -s tests -v`, `python3 scripts/reanalyze_cached.py`, and `python3 scripts/render_corrected_artifacts.py`, followed by a two-pass `pdflatex` compile. This exercise did not run a new experiment on the student's MacBook M2 and did not make network calls.

The legacy environment log remains at `results/logs/environment_smoke_test.json`; it is historical self-reported evidence from the original archive, not new verification. The corrected replay needs no GPU, and the primary file inputs are shipped with the ZIP.

**Setup:** create a virtual environment, install `requirements.txt`, run the tests and cached replay from the root folder. For PDF output, use installed `pdflatex` (references embedded in the LaTeX file). The source provides separate manifest and audit reports so a new machine can detect missing files.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/08_environment_test.md`.
