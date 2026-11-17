# PLAN.md — Autonomous Research Execution Plan

**Project:** *An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature*  
**Student:** Md Umaid Shaan (MSE2026009)  
**Lead Auditor & Engineer:** Autonomous MTech AI Research-Engineering Lead  
**Last Updated:** 2026-11-04  

---

## 1. Executive Roadmap & Gate Alignment

| Phase | Official Prompts | Handbook Gate | Core Deliverables | Target Status |
|---|---|---|---|---|
| **Phase I: Gap to Research Question** | Prompts 01–05 | **Gate G1: Research Brief** | Decision log, gap matrix, lit-to-exp bridge, novelty/feasibility matrix, 1-page research brief | Completed & Audited |
| **Phase II: Baseline Setup & Protocol Freeze** | Prompts 06–08 | **Gate G2 Prep** | Dataset validation, frozen protocol, environment smoke test & structured repo | Completed & Audited |
| **Phase III: Baseline Reproduction & Debugging** | Prompts 09–11 | **Gate G2 Checkpoint** | Vibe-coded baseline modules, baseline reproduction report, audited debugging decision log | Completed & Audited |
| **Phase IV: Comparative Experiment & Real Evidence** | Prompts 12–14 | **Gate G3: Experimental Evidence** | Comparative evaluation (Single vs Dual vs Consensus), real metrics CSV, publication figures, outcome analysis | Active Execution |
| **Phase V: LaTeX Manuscript & Technical Review** | Prompts 15–17 | **Gate G4: Paper & Reproducibility** | 6–10-page LaTeX implementation paper (excl. refs), compiled PDF, technical peer review, GitHub README | Queued |
| **Phase VI: Human-AI Accountability & Packaging** | Prompt 18 | **Gate G4 Final** | AI collaboration audit, prompt logs, final review ZIP archive | Queued |

---

## 2. Granular Step-by-Step Prompt Execution Plan

### [Phase I] From Review to Research Question (Gate G1)
- [x] **Prompt 01 | Setup an Accountable Research Workspace**
  - *Input:* Literature review PDF `MSE_09_Umaid-1.pdf`, student transcript `ATR_MSE2026009.pdf`.
  - *Action:* Import prior Prompt 01 output, initialize structured logs (`AGENTS.md`, `PLAN.md`, `STATUS.md`, `research_decisions.md`, `source_ledger.csv`, `evidence_ledger.csv`, `artifact_manifest.csv`).
  - *SAVE Deliverable:* `prompt_outputs/01_workspace.md` (Workspace & decision log; review scope summary).
- [x] **Prompt 02 | Extract Evidence-Based Research Gaps**
  - *Input:* Literature review Section 2.3, 3.4, 6, 7.
  - *Action:* Import and audit 6 candidate gaps; verify citations vs. review claims; classify epistemic boundaries (VERIFIED vs INFERRED vs UNKNOWN).
  - *SAVE Deliverable:* `prompt_outputs/02_gap_matrix.md` (Evidence-based gap matrix).
- [x] **Prompt 03 | Map the Literature to an Executable Experiment**
  - *Input:* Gap G1 (provenance-aware multi-source retraction checking) and primary studies (Cohan et al. 2019, Frampton et al. 2021, Heibi & Peroni 2021).
  - *Action:* Bridge foundational studies to candidate engineering design; identify single-source baseline vs multi-source proposed pipeline.
  - *SAVE Deliverable:* `prompt_outputs/03_literature_bridge.md` (Mandatory literature-to-experiment bridge).
- [x] **Prompt 04 | Check Feasibility, Novelty and Resource Access**
  - *Input:* Apple Silicon M2 hardware, GitLab Retraction Watch dataset, Crossref & OpenAlex REST APIs.
  - *Action:* Search strings, API rate limits, computational feasibility, go/no-go recommendation with fallback paths.
  - *SAVE Deliverable:* `prompt_outputs/04_feasibility_novelty.md` (Novelty/feasibility matrix & go/no-go decision).
- [x] **Prompt 05 | Frame Research Questions and Success Criteria (Gate G1 Checkpoint)**
  - *Input:* Audited gap and feasibility matrix.
  - *Action:* Frame 1 primary RQ, 2 secondary RQs, formal hypotheses (H0/H1), independent/dependent variables, decision rules, falsification criteria.
  - *SAVE Deliverable:* `prompt_outputs/05_research_questions.md` (Gate G1 One-Page Research Brief).

---

### [Phase II] Protocol Freeze & Baseline Environment
- [x] **Prompt 06 | Verify Datasets and Comparators**
  - *Input:* Crossref Retraction Watch GitLab repository, OpenAlex API docs, Crossref REST API docs.
  - *Action:* Validate dataset schemas, row counts, unique DOIs, licensing (CC0 / terms), comparator definitions (B0: OpenAlex Boolean, B1: Crossref typed update relation).
  - *SAVE Deliverable:* `prompt_outputs/06_dataset_comparators.md` (Dataset & baseline validation sheet).
- [x] **Prompt 07 | Freeze an Experiment Blueprint Before Viewing Results**
  - *Input:* Planned evaluation metrics, seed 20261028, sampling rules.
  - *Action:* Create frozen YAML configuration (`configs/protocol_v1.yaml`), define leakage barriers, specify primary metrics (Precision, Recall, F1_determinate, F1_end_to_end, Abstention Rate, Disagreement Rate).
  - *SAVE Deliverable:* `prompt_outputs/07_experiment_blueprint.md` (Frozen evaluation protocol & pre-experiment checklist).
