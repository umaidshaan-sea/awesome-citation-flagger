# Deviations Log

**Project:** *An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature*  
**Student:** Md Umaid Shaan (MSE2026009)  
**Lead Auditor:** Autonomous MTech AI Research-Engineering Lead  
**Last Updated:** 2026-11-04  

---

## Logged Methodological & Engineering Deviations

### DEV-001: Operational Narrowing to Formal Retractions
- **Initial Proposal in Review:** The 12-page literature review proposed flagging all forms of outdated citations, including epistemic obsolescence, superseded findings, corrections, and retractions.
- **Audited Deviation:** Constrained the empirical experimental study strictly to explicit, formal retraction events.
- **Rationale:** Epistemic obsolescence (e.g., a 2012 NLP paper being overtaken by Transformers) is subjective, context-dependent, and lacks consensus ground truth without massive manual expert panel review. Formal retractions possess deterministic official publisher notices, verifiable DOI mappings, and clear ground truth.
- **Epistemic Classification:** VERIFIED & JUSTIFIED.

### DEV-002: Dual Reporting of F1 Score (Determinate vs End-to-End)
- **Initial Baseline Implementation:** Earlier baseline implementations computed F1 score only over resolved predictions (dropping abstentions/unknowns).
- **Audited Deviation:** Replaced single F1 metric with dual reporting: $\text{F1}_{\text{determinate}}$ (precision/recall over resolved cases) and $\text{F1}_{\text{end-to-end}}$ (treating any abstention or missing status on a positive ground-truth case as a false negative).
- **Rationale:** If an API or tool abstains on difficult retractions, determinate F1 artificially inflates to 1.0, concealing failure modes. End-to-end F1 penalizes coverage failure and provides a faithful operational benchmark for citation recommendation safety.
- **Epistemic Classification:** VERIFIED & TESTED (Prompt 11 unit test `test_abstention_cannot_inflate_f1_end_to_end`).

### DEV-003: Exclusion of Semicolon Multi-DOI Records
- **Initial Data Loader:** Permitted arbitrary DOI regex matching, which inadvertently matched semicolon-separated multi-DOI strings (e.g. `10.1001/a;10.1001/b`).
- **Audited Deviation:** Explicitly excluded multi-DOI records (17 rows identified in Retraction Watch dataset) from single-paper benchmark sampling.
- **Rationale:** Multi-DOI records represent bundled errata or collective retractions that cannot be queried as a canonical single scholarly identifier.
- **Epistemic Classification:** VERIFIED & TESTED (Prompt 11 unit test `test_multi_doi_not_selected_even_when_regex_matches`).

### DEV-004: Local Execution Environment via Tectonic Compiler
- **Initial Resource Plan:** The student handbook suggested Google Colab or local GPU.
- **Audited Deviation:** Executed experimental pipeline and paper compilation locally on macOS Apple Silicon M2 using Tectonic LaTeX engine, while providing `notebooks/Pilot_Colab.ipynb` for cloud secondary verification.
- **Rationale:** Local execution is completely deterministic, immune to Colab session disconnections, enables instant unit test runs, and compiles LaTeX directly to PDF without external server dependencies.
- **Epistemic Classification:** VERIFIED.
