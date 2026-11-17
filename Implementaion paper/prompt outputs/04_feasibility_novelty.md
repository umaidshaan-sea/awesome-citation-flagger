# Prompt 04 — Feasibility and novelty decision

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Scientific go/no-go and smallest viable study.

**GO** for an engineering/error-analysis case study: demonstrate that `type=retraction` is a status signal even when the relation DOI is the original DOI, without pretending that the latter is a different notice DOI. **NO-GO** for the original novelty claim (combined method improves detection recall over corrected Crossref), as all three corrected methods yield 40/40 positive label matches.

**Compute:** Cached JSON replay, tests and plots run on ordinary Python CPU; MacBook M2 or free Colab is sufficient. The final work does not require GPU training or new model architecture.

**Availability:** Source CSV and API caches are included; exact raw CSV SHA checked. Source repository commit ID not independently established (no `.git`). **Fallback:** If live APIs change or throttle, the archived replay still gives bitwise reproducible per-record decisions. **Before a publication-quality validation:** independently inspect all 80 nominal labels, replace bad control IDs under a new pre-registered protocol, and obtain independent held-out records.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/04_feasibility_novelty.md`.