- [x] **Prompt 08 | Configure and Test the Coding Environment**
  - *Input:* macOS M2 Darwin arm64, Python 3.14.7, dependencies (`requirements.txt`).
  - *Action:* Run smoke tests, verify network connectivity to APIs and GitLab, verify local unit tests, record system telemetry.
  - *SAVE Deliverable:* `prompt_outputs/08_environment_test.md` (Environment verification log & structured repository tree).

---

### [Phase III] Baseline Implementation & Verified Debugging (Gate G2)
- [x] **Prompt 09 | Vibe-Code One Baseline Module at a Time**
  - *Input:* Reference specifications for DOI normalization, provider querying, caching, rule decision logic.
  - *Action:* Code audit of `src/validate_rw.py`, `src/data.py`, `src/core.py`, `src/providers.py`, `src/metrics.py`.
  - *SAVE Deliverable:* `prompt_outputs/09_baseline_vibecode.md` (Working baseline + code understanding + prompt-to-code log).
- [x] **Prompt 10 | Verify and Reproduce the Baseline (Gate G2 Checkpoint)**
  - *Input:* Unit tests and pilot candidate generation.
  - *Action:* Verify execution on synthetic fixture (13 unit tests PASS); document what is verified and what remains unverified prior to live evaluation.
  - *SAVE Deliverable:* `prompt_outputs/10_baseline_reproduction.md` (Baseline reproduction/validation report).
- [x] **Prompt 11 | Debug Using Actual Evidence**
  - *Input:* Colab traceback logs and static code audit defects.
  - *Action:* Formally document 4 genuine debugging cases: requests pin conflict, missing jedi, semicolon multi-DOI parsing flaw, and metric denominator/abstention distortion.
  - *SAVE Deliverable:* `prompt_outputs/11_debugging_fixes.md` (Corrected code, tested fixes & debugging decision log).

---

### [Phase IV] Controlled Comparative Evaluation (Gate G3)
- [ ] **Prompt 12 | Choose and Evaluate a Defensible Contribution**
  - *Input:* Validated baseline B0 (OpenAlex `is_retracted`), B1 (Crossref `updated-by`), proposed multi-source provenance-aware pipeline M_prop.
  - *Action:* Define Pathway B (Controlled Comparative Study); establish frozen benchmark evaluation split: 80 DOIs (40 positive retraction cases spanning multiple years/publishers + 40 negative control cases with verified unretracted literature from top venues).
  - *SAVE Deliverable:* `prompt_outputs/12_contribution_evaluation.md` (Chosen contribution pathway & executable comparison plan).
- [ ] **Prompt 13 | Evaluate Using Real Outputs Only (Gate G3 Checkpoint)**
  - *Input:* Live API outputs from Crossref and OpenAlex on the frozen 80-DOI benchmark.
  - *Action:* Execute evaluation, verify labels independently against publisher retraction notices / Crossref metadata, compute metrics (Precision, Recall, F1_det, F1_e2e, Coverage, Disagreement, Latency), generate publication figures and CSV.
  - *SAVE Deliverable:* `prompt_outputs/13_real_evaluation.md` (Evaluation script, results CSV, tables & publication figures).
- [ ] **Prompt 14 | Interpret Outcomes, Including Negative Results**
  - *Input:* Empirical metric tables, failure logs, edge cases.
  - *Action:* Critical scientific audit: answer RQ1, RQ2, RQ3; test hypotheses H0/H1; analyze shared data provenance between Retraction Watch and OpenAlex/Crossref; examine false negatives, abstentions, and publisher notice delays.
  - *SAVE Deliverable:* `prompt_outputs/14_results_discussion.md` (Evidence-based Results & Discussion outline with limitations).

---

### [Phase V] LaTeX Manuscript & Rigorous Review (Gate G4)
- [ ] **Prompt 15 | Draft an Evidence-Grounded Manuscript in LaTeX**
  - *Input:* Verified problem brief, audited results, high-resolution figures, verified BibTeX (`paper/references.bib`).
  - *Action:* Write complete 6–10-page academic manuscript (`paper/main.tex`) in standard IEEE/ACM format, compile via Tectonic to `paper/manuscript.pdf`.
  - *SAVE Deliverable:* `prompt_outputs/15_manuscript_draft.md` (Target manuscript text, figures, .tex, and verified .bib).
- [ ] **Prompt 16 | Conduct a Demanding Technical Peer Review**
  - *Input:* Compiled paper PDF, code repository, results tables.
  - *Action:* Act as a rigorous, skeptical external peer reviewer (ACM/IEEE standards); evaluate threats to validity, circularity, leakage, overclaiming; record revision diff.
  - *SAVE Deliverable:* `prompt_outputs/16_technical_peer_review.md` (Peer-review report & manuscript revision log).
- [ ] **Prompt 17 | Prepare Reproducible GitHub Documentation**
  - *Input:* Clean repository, frozen configs, verification scripts, instructions.
  - *Action:* Generate root `README.md`, reproduction guide, minimum checklist for second researcher, license, compute specifications.
  - *SAVE Deliverable:* `prompt_outputs/17_github_documentation.md` (Public-ready research repo & reproduction instructions).

---

### [Phase VI] Accountability & Packaging
- [ ] **Prompt 18 | Audit the Human–AI Collaboration**
  - *Input:* Prompt logs, tool telemetry, diff histories, human oversight records.
  - *Action:* Comprehensive provenance report detailing AI contributions vs. student author decisions, failure modes, epistemic validations.
  - *SAVE Deliverable:* `prompt_outputs/18_ai_audit.md` (AI provenance report & reflective account of verified decisions).
- [ ] **Final Packaging & Review Preparation**
  - *Action:* Create final self-contained ZIP archive `AITR_Lab02_MSE2026009_Citation_Retraction.zip` and present paper PDF for student review.
