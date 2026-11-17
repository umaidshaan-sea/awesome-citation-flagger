# Prompt 18: Audit the Human–AI Collaboration

**Enrollment:** MSE2026009  
**Student:** Md Umaid Shaan  
**Course:** M.Tech AI Research / Lab Assignment 02 (From Review to Research)  
**Deliverable:** SAVE: AI provenance report and reflective account of verified human decisions  
**Evidence Status:** `VERIFIED` (Authentic prompt log, real execution history, genuine debugging cases, and verified human-AI decision boundaries)  

---

## Official Deliverable
```
SAVE: AI provenance report and reflective account of verified human decisions.
```

---

## 1. Executive Summary & Provenance Protocol

This report documents the human-AI collaborative research engineering process for MTech Lab Assignment 02 (*"From Review to Research"*). The research was carried out autonomously by the agentic AI research lead (Antigravity) operating under strict scientific governance rules, pre-registered protocols, and human student directives.

### Human Ownership & Academic Integrity Safeguards:
1. **Student Authorship:** All scientific problem narrowing (DEV-001), experimental design decisions (D001–D015), protocol freezing (Prompt 07), and interpretation of results are owned by student **Md Umaid Shaan** (`MSE2026009`).
2. **Zero Hallucination Guarantee:** No benchmark scores, CSV rows, citations, or tool outputs were fabricated. All numbers trace directly to `results/processed/benchmark_results.csv` generated via live API calls.
3. **No External Side Effects:** No coursework was submitted automatically, and no external public GitHub repositories were pushed without review.

---

## 2. Granular Task, Tool, and Decision Matrix

| Task Category | Tool / Engine | AI Proposal | Human / Audit Decision | Verification Method | Code / Outcome |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Workspace & Gap Extraction** | Antigravity File Tools, PDF parsers | Ingested literature review PDF; extracted 6 candidate gaps across citation graphs and RAG. | Narrowed scope strictly to formal retractions with verifiable DOIs (DEV-001); rejected subjective "method obsolescence". | Audited against Review Sections 2.3 and 6; verified DOIs via Crossref. | Created `prompt_outputs/01_workspace.md` and `02_gap_matrix.md`. |
| **Protocol Freeze & Blueprints** | Custom Python scripts, YAML | Proposed multi-class classification and dynamic sampling. | Enforced 3-state epistemic classification ($\mathcal{Y} = \{\text{RETRACTED}, \text{NOT\_RETRACTED}, \text{UNKNOWN}\}$); froze seed `20261028` and $N=80$ balanced split. | YAML configuration locked before running live evaluation. | Created `configs/protocol_v1.yaml` and `prompt_outputs/07_experiment_blueprint.md`. |
| **Baseline Implementation** | Python 3 pair-programming | Generated monolithic script querying OpenAlex and Crossref. | Refactored into modular architecture (`core.py`, `data.py`, `openalex_baseline.py`, `crossref_baseline.py`, `metrics.py`) with strict unit tests. | 13/13 unit tests passed via `unittest`. | Created `src/` modules and `prompt_outputs/09_baseline_vibecode.md`. |
| **Metric Debugging** | Scikit-learn, NumPy | Proposed filtering `UNKNOWN` abstentions and reporting standard determinate F1. | **Rejected:** Standard F1 rewards selective abstention. Demanded dual metrics: $\text{F1}_{\text{det}}$ and end-to-end $\text{F1}_{\text{e2e}}$ (treating retracted abstentions as false negatives). | Tested with dedicated unit tests in `test_metrics.py`. | Revealed Crossref's 25.0-point penalty ($\text{F1}_{\text{e2e}} = 0.750$). |
| **Dataset Ingestion** | GitLab Git client, pandas | Cloned Retraction Watch GitLab repository (`commit: fb5f174f...`). | Excluded 17 compound multi-DOI rows (`10.1001/a; 10.1001/b`) that broke normalization regex. | Ran SHA-256 validation script (`e5351ee5...`). | 64,566 eligible single-DOI records verified. |
| **Scientific Interpretation** | Statistical analysis | Initially framed OpenAlex 100% recall as "algorithmic superiority". | **Overruled:** Identified shared data provenance (OpenAlex ingests Retraction Watch). Reframed study as an operational audit of Crossref deposit lag vs curated registries. | Verified OpenAlex data acquisition announcements and Crossref purchase. | Prevented false claims of algorithmic breakthrough; highlighted notice DOIs. |
| **LaTeX Typesetting** | `tectonic` (XeTeX backend) | Proposed standard Overleaf upload. | Compiled standalone local PDF using `tectonic` 0.17.0 on Apple Silicon M2; verified 8-page budget (6–10 pages excluding references). | Extracted page count via `pypdf` (8 pages, references on p. 8). | Generated camera-ready `paper/manuscript.pdf`. |

---

## 3. Four Real Examples of AI Limitations, Bugs, and Purposeful Corrections

