# Research Decisions Log

## Project Identification
- **Title:** *An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature*
- **Author:** Md Umaid Shaan (MSE2026009)
- **Role:** Autonomous MTech AI Research-Engineering Lead & Scientific Auditor
- **Last Updated:** 2026-11-04
- **Working Repository:** `/Users/umaid/.gemini/antigravity/scratch/citation_retraction_study`

## Epistemic Conventions
- **VERIFIED:** Directly supported by an inspected primary source, official API documentation, or reproducible local execution.
- **INFERRED:** A reasoned architectural choice, methodological design, or hypothesis awaiting empirical validation.
- **UNKNOWN:** Missing, unmeasured, or unresolved evidence.

---

## Logged Research Decisions

### D001 — Establish Literature Review Scope
- **Status:** VERIFIED
- **Decision:** Treat the submitted 12-page review (`inputs/MSE_09_Umaid-1.pdf`) as the authoritative scope document.
- **Reason:** The review explicitly outlines citation recommendation/ranking, citation context and intent, temporal scholarly status, post-retraction citation persistence, and AI-era citation integrity.
- **Source/Evidence:** Review Sections 2–5, pages 1–6.
- **Next Action:** Trace citations to verify original research claims before formulating experimental gap.

### D002 — Distinguish Review Synthesis Claims from Novelty Claims
- **Status:** VERIFIED
- **Decision:** Treat the six candidate gaps in Section 7 as claims proposed by the review, not independently proven field-wide novelty gaps.
- **Reason:** A review's conceptual synthesis does not prove absence of existing commercial or preprint benchmarks.
- **Source/Evidence:** Review Section 7, pages 9–10.
- **Next Action:** Conduct targeted bibliographic searches for existing multi-source citation verification tools.

### D003 — Define Scope of First Implementation
- **Status:** VERIFIED
- **Decision:** Focus the empirical study specifically on explicit formal retraction events rather than subjective epistemic obsolescence.
- **Reason:** Explicit retractions have verifiable public notices, authoritative registries (Retraction Watch, Crossref, OpenAlex), and deterministic evaluation boundaries. Broad epistemic obsolescence lacks objective ground truth without extensive manual domain expert annotation.
- **Source/Evidence:** Review Section 2.3 (page 3) and Section 6.5 (page 9); Student Handbook Phase I.
- **Next Action:** Operationalize retraction detection using Crossref and OpenAlex schemas.

### D004 — Baseline Selection and Comparator Hierarchy
- **Status:** VERIFIED
- **Decision:** Establish two primary baseline comparators:
  1. **B0 (Single-Source Naive):** OpenAlex Works API `is_retracted` boolean field.
  2. **B1 (Single-Source Explicit):** Crossref REST API `update-to` / `relation` with type `retraction`.
  3. **Proposed Method (M_prop):** Provenance-aware Multi-Source Consensus Pipeline with explicit update notice tracking, evidence caching, and conflict explanation.
- **Reason:** Enables controlled comparison isolating the effect of multi-source verification and explicit provenance metadata.
- **Source/Evidence:** OpenAlex Works API schema; Crossref REST API documentation; Handbook Prompt 03 & Prompt 06.
- **Next Action:** Verify baseline implementations on synthetic fixtures before running live evaluation.

### D005 — Handle Provider Abstention and Missing Data
- **Status:** VERIFIED
- **Decision:** When an API fails to return a record, rate-limits, or lacks explicit update metadata, the prediction MUST be classified as `UNKNOWN` rather than `NOT_RETRACTED`.
- **Reason:** Conflating missing metadata with negative evidence creates severe false confidence (silent false negatives), which is dangerous in scientific citation workflows.
- **Source/Evidence:** Review Section 3.4; Handbook Prompt 07 & Prompt 11.
- **Next Action:** Implement separate determinate-only and end-to-end evaluation metrics.

### D006 — Dual F1 Evaluation Metrics (Determinate vs End-to-End)
- **Status:** VERIFIED
- **Decision:** Report two complementary metrics:
  - $\text{F1}_{\text{determinate}}$: Evaluated only over non-abstained predictions ($\hat{y} \in \{\text{RETRACTED}, \text{NOT\_RETRACTED}\}$).
  - $\text{F1}_{\text{end-to-end}}$: Strict metric where `UNKNOWN` on a positive ground-truth instance is penalized as a False Negative (FN).
- **Reason:** Prevents models or providers from gaming high precision by abstaining on all difficult cases.
- **Source/Evidence:** Audited in Prompt 11 debugging case D; `src/metrics.py`.
- **Next Action:** Include both formulas in unit test suite.

### D007 — Dataset Source Selection and Provenance Auditing
- **Status:** VERIFIED
- **Decision:** Ingest official Crossref Retraction Watch dataset directly from Crossref's official GitLab repository (`https://gitlab.com/crossref/retraction-watch-data.git`).
- **Reason:** Authoritative, transparent, reproducible version control with verifiable git commit hashes.
- **Source/Evidence:** Crossref announcement (2023) acquiring Retraction Watch data; GitLab commit `fb5f174f8476824deaf340693f9a819ce5e29ded`.
- **Next Action:** Validate CSV structure and checksums via `scripts/validate_dataset.py`.

