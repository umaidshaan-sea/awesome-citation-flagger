# Prompt 14 — Corrected results and limitations

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Reconciled empirical interpretation.

**Confirmed by archived API JSON:** typed Crossref retraction metadata is present for all 40 RW-listed positives, including 16 cases the original code marked UNKNOWN. **Separate evidence:** 32/40 (80%) have a distinct notice DOI; eight have only status metadata referencing the article DOI. **Source attribution:** 29/40 positives have publisher-sourced typed signals, 37/40 RW-sourced signals, and 26/40 both, indicating substantial source overlap.

**Replaced interpretation:** The original 40% publisher omission explanation was unsupported. It arose from status-vs-notice logic, not genuinely absent `updated-by` arrays. Avoid quoting the original misleading 0.750 F1 as the actual Crossref status baseline.

**Limits:** all positives selected from RW, negative controls not independently adjudicated, 24 mismatched frozen titles (1 RW positive, 23 controls), four 404s, no new live query, small curated sample. A separate notice DOI is not automatic proof of independently visited publisher landing pages. Results support cautious metadata pipeline engineering, not a novel independent accuracy claim.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/14_results_discussion.md`.

**Important:** 8 of 16 legacy abstentions had distinct notice DOIs alongside self-DOI entries; 8 were self-only. Absent notice linkage cannot explain all 16 failures by itself.
