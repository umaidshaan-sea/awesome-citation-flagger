# Prompt 02 Output: Evidence-Based Research Gap Matrix

> **Provenance Notice:** Imported prior work from student submission `ATR_MSE2026009.pdf` (pages 5–11) and `Prompt_02_Research_Gap_Matrix.md`, dated 21 October 2026. Labeled as imported prior student work, audited and mapped to experimental execution.

---

## 1. Official Handbook Prompt Specification
- **Prompt:** Extract evidence-based research gaps
- **Official SAVE Deliverable:** Gap matrix: source evidence → candidate question → possible experiment.
- **Evidence Status:** VERIFIED (audited against `inputs/MSE_09_Umaid-1.pdf`).
- **Substantive Artifact Links:**
  - Base Literature Review: [MSE_09_Umaid-1.pdf](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/inputs/MSE_09_Umaid-1.pdf)
  - Prior Work Gap Matrix: [Prompt_02_Research_Gap_Matrix.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/inputs/Prompt_02_Research_Gap_Matrix.md)
  - Research Decisions: [research_decisions.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/research_decisions.md#d002--distinguish-the-reviews-claims-from-established-field-wide-gaps)

---

## 2. Evidence Boundary & Auditing Distinction
All claims extracted from the submitted 12-page literature review (`inputs/MSE_09_Umaid-1.pdf`) are classified into three distinct categories:
1. **Reported Findings:** Empirical observations documented in cited primary papers (e.g., Frampton et al. 2021 regarding retraction visibility; Heibi & Peroni 2021 regarding post-retraction citation persistence).
2. **Review Inferences:** Syntheses, proposed pipeline architectures, and conceptual gap taxonomies derived by the author in Sections 6 and 7.
3. **Novelty Boundary:** Marked **UNKNOWN** until independently corroborated through systematic bibliographic and software indexing.

---

## 3. Evidence-Based Research Gap Matrix

| Gap ID | Proposed Research Gap | Evidence Location in Review | Nature of Evidence | Testable Research Question | Candidate Experiment | Required Resources & Metrics | Primary Risks & Failure Modes |
|---|---|---|---|---|---|---|---|
| **G1** | **Provenance-Aware Multi-Source Retraction Reconciliation** | Sec 2.3 (p. 3); Sec 3.4 (p. 4); Sec 6 (pp. 8–9); Refs [6, 7] | Reported in Frampton (2021); Inferred as pipeline gap | Does combining Crossref and OpenAlex retraction metadata improve detection recall and explainability over single-source baselines? | Controlled comparison between single-source queries (OpenAlex `is_retracted`, Crossref `retraction`) and dual-source consensus engine on frozen DOI benchmark. | **Data:** Retraction Watch CSV (GitLab), Crossref REST API, OpenAlex API.<br>**Compute:** Local M2 MacBook.<br>**Metrics:** Precision, Recall, F1_det, F1_e2e, Coverage, Disagreement Rate. | API rate limiting; shared underlying data between OpenAlex and Retraction Watch creating circular validation; missing DOIs. |
| **G2** | **Context-Aware Citation Framing Classification** | Sec 2.2 (p. 3); Sec 3.2 (p. 4); Sec 7.2 (p. 9); Refs [1, 3] | Reported in Cohan (2019); Inferred for retracted literature | Can fine-tuned transformer models reliably classify whether a citation context to a retracted paper is affirming, acknowledging retraction, or uncritical? | Fine-tune SciBERT or RoBERTa on SciCite / annotated retraction citation contexts; evaluate framing accuracy. | **Data:** SciCite dataset, PubMed Central open access full text.<br>**Compute:** Local MPS / Colab GPU.<br>**Metrics:** Macro-F1, per-class accuracy. | Context parsing errors; high annotation cost for human ground truth; domain distribution shift. |
| **G3** | **Multimodal Figure / Table Outdatedness Flagging** | Sec 6.4 (p. 8); Sec 7.3 (p. 9) | Review author inference (speculative) | Can vision-language models identify whether embedded figures or tables in citing manuscripts rely on retracted claims? | Zero-shot evaluation of VLM (e.g. Gemini / CLIP) on retracted publication figures. | **Data:** Open access PDF extracts.<br>**Compute:** High GPU / Cloud VLM.<br>**Metrics:** Precision, Recall. | **NO-GO / UNKNOWN:** Highly speculative, no standard benchmark exists, computationally intractable for MTech lab scope. |
| **G4** | **Temporal Status Propagation Lag Measurement** | Sec 3.4 (p. 4); Sec 5.2 (p. 6); Sec 7.4 (p. 9); Refs [6, 8] | Reported in Heibi (2021); Inferred as measurement gap | What is the empirical latency between publisher retraction notice issuance and metadata synchronization across Crossref and OpenAlex? | Longitudinal timestamp analysis comparing `OriginalPaperDate`, `RetractionDate`, Crossref indexed date, and OpenAlex created date. | **Data:** 73k-row Retraction Watch dataset with timestamp fields.<br>**Compute:** Local Python.<br>**Metrics:** Median lag (days), hazard rate, cumulative distribution. | Incomplete timestamp metadata in historical records; publisher backdating. |
| **G5** | **Pre-print to Publication Status Synchronization** | Sec 2.3 (p. 3); Sec 7.5 (p. 10) | Inferred by review author | How frequently do citation recommenders recommend retracted or superseded preprints when revised peer-reviewed versions exist? | Match bioRxiv/arXiv preprint DOIs against Crossref withdrawal notices and journal publication DOIs. | **Data:** bioRxiv metadata dump, Crossref relations.<br>**Compute:** Moderate.<br>**Metrics:** Discrepancy rate, version mismatch. | Unlinked preprint DOIs; heterogeneous preprint server APIs. |
| **G6** | **RAG Hallucination & Post-Ranking Retraction Constraints** | Sec 4.2 (p. 5); Sec 5.1 (p. 5); Sec 7.6 (p. 10) | Inferred by review author | Does injecting post-ranking retraction constraint filters eliminate retracted citations in RAG-generated academic summaries? | Evaluate academic RAG pipeline with and without deterministic retraction verification filter. | **Data:** Labeled QA evaluation pairs, scholarly retriever.<br>**Compute:** LLM inference costs.<br>**Metrics:** Hallucination rate, citation validity. | RAG retrieval nondeterminism; LLM API expenses. |

---

## 4. Gap Selection & Tractability Analysis
Among the candidate gaps, **G1 (Provenance-Aware Multi-Source Retraction Reconciliation)** is selected as the primary research focus because:
1. It addresses an empirically validated failure mode in scholarly communication (inconsistent platform propagation documented by Frampton et al. 2021).
2. It has direct access to authoritative, complete open data (Crossref Retraction Watch GitLab repository with 73,597 records).
3. It permits a clean, mathematically rigorous, controlled comparative experimental design (Pathway B) that executes locally on MacBook Pro M2 without high cloud compute or paid LLM dependencies.
4. It enables secondary evaluation of **G4 (Temporal Propagation Lag)** through metadata timestamps.

---

## 5. Actual Outcome
- 6 candidate research gaps extracted, audited, and mapped from review evidence.
- Epistemic status delineated: G1, G2, G4 grounded in reported findings; G3, G5, G6 identified as author inferences.
- Gap G1 selected with explicit tractability justification.
- **Official SAVE Deliverable:** Gap matrix: source evidence → candidate question → possible experiment recorded.