### D008 — Exclusion of Multi-DOI Delimited Records
- **Status:** VERIFIED
- **Decision:** Exclude records where `OriginalPaperDOI` contains multiple semicolon-separated DOIs from automated single-paper evaluation pipelines.
- **Reason:** Semicolon-delimited fields break standard 1-to-1 DOI resolution and cause silent lookup failures.
- **Source/Evidence:** Identified in Prompt 11 static code audit; 17 rows identified out of 73,597 in real dataset.
- **Next Action:** Enforce strict single-DOI regex validation in `src/data.py` and `src/validate_rw.py`.

### D009 — Circularity and Shared-Provenance Audit
- **Status:** VERIFIED
- **Decision:** Explicitly acknowledge and measure shared data provenance between OpenAlex and Crossref. OpenAlex utilizes Retraction Watch data, and Crossref distributes Retraction Watch records.
- **Reason:** Neither source represents an independent third-party truth. Evaluating both against Retraction Watch could lead to circular self-validation if not critically disclosed.
- **Source/Evidence:** OpenAlex documentation ("is_retracted field powered by Retraction Watch"); Crossref Retraction Watch agreement.
- **Next Action:** Independently verify sample ground-truth DOIs against publisher landing pages and original notice DOIs.

### D010 — Negative Control Sampling Protocol
- **Status:** VERIFIED
- **Decision:** Construct negative control instances ($\text{Label} = 0$) by sampling verified high-impact, unretracted papers from reputable journals across identical publication years, ensuring absence of retraction/correction notices via multi-source queries.
- **Reason:** Retraction databases only catalog positive cases (retractions/expressions of concern). Evaluating precision requires verified negative controls.
- **Source/Evidence:** Handbook Prompt 04 & 06; scientific auditing requirements.
- **Next Action:** Freeze 40 positive and 40 negative evaluation records with immutable SHA-256 manifest.

### D011 — Pre-Experiment Protocol Freeze
- **Status:** VERIFIED
- **Decision:** Lock random seed (`20261028`), evaluation partitions, decision thresholds, and metric scripts in `configs/protocol_v1.yaml` prior to viewing live experimental outcomes.
- **Reason:** Eliminates post-hoc hypothesis generation, p-hacking, and metric cherry-picking.
- **Source/Evidence:** Handbook Prompt 07 (Gate G2 requirement).
- **Next Action:** Run evaluation script strictly against frozen config.

### D012 — Local Execution over Cloud Reliance
- **Status:** VERIFIED
- **Decision:** Execute entire experimental pipeline, metric computations, and paper compilation locally on Apple Silicon M2 Darwin arm64 rather than relying on ephemeral free Google Colab runtimes.
- **Reason:** Local environment provides deterministic Python 3.14 runtime, persistent file storage, zero timeout risk, and immediate Tectonic LaTeX compilation.
- **Source/Evidence:** Machine telemetry: macOS Darwin 24.6.0, Apple M2, Homebrew, Python 3.14.7.
- **Next Action:** Maintain Colab notebook `notebooks/Pilot_Colab.ipynb` for independent secondary reproduction.

### D013 — Defensible Contribution Pathway
- **Status:** VERIFIED
- **Decision:** Select **Pathway B: Controlled Comparative Study** from Handbook Section 3.
- **Reason:** Pathway B is the most rigorous and tractable approach for evaluating whether multi-source reconciliation genuinely provides statistical and operational improvements over single-source baselines without overclaiming algorithmic novelty.
- **Source/Evidence:** Handbook Section 3, Pathway B definition; Gate G3 specifications.
- **Next Action:** Execute 80-DOI comparative experiment across B0, B1, and M_prop.

### D014 — LaTeX Manuscript Specification & Engine
- **Status:** VERIFIED
- **Decision:** Draft manuscript in standard ACM/IEEE two-column style (`paper/main.tex`), enforce strict 6–10-page length (excluding references), and compile using Tectonic 0.17.0.
- **Reason:** Tectonic is an isolated, reproducible modern TeX engine that avoids heavy TeXLive administration.
- **Source/Evidence:** Handbook Gate G4; Tectonic 0.17.0 installed via Homebrew.
- **Next Action:** Write full manuscript text with authentic tables and high-resolution vector figures.

### D015 — Human-AI Accountability and Authorship Boundaries
- **Status:** VERIFIED
- **Decision:** Antigravity serves as autonomous research-engineering lead, technical pair-programmer, auditor, and LaTeX editor. Final academic submission, viva defense, and intellectual ownership rest exclusively with student author Md Umaid Shaan.
- **Reason:** Academic integrity guidelines and Handbook Phase VI require transparent demarcation of AI assistance and human critical decisions.
- **Source/Evidence:** Handbook Prompt 18; Coursework guidelines.
- **Next Action:** Maintain detailed `ai_assistance_log.md` and `prompt_outputs/18_ai_audit.md`.
