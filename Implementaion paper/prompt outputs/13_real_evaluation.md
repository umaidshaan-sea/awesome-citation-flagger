# Prompt 13 — Evaluate using real archived outputs

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Corrected metric script, 80-row CSV, per-case evidence, tables and figures.

The reanalysis loads all 160 archived real API responses captured 2026-11-04; it does not synthesize new provider outputs or claim fresh live requests. The accurate reclassification is in `results/processed/benchmark_results.csv`; metrics in `results/processed/metrics_summary.csv`; evidence counts in `results/processed/audit_statistics.json`.

| Method | TP | TN | Unknown | Positive-label recall | End-to-end F1 |
|---|---:|---:|---:|---:|---:|
| B0 OpenAlex | 40 | 36 | 4 | 1.000 | 1.000 |
| B1* Crossref corrected | 40 | 36 | 4 | 1.000 | 1.000 |
| M* combined corrected | 40 | 36 | 4 | 1.000 | 1.000 |
| Legacy B1 (diagnostic) | 24 | 36 | 20 | 0.600 | 0.750 |

Four 404s occur on controls in both providers. 32/40 positives have a distinct notice DOI; eight have only self-DOI status signals. The archived data has no independent full-benchmark adjudication; accuracy should not be claimed. Original incorrect predictions remain in `audit/original_results/`.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/13_real_evaluation.md`.

**Further audited outputs:** `results/processed/legacy_rule_failures.csv` has 16 rows (8 self-only + 8 mixed); `title_audit_by_class.csv` has 1 flagged positive, 23 flagged controls and 4 unavailable controls. Determinate F1 is 1.000 for all four rows; legacy decision coverage is 60/80, corrected coverage 76/80.
