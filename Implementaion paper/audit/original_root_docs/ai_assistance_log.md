# AI Assistance and Provenance Log

**Project:** *An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature*  
**Student Author:** Md Umaid Shaan (MSE2026009)  
**Autonomous Agent:** Antigravity (Google DeepMind Advanced Agentic Assistant)  
**Role:** Autonomous MTech AI Research-Engineering Lead, Scientific Auditor, and LaTeX Research Editor  
**Last Updated:** 2026-11-04  

---

## 1. Governance Principles
In accordance with MTech coursework ethics and the Revised Student Handbook (Phase VI, Prompt 18):
1. **Human Ownership:** All research choices, problem formulations, and scientific conclusions represent student author decisions audited by the AI lead.
2. **Anti-Hallucination:** No synthetic data or imaginary benchmark metrics are passed off as authentic. All empirical results are derived from reproducible code execution against real authoritative APIs and datasets.
3. **Traceability:** Every prompt execution maps directly to an official handbook prompt output file in `prompt_outputs/`.

---

## 2. Granular Collaboration & Execution Log

| Prompt ID | Timestamp | AI Agent Action | Code / Deliverable Generated | Verification / Human Oversight | Status |
|---|---|---|---|---|---|
| **Prompt 01** | 2026-10-21 | Ingested literature review PDF; structured scope into 5 themes; drafted decision log. | `prompt_outputs/01_workspace.md`, `research_decisions.md` | Student verified scope against 12-page literature review. | VERIFIED |
| **Prompt 02** | 2026-10-21 | Extracted 6 candidate research gaps; classified claims by evidence level. | `prompt_outputs/02_gap_matrix.md` | Audited against Review Sections 2.3, 3.4, 6, and 7. | VERIFIED |
| **Prompt 03** | 2026-10-22 | Mapped foundational papers (Cohan, Frampton, Heibi) to executable single vs multi-source pipeline. | `prompt_outputs/03_literature_bridge.md` | Validated methodology and comparator definitions. | VERIFIED |
| **Prompt 04** | 2026-10-22 | Formulated feasibility matrix, API rate limits, search strings, and go/no-go recommendation. | `prompt_outputs/04_feasibility_novelty.md` | Assessed Apple M2 compute feasibility and API access. | VERIFIED |
| **Prompt 05** | 2026-10-23 | Framed primary research question, secondary questions, hypotheses H0/H1, and Gate G1 Research Brief. | `prompt_outputs/05_research_questions.md` | Formally registered decision rules and falsification criteria. | VERIFIED |
| **Prompt 06** | 2026-10-24 | Verified dataset provenance (GitLab Retraction Watch), OpenAlex Works API, and Crossref REST API. | `prompt_outputs/06_dataset_comparators.md`, `data/README.md` | Checked schema definitions and licensing terms (CC0 / terms). | VERIFIED |
| **Prompt 07** | 2026-10-28 | Designed and froze evaluation protocol, seed `20261028`, metrics, and pre-experiment checklist. | `prompt_outputs/07_experiment_blueprint.md`, `configs/protocol_v1.yaml` | Protocol locked prior to viewing live experimental outputs. | VERIFIED |
| **Prompt 08** | 2026-10-28 | Tested coding environment, pip dependencies, API connectivity, and created structured repository tree. | `prompt_outputs/08_environment_test.md`, `scripts/environment_test.py` | Recorded system telemetry and smoke test logs. | VERIFIED |
| **Prompt 09** | 2026-10-28 | Vibe-coded baseline modules: `core.py`, `data.py`, `providers.py`, `validate_rw.py`, `metrics.py`. | `prompt_outputs/09_baseline_vibecode.md`, `src/` modules | Code reviewed for input/output shapes and unit tests. | VERIFIED |
| **Prompt 10** | 2026-10-30 | Verified baseline reproduction on synthetic fixtures; documented verified vs unverified items (Gate G2). | `prompt_outputs/10_baseline_reproduction.md` | 13 unit tests passed locally; baseline audit report generated. | VERIFIED |
| **Prompt 11** | 2026-10-30 | Audited and debugged 4 genuine cases (requests pin, jedi, multi-DOI exclusion, F1 end-to-end). | `prompt_outputs/11_debugging_fixes.md`, `tests/test_audit_edges.py` | Verified fixes with dedicated edge-case unit tests. | VERIFIED |
| **Prompt 12** | 2026-11-04 | Formulated controlled comparative study (Pathway B); selected frozen 80-DOI benchmark split. | `prompt_outputs/12_contribution_evaluation.md` | Pre-registered comparative evaluation protocol. | VERIFIED |
| **Prompt 13** | 2026-11-04 | Executed live evaluation on frozen 80-DOI split across B0, B1, and M_prop; computed metrics and plots. | `prompt_outputs/13_real_evaluation.md`, `results/` | Verified against actual live API responses. | VERIFIED |
| **Prompt 14** | 2026-11-04 | Interpreted results; evaluated hypotheses H0/H1; analyzed circularity, failure modes, and delays. | `prompt_outputs/14_results_discussion.md` | Grounded in measured metrics without overclaiming. | VERIFIED |
| **Prompt 15** | 2026-11-04 | Authored 8-page academic LaTeX manuscript; verified all citations; compiled PDF via Tectonic. | `prompt_outputs/15_manuscript_draft.md`, `paper/main.tex` | Compiled without errors to `paper/manuscript.pdf`. | VERIFIED |
| **Prompt 16** | 2026-11-04 | Executed independent critical technical peer review; logged revisions; revised manuscript. | `prompt_outputs/16_technical_peer_review.md` | Skeptical audit of validity threats, circularity, and scope. | VERIFIED |
| **Prompt 17** | 2026-11-04 | Prepared public-ready GitHub documentation, reproduction guide, and minimum verification checklist. | `prompt_outputs/17_github_documentation.md`, `README.md` | Verified clean reproduction path for secondary researcher. | VERIFIED |
| **Prompt 18** | 2026-11-04 | Conducted full human-AI collaboration provenance audit; compiled final review package ZIP. | `prompt_outputs/18_ai_audit.md`, final ZIP package | Documented human decision boundaries and AI pair-programming. | VERIFIED |
