# Antigravity MTech AI Research: 10 Core Execution Prompts & Official Handbook Protocol

This document contains the authoritative text of the research prompts adapted for autonomous execution in Google Antigravity, corresponding directly to the MTech AI Tools for Research (ATR) Revised Student Handbook.

---

## PROMPT 01 | Setup an Accountable Research Workspace
**Prompt Text:**
> I am a postgraduate student converting my completed literature review into an implementation-based research paper. My topic is *An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature*. Act as a critical research mentor and technical pair programmer. Guide me in stages: evidence-based gap identification, literature-to-experiment mapping, feasibility, research questions, verified baseline, coding, experimental evaluation, manuscript and reproducibility. Mark statements as VERIFIED, INFERRED or UNKNOWN, and explicitly request source files or outputs when evidence is missing. Never invent papers, datasets, repository links, code execution outputs, test metrics or human actions. Begin by summarizing the scope of the attached review and proposing a structured research workspace.

**SAVE:** Workspace and decision log; review scope. (`prompt_outputs/01_workspace.md`)

---

## PROMPT 02 | Extract Evidence-Based Research Gaps
**Prompt Text:**
> Analyze my attached literature review *An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature*. Identify central methods, datasets, measured findings, author-reported limitations and candidategaps. For each gap record: (1) evidence location in the review, (2) whether it is reported by the review's cited authors or inferred by the reviewer, (3) a testable research question, (4) candidate experiment, (5) required datasets/compute/metrics, and (6) primary risks or failure modes. Label any gap requiring unverified resources as UNKNOWN. Do not invent papers or results.

**SAVE:** Gap matrix: source evidence → candidate question → possible experiment. (`prompt_outputs/02_gap_matrix.md`)

---

## PROMPT 03 | Map the Literature to an Executable Experiment
**Prompt Text:**
> My literature review *An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature* identified these candidate gaps: provenance-aware reconciliation of retraction-status sources; context-aware persistence analysis; multimodal retraction detection; temporal propagation lag quantification. Identify three published methods from the review that can be adapted to an executable experiment on MacBook Pro M2. For each, extract: original method, paper title, authors, year, DOI, original task and dataset, original evaluation protocol, reported limitations, and computational requirements. Then select ONE method, explain why it is tractable, specify the executable baseline, and propose a controlled experimental comparison between the baseline and an extension or modification. Draw a clear text diagram: Original published research → Selected verification method → Executable Python baseline → Controlled experimental comparison → Measured results → Research paper.

**SAVE:** Mandatory bridge: original papers → selected method → executable baseline → planned test. (`prompt_outputs/03_literature_bridge.md`)

---

## PROMPT 04 | Check Feasibility, Novelty and Resource Access
**Prompt Text:**
> My candidate study is a Controlled Comparison of Single-Source vs. Multi-Source Retraction-Status Verification for AI-Recommended Citations. Develop a feasibility and novelty-verification plan. Provide scholarly search strings to verify whether this specific experiment has already been published. Search Google Scholar, Semantic Scholar, Crossref and OpenAlex. Define criteria to confirm or refute novelty: what finding would make this idea non-novel? Next, assess resource feasibility: dataset access, terms of use, licensing, model weights/APIs, compute requirements, software dependencies, and estimated time. Produce a novelty/feasibility matrix. Rate the idea as HIGH, CONDITIONAL or NO-GO with explicit justification. Recommend a fallback if preferred resources are unavailable.

**SAVE:** Novelty/feasibility matrix and go/no-go decision. (`prompt_outputs/04_feasibility_novelty.md`)

---

## PROMPT 05 | Frame Research Questions and Success Criteria
**Prompt Text:**
> Here is my verified gap: inconsistency and lack of provenance reconciliation in scholarly retraction metadata across discovery platforms; selected study: Controlled comparison of OpenAlex `is_retracted` vs Crossref explicit update relations vs Multi-source consensus pipeline; source evidence: Cohan et al. (2019), Frampton et al. (2021), Heibi & Peroni (2021), Crossref Retraction Watch data. Write one precise research problem, two or three testable research questions, and hypotheses only where appropriate. For each question identify: input data, comparator, independent/dependent variables, evaluation metric, meaningful success threshold or decision rule, and an observation that would contradict my expectation. Separate the contribution I intend to evaluate from secondary features. Compile into a one-page research brief (Gate G1).

**SAVE:** One-page problem brief with questions and measurable outcomes. (`prompt_outputs/05_research_questions.md`)

---

## PROMPT 06 | Verify Datasets and Comparators
**Prompt Text:**
> My question is *Does combining Crossref and OpenAlex retraction-status information improve detection performance and explainability compared with using single-source baselines?* in scholarly citation verification. Recommend a primary dataset and two meaningful baseline methods or comparable published results. For each dataset: official source URL, exact version/date/commit, persistent identifier (DOI/URI), sample size, feature fields, train/dev/test partitions, licensing/terms of use, known biases or artifacts, leakage risks, and how to verify file integrity (SHA-256). For each baseline: reference paper, public code/API availability, license, exact inputs/outputs, reproduction risks. Flag any shared underlying data sources between datasets and baselines to avoid circular evaluation.

