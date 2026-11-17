# Prompt 07 — Protocol and dated correction

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Original frozen protocol and explicit post-hoc amended implementation.

Original `configs/protocol_v1.yaml` remains untouched. It records a benchmark of N=80, labels 40/40, seed 20261028 and the original planned end-to-end F1 metric. The corrected classifier was implemented only after reviewing source records and therefore must **not** be presented as pre-registered.

A separate `configs/analysis_amendment_2026-11-17.yaml` documents the change. Frozen DOI strings, source labels, raw CSV and 160 response JSON are unchanged. Primary comparison is now source-status vs distinct-notice evidence, with the legacy classifier retained solely for diagnostic comparison. No new test data were sampled after the correction.

**Fair future test:** create an independently verified and newly locked split, record a fresh API capture timestamp, predefine exact status and notice rules, exclude self-referential links from the distinct-notice rate and compare on the same DOIs.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/07_experiment_blueprint.md`.
