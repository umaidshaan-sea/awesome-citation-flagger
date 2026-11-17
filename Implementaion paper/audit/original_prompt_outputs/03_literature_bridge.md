# Prompt 03 Output: Literature-to-Experiment Mandatory Bridge

> **Provenance Notice:** Imported and expanded from student submission `ATR_Prompt_3_4_MSE2026009.pdf` (pages 1–8). Audited and structured as the mandatory method bridge between foundational literature and executable code.

---

## 1. Official Handbook Prompt Specification
- **Prompt:** Map the literature to an executable experiment
- **Official SAVE Deliverable:** Mandatory bridge: original papers → selected method → executable baseline → planned test.
- **Evidence Status:** VERIFIED (grounded in audited primary citations).
- **Substantive Artifact Links:**
  - Prior Work Transcript: [ATR_Prompt_3_4_MSE2026009.pdf](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/inputs/ATR_Prompt_3_4_MSE2026009.pdf)
  - Primary Source Ledger: [source_ledger.csv](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/source_ledger.csv)
  - Core Logic Implementation: [core.py](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/src/core.py)

---

## 2. Foundational Published Research Studies

### Paper 1: Cohan et al. (2019)
- **Title:** Structural Scaffolds for Citation Intent Classification in Scientific Publications
- **Authors:** Arman Cohan, Waleed Ammar, Madeleine van Zuylen, Mostafa Dehghani, Hannaneh Hajishirzi
- **Year & Venue:** 2019, NAACL-HLT (pp. 3586–3596)
- **DOI:** [10.18653/v1/N19-1361](https://doi.org/10.18653/v1/N19-1361)
- **Original Task & Method:** Multitask neural sequence model (SciCite) classifying citation intent into Method, Background, or Result Comparison using structural document scaffolds.
- **Dataset:** SciCite benchmark dataset (~11,000 citation contexts).
- **Reported Limitations:** Does not verify scholarly status or determine whether the cited paper was retracted, corrected, or invalidated.
- **Computational Requirement:** GPU required for full transformer fine-tuning; lightweight inference.

### Paper 2: Frampton et al. (2021)
- **Title:** Inconsistent and incomplete availability of retraction information across digital platforms
- **Authors:** Geoff Frampton, Lois Woods, David A. Scott
- **Year & Venue:** 2021, PLOS ONE 16(11): e0258935
- **DOI:** [10.1371/journal.pone.0258935](https://doi.org/10.1371/journal.pone.0258935)
- **Original Task & Method:** Observational empirical audit assessing whether retraction notices for 53 biomedical publications were consistently visible across 18 digital platforms (e.g., PubMed, Crossref, publisher sites).
- **Original Evaluation Protocol:** Descriptive manual auditing of notice banners, watermarks, and status metadata.
- **Reported Findings & Limitations:** Over 30% of platform listings failed to show retraction notices; observational human study without an automated algorithmic classification or reconciliation pipeline.
- **Computational Requirement:** Negligible (observational study). Highly adaptable to automated metadata query pipelines.

### Paper 3: Heibi & Peroni (2021)
- **Title:** A qualitative and quantitative analysis of open citations to retracted articles: The Wakefield 1998 et al.'s case
- **Authors:** Ivan Heibi, Silvio Peroni
- **Year & Venue:** 2021, Scientometrics 126: 7833–7870
- **DOI:** [10.1007/s11192-021-04097-5](https://doi.org/10.1007/s11192-021-04097-5)
- **Original Task & Method:** Longitudinal citation network analysis tracing post-retraction citation trajectories to Wakefield's fraudulent autism paper using OpenCitations data.
- **Reported Findings & Limitations:** Over 80% of citing works cited the retracted paper affirmatively without acknowledging the retraction; focused on a single high-profile case study rather than a general automated verification system.
- **Computational Requirement:** Low; graph analysis and SQL/DataFrame filtering.

---

## 3. Selected Method & Tractability Justification
- **Selected Method:** Automated Multi-Source Retraction Verification and Provenance Reconciliation.
- **Tractability Justification:** Rather than training large compute-intensive deep learning models on unstructured text, this study adapts Frampton et al.'s observational findings into an automated, deterministic software verification pipeline. The approach requires only lightweight Python, live REST API calls, and standard data frames, making it 100% reproducible on local Apple Silicon M2 hardware.
- **Executable Baselines:**
  - **B0 (Single-Source Naive):** OpenAlex Works API Boolean `is_retracted`.
  - **B1 (Single-Source Explicit):** Crossref REST API `update-to` / `relation` with type `retraction`.
- **Proposed Comparative Method ($M_{\text{prop}}$):** Multi-Source Provenance-Aware Consensus Pipeline. Performs canonical DOI normalization, queries both providers with exponential backoff, reconciles conflicting signals using explicit notice provenance, provides structured evidence links, and abstains safely as `UNKNOWN` rather than emitting false negatives.

---

## 4. Mandatory Literature-to-Experiment Method Bridge Diagram

```
+-----------------------------------------------------------------------------------+
|                           ORIGINAL PUBLISHED RESEARCH                             |
|  - Frampton et al. (2021): Inconsistent retraction notice dissemination          |
|  - Heibi & Peroni (2021): Persistent uncritical citations to retracted papers    |
|  - Cohan et al. (2019): Citation context & intent boundaries                      |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                          SELECTED VERIFICATION METHOD                             |
|  Automated Identifier-Based Retraction-Status Verification using Multi-Source     |
|  Scholarly Metadata APIs (Crossref REST API + OpenAlex Works API)                 |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                            EXECUTABLE PYTHON BASELINE                             |
|  Baseline B0: OpenAlex Works API `is_retracted` Boolean                          |
|  Baseline B1: Crossref REST API `updated-by` Typed Retraction Relation            |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                        CONTROLLED EXPERIMENTAL COMPARISON                         |
|  Evaluate B0 vs B1 vs M_prop (Multi-Source Consensus Pipeline)                    |
|  on Frozen 80-DOI Benchmark (40 Retracted Positives + 40 Unretracted Controls)    |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                             MEASURED EMPIRICAL RESULTS                            |
|  Precision, Recall, F1_determinate, F1_end_to_end, Abstention, Latency, Disagree  |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                             AUDITED RESEARCH PAPER                                |
|  6–10-page IEEE/ACM style manuscript in LaTeX compiled via Tectonic to PDF       |
+-----------------------------------------------------------------------------------+
```

---

## 5. Actual Outcome
- Three primary literature sources rigorously documented with DOIs and limitations.
- Methodological bridging established from observational literature to automated computational pipeline.
- Single-source baselines and proposed consensus pipeline specified.
- Visual textual flowchart verified.
- **Official SAVE Deliverable:** Mandatory bridge: original papers → selected method → executable baseline → planned test recorded.