**SAVE:** Dataset and baseline validation sheet. (`prompt_outputs/06_dataset_comparators.md`)

---

## PROMPT 07 | Freeze an Experiment Blueprint Before Viewing Results
**Prompt Text:**
> Design a reproducible protocol for comparing B0 (OpenAlex `is_retracted`) and B1 (Crossref typed `retraction`) with proposed multi-source pipeline on the Crossref Retraction Watch dataset. Include: fixed random seed, data splits with leakage barriers, preprocessing, exact hyperparameter/decision settings, primary evaluation metric, secondary/safety metrics, statistical test with null hypothesis, and a flowchart tracing input data through preprocessing, baseline, proposed method, evaluation, to tabular and graphical outputs. Add a pre-experiment checklist of five conditions that must be true before running code. Once finalized, freeze the protocol and declare that no hyperparameters or metric definitions will change after viewing results.

**SAVE:** Frozen evaluation protocol, flowchart and pre-experiment checklist. (`prompt_outputs/07_experiment_blueprint.md`)

---

## PROMPT 08 | Configure and Test the Coding Environment
**Prompt Text:**
> Act as my research software engineer. Set up local Apple Silicon MacBook Pro M2 environment for retraction citation verification using Python 3.14. Produce: (1) `requirements.txt` with pinned dependency versions, (2) verified installation command sequence, (3) hardware/OS verification script, (4) directory structure adhering to standard project layout, (5) smoke test script importing dependencies, asserting versions, checking GPU/CPU access, testing deterministic random seeding, running toy forward pass, and logging results to JSON. If any package conflicts arise, resolve them using minimal compatible changes.

**SAVE:** Environment verification log and structured project repository. (`prompt_outputs/08_environment_test.md`)

---

## PROMPT 09 | Vibe-Code One Baseline Module at a Time
**Prompt Text:**
> You are my AI pair programmer. I am reproducing single-source OpenAlex and Crossref retraction baselines on Retraction Watch data to produce retraction flags with evidence links. Work in short cycles: (1) specify the module and assumptions, (2) generate minimal executable code, (3) explain logic and input/output shapes, (4) supply a unit/sanity test, and (5) wait for execution output before continuing. Implement data loading/validation (`src/validate_rw.py`), candidate sampling (`src/data.py`), provider query and caching (`src/providers.py`), classification rules (`src/core.py`), evaluation metrics (`src/metrics.py`), and runner scripts (`scripts/pilot.py`). Prefer official APIs and keep every module testable in isolation.

**SAVE:** Working baseline plus code understanding and prompt-to-code log. (`prompt_outputs/09_baseline_vibecode.md`)

---

## PROMPT 10 | Verify and Reproduce the Baseline
**Prompt Text:**
> I have implemented OpenAlex and Crossref baseline modules based on official API schemas and Retraction Watch dataset. Here are the code, unit tests, configurations, and environment details. Verify baseline implementation against published literature and API documentation. Check: data leakage between candidate selection and evaluation, metric calculation matches standard formulas, abstention handling prevents false negatives, edge cases in DOI normalization and semicolon-separated strings. Run baseline on verification split, record outputs, compare with expectations, and document discrepancies. Classify findings into: VERIFIED (empirically confirmed), UNCERTAIN (requires live API data), and NEEDS CORRECTION.

**SAVE:** Baseline reproduction/validation report, including discrepancies. (`prompt_outputs/10_baseline_reproduction.md`)

---

## Prompts 11–18 (Phases IV, V, VI)
- **Prompt 11 | Debug Using Actual Evidence:** Document 4 genuine debugging cases with minimal fixes, tests, and decision rationale. (`prompt_outputs/11_debugging_fixes.md`)
- **Prompt 12 | Choose and Evaluate a Defensible Contribution:** Formalize Pathway B (Controlled Comparative Study) with 80-DOI benchmark split. (`prompt_outputs/12_contribution_evaluation.md`)
- **Prompt 13 | Evaluate Using Real Outputs Only:** Execute live comparative experiment across B0, B1, and M_prop; export traceable CSV, metrics tables, and publication figures. (`prompt_outputs/13_real_evaluation.md`)
- **Prompt 14 | Interpret Outcomes, Including Negative Results:** Evidence-based results analysis, hypotheses evaluation, failure modes, data circularity audit, and limitations. (`prompt_outputs/14_results_discussion.md`)
- **Prompt 15 | Draft an Evidence-Grounded Manuscript in LaTeX:** Complete 6–10-page LaTeX paper (`paper/main.tex`), verified bibliography (`paper/references.bib`), compiled via Tectonic to PDF. (`prompt_outputs/15_manuscript_draft.md`)
- **Prompt 16 | Conduct a Demanding Technical Peer Review:** Skeptical external peer review, constructive feedback, manuscript revisions. (`prompt_outputs/16_technical_peer_review.md`)
- **Prompt 17 | Prepare Reproducible GitHub Documentation:** Root `README.md`, reproduction guide, minimum reproduction checklist for peer researcher. (`prompt_outputs/17_github_documentation.md`)
- **Prompt 18 | Audit the Human–AI Collaboration:** Provenance log, human decision boundaries, tool reflections, final review ZIP archive. (`prompt_outputs/18_ai_audit.md`)
