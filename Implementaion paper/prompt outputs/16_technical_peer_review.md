# Prompt 16 — Technical peer-review audit and response

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Skeptical review with findings, evidence and revision responses.

**Major #1 — Invalid source comparison (resolved).** Crossref contains typed retractions for all 40 positives; 16 abstentions came from the classifier rule. Response: updated `src/core.py`, generated corrected 80-row CSV, and added regression tests.

**Major #2 — Missing independent labels (open).** Positive cases derive from RW; control labels were not validated independently. Response: paper reports agreement with provisional benchmark labels, not verified accuracy; future independent adjudication required.

**Major #3 — DOI/title mismatches (open).** 24 low-similarity title pairs (1 positive, 23 controls) and four missing control records. Response: preserved frozen DOI strings and issued `title_audit.csv`; did not silently swap cases post hoc.

**Major #4 — False provenance and notice claims (resolved/qualified).** Status signal not equal to distinct notice. Response: report 32/40 links; publisher-sourced and RW-sourced evidence separately counted; no proof of publisher noncompliance.

**Major #5 — Synthetic latency data (resolved).** Original generated warm-cache latencies were random numbers. Response: removed latency figure/table from active conclusions.

**Minor — DOI/citation and typography (resolved).** Corrected Cohan and Frampton references; regenerated vector figures and LaTeX tables and compiled without overflow warnings. See `audit/validation_passes.json`.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/16_technical_peer_review.md`.

**Second-review response:** corrected ambiguous flag precedence description (8 self-only, 8 mixed), updated case-study relation counts, full raw SHA, five tables, charts without overlapping legends, and clarified "internal consistency passes". Exact Crossref API live check remains unavailable; no manual adjudication is claimed.
