# Correction and discrepancy ledger — 17 November 2026

This audit compares the exact supplied paper PDF with the original ZIP's frozen split,
archived provider JSON, original results, plots, scripts, and bibliography. The original
PDF and the ZIP's `paper/main.pdf` were SHA-256-identical. The original data remains
in `audit/original_results/` and `audit/original_scripts/`.

## Critical corrections with evidence

| # | Original assertion / artifact | Actual evidence | Corrective action |
|---|---|---|---|
| 1 | Crossref detected only 24/40 because it had no typed update relations for 16 retractions | **All 40** positive Crossref cached records contain at least one valid `updated-by` entry of type `retraction`. The 16 legacy UNKNOWNs had self-DOI relations; **8 also had different notice DOIs**. | Rewrite status decision; present exact legacy **self-DOI ambiguity precedence bug** (eight self-only + eight mixed cases), not true status recall. |
| 2 | 40% publisher Crossmark deposit omission caused status under-detection | Cases labeled unknown contain typed retraction tags and in some cases publisher-attributed tags | Withdraw all publisher-omission and publisher-compliance causal claims. |
| 3 | 60% of positive papers link to distinct notice DOIs | Cached result CSV and Crossref relations show **32/40 = 80%** | Recompute all percentages, tables and figures. |
| 4 | IEEE had zero typed retraction relations | All four IEEE positives contain typed self-DOI retraction updates; none has different notice DOI | Describe absence of **distinct notice linkage**, not absence of status data. |
| 5 | All negative controls correctly classified | Four nominal negative controls produce HTTP 404 / UNKNOWN on both APIs | Treat as unresolved, never as TN. Corrected TN=36, UNKNOWN=4 for all three methods. |
| 6 | One publisher grouping listed 7 major strata (Nature, Science, Elsevier, Wiley, Springer, PLOS, IEEE) | Actual split includes 14 Springer/Nature/BMC/Cureus, 8 Elsevier, 5 Wiley, 5 PLOS, 4 IEEE, 2 PNAS, 2 Other | Group categories directly from archived publisher strings; document that groups are not a population sample. |
| 7 | Specific disagreement case-study DOIs and dates without supporting rows | Several mentioned article DOIs in legacy section 5.4 are absent from the 80 selected records | Replace examples by directly traceable cached cases; omit unsupported dates. |
| 8 | All 80 gold labels were independently publisher-verified | Positive list imported from RW; presumed negatives use simple DOI landing links; no full independent adjudication ledger | Describe results as **nominal benchmark-label agreement** only. |
| 9 | Control titles and DOIs were reliably matched | **24 low title-similarity cases** (1 RW positive; 23 presumed controls; threshold <0.55), plus four control 404s; e.g. `10.1007/bf00993078` is *Balanced Cooperative Modeling*, not *Support-Vector Networks*. | Preserve frozen DOIs, output `title_audit.csv`, display provider title when available; require independent adjudication before true accuracy claims. |
| 10 | 60% separate notices described as verified publisher evidence | Of 40 positives, 29 have a publisher-attributed typed status signal and 37 RW-attributed; 20 have publisher-attributed separate notice entries. Sources overlap and DOI links were not manually verified. | Report provider metadata provenance, never independent notice proof. |
| 11 | Original sensitivity curve treated 0.40 as a real Crossref status-abstention rate | 0.40 is a postulated *legacy classifier-rule* abstention rate, not Crossref status absence | Remove false causal interpretations and synthetic sensitivity figure from active paper. |
| 12 | Latency figure reported in-memory cache <0.5ms as measured and >4,000x faster | Legacy figure code contains `np.random.uniform(0.1, 0.45)` to generate the supposed measured cache timings; reported SD also disagreed between table and prose | Remove performance/latency claims; archive historical generator and chart for inspection. |
| 13 | Bibliography claimed verified metadata but supplied incorrect Cohan author and Frampton title; frozen control used incorrect DOI for SVM | ACL Anthology identifies Field Cady as Cohan coauthor; PLOS ONE gives exact Frampton title; official DOI match contradicts control title | Correct bibliography; flag control inconsistencies instead of silently substituting papers. |
| 14 | Claimed independent cross-source corroboration | Crossref docs describe RW records integrated into Crossref; OpenAlex docs describe RW as an `is_retracted` input | Explicitly identify dependency/circularity; no accuracy or independence claim. |
| 15 | Stated original protocol remained frozen after correction | Repaired classifier is a new rule applied after seeing the legacy results | Keep `protocol_v1.yaml` unchanged and create a dated post-hoc amendment. |
| 16 | Full method superiority claimed with $p<0.0001$ | Corrected OpenAlex, Crossref and combined produce identical 76 determinate correct-label matches and 4 UNKNOWNs | No superiority or significance claim; identical paired outcomes have zero discordance. |

