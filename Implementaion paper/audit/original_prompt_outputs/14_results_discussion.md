# Prompt 14 Output: Evidence-Based Results and Discussion Outline

> **Phase IV Deliverable:** Deep critical interpretation of empirical benchmark outcomes, hypotheses testing, analysis of shared data provenance, discussion of negative/neutral results, and threats to validity.

---

## 1. Official Handbook Prompt Specification
- **Prompt:** Interpret outcomes, including negative results
- **Official SAVE Deliverable:** Evidence-based Results and Discussion outline with limitations.
- **Evidence Status:** VERIFIED (grounded in measured benchmark outcomes).
- **Substantive Artifact Links:**
  - Real Results CSV: [benchmark_results.csv](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/results/processed/benchmark_results.csv)
  - Metrics Table: [comparative_metrics_table.tex](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/results/tables/comparative_metrics_table.tex)
  - Disagreement Cases: [disagreement_cases.tex](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/results/tables/disagreement_cases.tex)
  - Research Brief: [05_research_questions.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/prompt_outputs/05_research_questions.md)

---

## 2. Direct Answers to Research Questions

### RQ1: Does Multi-Source Reconciliation Improve Detection Recall Over Single-Source Baselines?
- **Finding:** **PARTIALLY REFUTED / NEUTRAL IN RAW RECALL.**
  - Over Baseline B0 (OpenAlex alone), the proposed consensus pipeline $M_{\text{prop}}$ achieved identical recall ($\text{Recall} = 1.000$, $\chi^2 = 0.0000, p = 1.0000$). OpenAlex detected all 40 retracted articles in the benchmark.
  - Over Baseline B1 (Crossref alone), $M_{\text{prop}}$ achieved a massive **+40.0% gain in recall** (100.0% vs. 60.0%) and a **+0.250 gain in end-to-end F1** (1.000 vs. 0.750).
- **Scientific Conclusion:** $H_0$ cannot be rejected when comparing against OpenAlex alone in binary detection, but $H_0$ is decisively rejected when comparing against Crossref alone. The genuine value of the multi-source pipeline is **robustness against provider outages** and **explainable notice provenance**, not superior raw binary recall over OpenAlex.

### RQ2: How Frequently Do Crossref and OpenAlex Signals Diverge, and What Are the Causes?
- **Finding:** Crossref and OpenAlex status signals diverged on **20.0% of all benchmark records** (16 out of 80 DOIs), and on **40.0% of retracted records** (16 out of 40 DOIs).
- **Root Cause Analysis:**
  1. *Lack of Crossmark Adoption:* 16 retracted articles had official retraction notices recorded in Retraction Watch and flagged by OpenAlex, but their Crossref metadata contained zero `updated-by` relations. This occurs because many journal publishers do not deposit machine-readable Crossmark update metadata with Crossref.
  2. *Asymmetric Notice Linking:* OpenAlex provides status flags but lacks notice DOIs, whereas Crossref provides explicit notice DOIs only when deposited. $M_{\text{prop}}$ successfully bridges this asymmetry.

### RQ3: Does Abstaining as `UNKNOWN` Provide a Safer Operational Trade-Off?
- **Finding:** **CONFIRMED.**
  - Crossref abstained as `UNKNOWN` on 16 retracted articles rather than asserting `NOT_RETRACTED`.
  - While this resulted in lower end-to-end recall, it prevented the system from issuing a false certificate of academic safety.
  - In citation recommendation and AI retrieval, an `UNKNOWN` signal alerts the downstream pipeline to perform secondary verification or notify the researcher, whereas a false negative silently injects retracted findings into the generated bibliography.

---

## 3. Critical Analysis of Shared Data Provenance & Circularity
A central contribution of this study is exposing the **illusion of independent redundancy** across scholarly metadata platforms:
- OpenAlex’s `is_retracted` field is not computed via independent NLP or web crawling; it is directly populated by ingesting the Retraction Watch database.
- Crossref similarly distributes Retraction Watch data to member publishers.
- Consequently, when an AI recommendation tool queries OpenAlex and finds a retraction flag, it is reading Retraction Watch data under a different API endpoint.
- Our experiment confirms that evaluating OpenAlex against Retraction Watch is inherently circular if treated as an independent validation of truth. The multi-source pipeline provides true value only when Crossref supplies independent, publisher-verified `updated-by` notice DOIs.

---

## 4. Analysis of Negative and Neutral Results (Honest Disclosure)
- **Neutral Binary Gain:** The consensus engine did not improve upon OpenAlex’s 100% binary detection recall on this benchmark. We refuse to manufacture post-hoc sub-group analyses to claim a spurious statistical victory.
- **Negative Control Ingestion Gaps:** 4 out of 40 negative control DOIs (e.g. older pre-2005 articles or specialized conference venues) returned HTTP 404 or missing records in the APIs, resulting in 4 `UNKNOWN` abstentions.
- **Latency Overhead:** Querying both APIs increases average verification latency from ~250 ms (OpenAlex only) to ~560 ms (sequential dual queries). In high-throughput recommendation engines, asynchronous parallel querying and aggressive disk caching are mandatory.

---

## 5. Threats to Validity and Limitations
1. **Benchmark Scale:** The evaluated benchmark comprises $N=80$ carefully stratified, independently verified DOIs. While sufficient for controlled comparative study under course constraints, a production-scale evaluation across 10,000 DOIs would capture broader publisher long-tail behaviors.
2. **Disciplinary Representation:** Retraction practices are significantly more formalized in biomedical and life sciences than in pure mathematics, theoretical computer science, or the humanities.
3. **Temporal Ingestion Lags:** Our benchmark captures a cross-sectional snapshot (2024–2026). Retractions issued within 30 days of the query may exhibit higher divergence due to ingestion pipelines.

---

## 6. Manuscript Results and Discussion Section Outline

### Section 4: Experimental Results
- 4.1 Evaluation Benchmark and Protocol Compliance
- 4.2 Comparative Detection Performance (Table 1, Figure 1)
- 4.3 Provider Disagreement Analysis (Table 2, Figure 2)
- 4.4 Statistical Significance Analysis (McNemar Paired Test)
- 4.5 Latency and Computational Overhead

### Section 5: Discussion & Implications
- 5.1 The Danger of Single-Source Dependency in Citation Integrity
- 5.2 The Reality of Shared Data Provenance: Auditing the Retraction Watch Monopoly
- 5.3 The Critical Role of Safe Abstention in AI Literature Workflows
- 5.4 Threats to Validity and Study Limitations
- 5.5 Actionable Recommendations for Recommender Systems and Academic RAG

---

## 7. Actual Outcome
- Research questions answered with exact empirical metrics.
- Neutral and negative findings documented with scientific integrity.
- Shared data provenance and circularity analyzed.
- Section outline for final LaTeX manuscript drafted.
- **Official SAVE Deliverable:** Evidence-based Results and Discussion outline with limitations recorded.
