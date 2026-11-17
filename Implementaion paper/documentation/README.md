# Final numeric-only PDF reconciliation — 18 November 2026

**Use `paper/manuscript.pdf` as the final paper.** It uses the precise uploaded 7-page paper (not the earlier ZIP's different main.tex) and preserves every alphabetic word, spelling, and grammar choice. Three incorrect numerical values were adjusted; Figure 5 was rerendered with its correct 76-case plotted denominator. The original paper is preserved at `inputs/final_paper_source_verbatim.pdf`.

**Read [`audit/FINAL_NUMERIC_ONLY_RECONCILIATION.md`](audit/FINAL_NUMERIC_ONLY_RECONCILIATION.md)** before the evaluation. It distinguishes the historical 24/40 Crossref rule from the corrected 40/40 rule and describes unsupported causal and latency prose that cannot be corrected without violating the wording restriction. `audit/final_three_pass_validation.json` is the current check report. The archive also includes the original and corrected code, all 18 prompts, raw data, 160 cached API JSON records, figures, tables and results.

**Offline verification:** `python3 scripts/verify_final_package.py`. To reproduce the numerical edits and chart: `python3 scripts/rebuild_final_pdf.py`. `paper/main.tex` is a seven-page PDF import wrapper for exact appearance; the older different text source is preserved in `audit/historical_main_from_incoming_zip.tex`.

---

## Historical project README retained from supplied ZIP

# Retraction Status vs Notice-Link Availability — Audited 18-Prompt Package

**M.Tech AI Research — Lab Assignment 02 | MSE2026009**  
**Corrected reanalysis:** 17 November 2026 | **Source API cache:** 4 November 2026

## Start here

> **Verbatim manuscript update (17 November 2026).** For the explicit word-for-word replacement request, Sections 1–5.7 now follow `Pasted markdown(4).md` exactly as provided, apart from layout whitespace and separation into headings. Do not mistake the historical charts and reintroduced prose for new scientific validation. The pasted text contradicts the earlier audit in its reported Crossref under-detection cause, 40-control classification statement, and 4,000× cache-speedup claim. The independently checked results/data remain available in `results/`, `audit/CORRECTIONS_AND_LIMITATIONS.md`, and `audit/pre_verbatim_v2_manuscript.pdf`. The new paper is a faithful edit of requested text, not an updated accuracy study.


1. Read `paper/manuscript.pdf` for the newly typeset 7-page report with **verbatim user-supplied Sections 1–5.7**. The updated sections preserve the source wording (including mistakes and disputed claims). The abstract, later sections, and references remain from the independently audited v2 report.
2. Read `paper/verbatim_sections_1_to_5.md` for the exact input text. `prompt_outputs/15_manuscript_draft.md` is identical byte-for-byte.
3. Read `audit/CORRECTIONS_AND_LIMITATIONS.md` for an exact list of contradictions and fixes.
4. Read `audit/EVALUATION_CHEATSHEET.md` for an evaluation/viva explanation.
5. See `prompt_outputs/01_workspace.md` through `18_ai_audit.md` for the 18 updated SAVE deliverables.

## What actually changed

The legacy Crossref classifier returned `UNKNOWN` when **any** typed retraction entry used the original article DOI. It rejected **8 self-only cases** and **8 mixed self-plus-distinct-notice cases**, even though all 16 contained typed retraction signals. A simple distinct-notice-required classifier would have detected 32/40, not the observed 24/40. This was a **software/metric design error**,
not proof of absent publisher retraction data.

| Archived 80-DOI sample | OpenAlex B0 | Corrected Crossref B1* | Combined M* |
|---|---:|---:|---:|
| RW-listed retractions labeled RETRACTED | 40/40 | 40/40 | 40/40 |
| Presumed controls labeled NOT_RETRACTED | 36/40 | 36/40 | 36/40 |
| UNKNOWN controls | 4/40 | 4/40 | 4/40 |
| Positive-label recall / end-to-end F1 | 1.000 / 1.000 | 1.000 / 1.000 | 1.000 / 1.000 |

Crossref has **32/40 (80%) distinct notice links**; **8/40** have only self-DOI
typed status updates. For 24 entries (1 positive, 23 controls), the frozen title differs substantially
from the cached Crossref record title, and four controls return 404 from both providers.
These are **agreements with archived nominal benchmark labels**, *not verified
population accuracy*. No independent publisher adjudication for all 80 records
is documented in the supplied archive.

## Reproduce offline (no API calls)

From this project folder, with Python 3.10+ and the dependencies installed:

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 scripts/reanalyze_cached.py
python3 scripts/render_corrected_artifacts.py
python3 scripts/verify_audit.py
```

The corrected replay reads the complete cached JSON records. Run:

```bash
cd paper
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

`xelatex` (or `latexmk -xelatex`) is required for PDF compilation. `bibtex` is **not** required: references
are embedded in `main.tex`; the machine-readable `references.bib` is also provided.
The script `scripts/build_and_run_benchmark.py` is a **safe offline compatibility
wrapper**. It does not rewrite the frozen split or call the live APIs.

## Where all deliverables are

- `prompt_outputs/` — 18 corrected prompt-specific SAVE files.
- `data/raw/retraction-watch-data/retraction_watch.csv` — original 73,597-row file, unmodified.
- `data/splits/benchmark_80_frozen.csv` — original 80-DOI protocol split, unmodified.
- `data/processed/api_cache/` — all 160 original archived API responses, unmodified.
- `results/processed/benchmark_results.csv` — corrected 80-row prediction/evidence CSV.
- `results/processed/metrics_summary.csv` — corrected per-method metrics.
- `results/processed/title_audit.csv` — title mismatches and unresolved DOIs.
- `results/processed/publisher_breakdown.csv` — notice coverage and source attribution.
- `results/figures/` and `paper/figures/` — five corrected figures (PDF, PNG).
- `results/tables/` and `paper/tables/` — five corrected LaTeX tables.
- `paper/main.tex`, `paper/references.bib`, `paper/manuscript.pdf` — editable manuscript and compiled PDF.
- `tests/` — 21 passing unit tests including the new self-DOI edge cases.
- `configs/` — untouched original frozen protocol plus labeled post-hoc amendment.
- `audit/original_results/` — original incorrect results/figures/table/PDF for traceability.
- `audit/original_prompt_outputs/` — original (outdated) prompt outputs, for audit only.
- `audit/original_root_docs/` — historical root documents, for audit only.
- `audit/validation_passes.json` — three **internal** consistency passes and their results (not scientific adjudication).

## Important scientific boundaries

The corrected results are a post-hoc reanalysis of **cached responses from 4 November
2026**, not new live-API results. The source CSV's SHA-256 is independently
recalculated. The original commit ID was supplied with the archive, but Git history
is not included; do not say the GitLab commit was independently checked.

Do **not** claim the revised study proves better recall than Crossref or that publisher
retraction tags were absent. Do **not** interpret provisional label agreement as a
clinical-style accuracy or independent verification claim. This case study demonstrates
a critical design distinction: retraction status versus a separately identified notice DOI.

## Post-review audit addendum

- **Original error traced precisely:** 8 self-only positives and 8 mixed self-plus-distinct positives were marked UNKNOWN by the legacy rule; another 24 distinct-only cases were positive. See `results/processed/legacy_rule_failures.csv` and `audit/original_scripts/core_legacy.py`.
- **Title screening by label:** 1 of 40 RW-listed positives and 23 of 40 presumed controls have low DOI-title similarity; another 4 controls have missing Crossref records. See `paper/tables/title_integrity_table.tex`.
- **Metrics:** legacy determinate F1 = 1.000, end-to-end F1 = 0.750 and decision coverage = 60/80; corrected coverage = 76/80. All are agreement with provisional labels, not independently verified accuracy.
- **Verification status:** 3 **internal** source/execution/presentation passes. Fresh network queries were attempted but unsuccessful here. The optional `scripts/live_api_spotcheck.py` is intended for a network-connected machine, not evidence that requests were completed.
- **Manual adjudication queue:** `audit/independent_adjudication_queue.csv` includes all 40 controls and 8 self-only positives. All 48 cases remain **PENDING**.
- **Figure/table regeneration:** `python3 scripts/render_corrected_artifacts.py` regenerates 5 active figure pairs and 5 LaTeX tables; titles, legends and numeric case studies have been rechecked.