## What was internally checked

- All archived 80 Crossref and 80 OpenAlex cache files were read and paired by DOI hash.
- Dataset SHA-256 was recomputed from the exact CSV bytes.
- The 80 immutable frozen DOI strings remain unchanged and unique.
- Corrected classification metrics and per-publisher evidence were recalculated from raw cached responses.
- All active tables and figures regenerate from the recalculated output, with no randomness.
- Code unit tests and PDF compilation were checked, including added error-regression tests.

## What was **not** verified

- Whether the nominal 40 control labels are genuinely non-retracted, or all 40 positive
  cases are independently publisher-confirmed, as of November 2026.
- Whether the API responses or notice URLs remain identical after 4 November 2026.
- Whether all printed notice DOIs resolve to genuine independent publisher notices.
- The repository's original GitLab commit ID; the ZIP does not include Git history.
- Accuracy on a new non-circular, independently adjudicated test set.
- Latency, cache speedups or measured throughput on the student's MacBook hardware.

## Preservation and transparent interpretation

Historical artifacts with superseded statements remain under `audit/original_...`
for forensic traceability. They are **not** current results and should not be cited
in a new submission. Full limitations are stated in the corrected manuscript,
`STATUS.md` and `prompt_outputs/16_technical_peer_review.md`.

## 17–23. Corrections from the second critical review (17 November 2026)

| # | Identified issue | Resolution | Reproducible evidence |
|---|---|---|---|
| 17 | Conflicting descriptions of original bug | Legacy code marks `ambiguous=True` on any self-DOI typed retraction; this overrides a different valid notice. Breaks down into **8 self-only UNKNOWN + 8 mixed UNKNOWN**; 24 distinct-only remain positive. | `audit/original_scripts/core_legacy.py`; `results/processed/legacy_rule_failures.csv`; `tests/test_archived_invariants_v2.py` |
| 18 | Three "independent" validation passes | Renamed to **three internal consistency passes** (source, execution, PDF presentation), never ground-truth adjudication. | `scripts/verify_audit.py`; `audit/validation_passes.json` |
| 19 | Misused bibliography [8] | Citation now attaches to the public Retraction Watch GitLab dataset; the supporting ZIP is described without citing GitLab as its source. Crossref blog date confirmed **29 January 2025**. | `paper/main.tex`; official Crossref page |
| 20 | Contradictory case-study row and missing fourth explanation | Table states exactly **2 self/0 distinct**, **1 self/2 distinct**, **1 self/1 distinct + 1 erratum**, **1 self/0 distinct** for the four displayed cases; prose discusses all four. | `paper/tables/case_studies_table.tex`; cached JSON |
| 21 | Misleading 100% score framing and missing F1 | Table includes **determinate F1**, **end-to-end F1**, **positive abstention**, **control abstention**, and **coverage**, explicitly as provisional benchmark-label agreement. | `paper/tables/comparative_metrics_table.tex` |
| 22 | Imbalanced control/title mismatch distribution | A new class-stratified table reports **positive 1/40 mismatch, control 23/40 mismatch, plus four missing control records**; 48-item manual review queue remains PENDING. | `results/processed/title_audit_by_class.csv`; `audit/independent_adjudication_queue.csv` |
| 23 | Truncated raw hash, overlapped chart legends, omitted external check status | PDF includes full 64-character SHA-256; figure legends moved outside plots; attempted online access failed, and optional standalone check script is provided with no fabricated live results. | `paper/main.tex`; `results/figures/`; `audit/LIVE_AND_MANUAL_VERIFICATION_STATUS.md` |

No source-label accuracy, fresh API superiority, independent negative adjudication, or publisher compliance can be inferred from these internal results.