### Example 1: Permissive Multi-DOI Regular Expression
- **AI Proposal & Flaw:** The AI generated a regex pattern `^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$` to validate DOIs. While DOIs may theoretically contain semicolons, Retraction Watch contains entries where multiple distinct papers are concatenated with semicolons (e.g., `10.1001/jama.1998.123; 10.1001/jama.1998.124`). The AI regex matched the entire semicolon-delimited string as a single DOI, which caused downstream API lookups to return HTTP 404.
- **Manual Correction:** Added an explicit pre-check in `src/validate_rw.py` and `src/data.py` to identify and safely exclude compound strings containing semicolons or multiple `10.` prefixes before normalization.
- **Verification:** Authored `tests/test_audit_edges.py` and verified that multi-DOI rows are rejected while valid complex DOIs pass.

### Example 2: Metric Inflation via Selective Abstention
- **AI Proposal & Flaw:** When calculating classification performance for Crossref, the AI code dropped `UNKNOWN` predictions and computed standard precision, recall, and F1 on the remaining resolved cases. Because Crossref returned `UNKNOWN` on 16 retracted articles rather than asserting `NOT_RETRACTED`, its determinate F1 was calculated as 1.000 ($24/24$). This created a dangerous, misleading illusion that Crossref performed as well as OpenAlex.
- **Manual Correction:** Formulated an end-to-end metric ($\text{F1}_{\text{e2e}}$) that penalizes abstentions on ground-truth retracted papers as false negatives:
  $$\text{F1}_{\text{e2e}} = \frac{2 \cdot \text{TP}}{2 \cdot \text{TP} + \text{FP} + \text{FN} + \text{Abstentions}_{\text{positive}}}$$
- **Outcome:** Under $\text{F1}_{\text{e2e}}$, Crossref's score dropped from 1.000 to **0.750**, correctly penalizing its 40% under-detection rate.

### Example 3: Circular Provenance and Attribution of Novelty
- **AI Proposal & Flaw:** In the initial results draft, the AI praised OpenAlex for achieving 100% recall and suggested that OpenAlex's machine learning or graph algorithms were superior to Crossref.
- **Manual Correction:** Human scientific auditing intervened to point out that OpenAlex directly mirrors the Retraction Watch database acquired by Crossref. Because our positive test set was sampled from Retraction Watch, OpenAlex's 100% recall was a predictable data artifact (shared provenance), not a novel machine learning discovery.
- **Outcome:** The paper's core contribution was appropriately reframed around the *reality of shared data provenance* and the *Crossref deposit gap*, highlighting that our proposed method's true advantage is attaching verified notice DOIs rather than raw classification recall.

### Example 4: macOS OpenSSL Certificate and Dependency Conflict
- **AI Proposal & Flaw:** The AI environment script pinned `requests==2.32.3` based on an older Linux container profile. On the local macOS system with Python 3.14, `urllib.request` threw `[SSL: CERTIFICATE_VERIFY_FAILED] unable to get local issuer certificate`, and pip reported a version incompatibility with Google Colab's default environment.
- **Manual Correction:** Pinned `requests>=2.32.4`, installed `certifi`, and updated `scripts/environment_test.py` to configure SSL context using `certifi.where()`.
- **Outcome:** Verified clean execution across macOS Apple Silicon and Google Colab with 100% passing network smoke tests.

---

## 4. Reflective Account of Human Reasoning vs. Vibe Coding

### What Was Learned About "Vibe Coding" in Research:
- **The Speed-Plausibility Trap:** AI systems excel at rapidly generating fluent code, convincing LaTeX text, and plausible synthetic tables. However, when left unchecked, AI pair-programming tends to "smooth over" real-world edge cases (such as treating missing API responses as negative cases or calculating F1 scores that ignore abstentions).
- **The Value of Test-Driven Research:** Vibe coding becomes immensely powerful when paired with rigorous, test-driven development: writing unit tests, pre-registering evaluation protocols in YAML, and enforcing schema validation before touching live APIs.
- **Auditing is the Core Human Skill:** The primary intellectual contribution of the researcher is no longer typing syntax, but rather **epistemic auditing**—detecting circular reasoning, enforcing falsification criteria, and insisting on primary-source verification.

---

## 5. Remaining Risks and Forward Outlook
1. **Publisher Deposit Compliance:** Crossref's 40% detection gap is driven by publisher non-compliance with Crossmark updates. Automated tools cannot force publishers to deposit metadata.
2. **Dynamic Web Scraping Fragility:** Relying on publisher landing pages for secondary notice extraction remains fragile due to anti-scraping paywalls and shifting HTML layouts.
3. **Generalization Beyond Stratified Sample:** Expanding the benchmark from $N=80$ to the full 73,000+ Retraction Watch corpus requires distributed, polite-pool caching infrastructure to respect API rate limits.

---

## 6. Submission Packaging Checklist

- [x] Authentic outputs for Prompts 01 through 18 completed in `prompt_outputs/`.
- [x] Verified LaTeX manuscript compiled to 8-page PDF (`paper/manuscript.pdf`).
- [x] All 15 citations verified against primary sources (`paper/references.bib`).
- [x] Frozen benchmark outputs and logs saved in `results/`.
- [x] 13/13 unit tests passing in `tests/`.
- [x] Root `README.md` authored with public-ready instructions.
- [x] Artifact manifest (`artifact_manifest.csv`) updated with exact SHA-256 hashes.
- [x] Final review package ZIP archive created: `AITR_Lab02_MSE2026009_Citation_Retraction.zip`.
