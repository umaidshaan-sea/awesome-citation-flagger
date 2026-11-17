# Prompt 05 Output: Gate G1 One-Page Research Brief

> **Gate G1 Checkpoint:** Mandatory Research Brief Template (Handbook Section 11). Formally approved and verified prior to baseline execution.

---

## 1. Official Handbook Prompt Specification
- **Prompt:** Frame research questions and success criteria
- **Official SAVE Deliverable:** One-page problem brief with questions and measurable outcomes.
- **Evidence Status:** VERIFIED (Gate G1 Complete).
- **Substantive Artifact Links:**
  - Base Literature Review: [MSE_09_Umaid-1.pdf](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/inputs/MSE_09_Umaid-1.pdf)
  - Prior Work Transcripts: [ATR_MSE2026009.pdf](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/inputs/ATR_MSE2026009.pdf), [ATR_Prompt_3_4_MSE2026009.pdf](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/inputs/ATR_Prompt_3_4_MSE2026009.pdf)
  - Research Decisions: [research_decisions.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/research_decisions.md#d003--define-the-first-implementations-scope)

---

## 2. Gate G1 Official Research Brief

| Field | Project Specification |
|---|---|
| **Student Author** | Md Umaid Shaan (Enrollment: MSE2026009) |
| **Review Topic & Key Papers** | *An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature*<br>• Cohan et al. (2019) [*NAACL-HLT*, DOI: 10.18653/v1/N19-1361]<br>• Frampton et al. (2021) [*PLOS ONE*, DOI: 10.1371/journal.pone.0258935]<br>• Heibi & Peroni (2021) [*Scientometrics*, DOI: 10.1007/s11192-021-04097-5] |
| **Research Gap** | Inconsistent and fragmented propagation of retraction notices across digital scholarly platforms (Frampton et al. 2021), coupled with the lack of multi-source provenance reconciliation in automated citation recommenders and AI retrieval pipelines (Review Section 7.1). |
| **Primary Research Question** | **RQ1 (Primary):** Does a multi-source reconciliation pipeline combining Crossref explicit notice relations and OpenAlex status metadata improve retraction detection recall and end-to-end F1 score compared to single-source baselines on a controlled evaluation benchmark? |
| **Secondary Research Questions** | **RQ2:** How frequently do Crossref and OpenAlex status signals diverge on verified retracted literature, and what are the primary structural causes of disagreement?<br>**RQ3:** Does abstaining as `UNKNOWN` rather than emitting false negatives provide a safer operational trade-off for citation integrity in academic recommendation? |
| **Study Pathway** | **Pathway B: Controlled Comparative Study** (Handbook Section 3). Comparing single-source baseline B0 (OpenAlex) and B1 (Crossref) against proposed multi-source consensus method ($M_{\text{prop}}$). |
| **Dataset & Partitions** | **Primary Data:** Official Crossref Retraction Watch Open Data snapshot (`commit: fb5f174f...`, 73,597 records).<br>**Benchmark Split:** Frozen 80-DOI balanced evaluation benchmark ($N=80$):<br>• 40 positive formal retraction cases spanning years 2000–2024 across major publishers (Nature, Science, Elsevier, Wiley, Springer).<br>• 40 negative control cases consisting of verified, highly cited, unretracted papers from identical years and journals. |
| **Baselines & Comparators** | • **Baseline B0:** OpenAlex Works API Boolean `is_retracted`.<br>• **Baseline B1:** Crossref REST API `update-to` / `relation` with type `retraction`.<br>• **Proposed Method ($M_{\text{prop}}$):** Multi-Source Provenance-Aware Consensus Pipeline with deterministic notice linking and safe abstention. |
| **Primary Metrics & Control** | • **Primary:** End-to-End F1 Score ($\text{F1}_{\text{e2e}}$) where positive abstentions count as False Negatives.<br>• **Secondary:** Determinate F1 ($\text{F1}_{\text{det}}$), Precision, Recall, Abstention Rate, Disagreement Rate, API Latency (ms).<br>• **Success Threshold:** Statistically significant improvement ($\Delta \text{Recall} \ge +5\%$) and $\text{F1}_{\text{e2e}} \ge 0.90$ with zero false-negative misclassifications on retracted instances having verified Crossref notices. |

---

## 3. Formal Hypotheses, Variables, & Falsification Criteria

### Formal Hypotheses
- **$H_0$ (Null Hypothesis):** Combining Crossref and OpenAlex retraction metadata does not improve retraction detection recall over the best single-source comparator on the evaluation benchmark ($\text{Recall}_{\text{prop}} \le \max(\text{Recall}_{B0}, \text{Recall}_{B1})$).
- **$H_1$ (Alternative Hypothesis):** Combining Crossref and OpenAlex retraction metadata achieves strictly higher retraction detection recall than either single-source baseline alone ($\text{Recall}_{\text{prop}} > \max(\text{Recall}_{B0}, \text{Recall}_{B1})$).

### Experimental Variables
- **Independent Variable:** Verification Architecture (Single-source OpenAlex vs Single-source Crossref vs Dual-source Consensus Pipeline).
- **Dependent Variables:** Classification Precision, Recall, Determinate F1, End-to-End F1, Abstention Rate, Latency.
- **Control Variables:** Fixed random seed `20261028`, identical 80-DOI benchmark evaluation instances, identical network timeout (10s) and retry policies.

### Decision Rules & Falsification Conditions
- **Falsification Observation 1:** If OpenAlex `is_retracted` already achieves 100% recall on the retracted partition and Crossref adds no additional detected retractions while adding query latency, $H_0$ cannot be rejected, and the multi-source pipeline fails its primary value proposition.
- **Falsification Observation 2:** If multi-source reconciliation increases False Positive flags on unretracted negative controls, the consensus mechanism will be rejected as unsafe.

---

## 4. Actual Outcome
- Gate G1 requirements fully fulfilled.
- 1-page research brief completed following official template.
- Testable hypotheses, variables, decision rules, and falsification criteria pre-registered.
- **Official SAVE Deliverable:** One-page problem brief with questions and measurable outcomes recorded.
