# Prompt 12 Output: Chosen Contribution Pathway and Executable Comparison Plan

> **Phase IV Deliverable:** Formal selection of Pathway B (Controlled Comparative Study), comparative experimental architecture, independent and controlled variables, expected failure modes, and criteria for genuine negative outcomes.

---

## 1. Official Handbook Prompt Specification
- **Prompt:** Choose and evaluate a defensible contribution
- **Official SAVE Deliverable:** Chosen contribution pathway and executable comparison plan.
- **Evidence Status:** VERIFIED (frozen protocol locked in `configs/protocol_v1.yaml`).
- **Substantive Artifact Links:**
  - Frozen Protocol Config: [protocol_v1.yaml](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/configs/protocol_v1.yaml)
  - Research Decisions: [research_decisions.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/research_decisions.md#d013--defensible-contribution-pathway)
  - Baseline Validation Report: [10_baseline_reproduction.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/prompt_outputs/10_baseline_reproduction.md)

---

## 2. Selected Contribution Pathway: Pathway B (Controlled Comparative Study)

### Justification & Constraint Alignment
According to Section 3 of the Revised Student Handbook, four approved pathways exist:
- *Pathway A: Reproduction + Extension*
- *Pathway B: Controlled Comparative Study*
- *Pathway C: Targeted Component Modification*
- *Pathway D: Hybrid Study*

**Pathway B (Controlled Comparative Study)** is selected for the following evidence-grounded reasons:
1. **Empirical Tractability:** Comparing two widely adopted open scholarly metadata infrastructures (OpenAlex Works API vs. Crossref REST API) against a unified consensus engine directly answers whether multi-source engineering is necessary or redundant.
2. **Computational Feasibility:** Executes deterministically on local Apple Silicon M2 hardware without requiring multi-GPU training clusters or paid commercial API tokens.
3. **Absence of Hyperparameter Leakage:** Unlike neural model fine-tuning where hyperparameter choices can obscure baseline fairness, rule-based API comparators operate under frozen, deterministic decision boundaries.
4. **Direct Impact on Citation Safety:** Recommenders and AI literature tools currently rely on single metadata providers; measuring their empirical divergence reveals real-world risks in automated literature workflows.

---

## 3. Executable Comparison Plan

### Comparator Systems
1. **$B_0$ (OpenAlex Baseline):** Single-source naive retraction classification using the `is_retracted` Boolean field. Fast and widely used, but vulnerable to indexing lags and opaque data ingestion.
2. **$B_1$ (Crossref Baseline):** Single-source explicit notice relation classification using `updated-by` / `relation` with type `retraction`. High precision with machine-readable notice DOIs, but lower recall due to voluntary publisher participation.
3. **$M_{\text{prop}}$ (Proposed Consensus Pipeline):** Multi-source provenance-aware reconciliation engine. Merges signals, extracts explicit notice DOIs, prioritizes verified retraction notices, and safely abstains as `UNKNOWN` when signals are contradictory or missing.

### Experimental Variables
- **Independent Variable:** Classification Architecture ($B_0$ vs. $B_1$ vs. $M_{\text{prop}}$).
- **Controlled Variables:**
  - Evaluation Instances: Identical frozen 80-DOI balanced split ($N=80$).
  - Random Seed: Fixed seed `20261028` for candidate sampling.
  - Network Configuration: Pinned timeout of 10s, exponential backoff (up to 3 retries), local disk caching to prevent temporal drift.
  - Evaluation Metrics: Pinned metric scripts in `src/metrics.py`.
- **Dependent Variables:**
  - Primary: End-to-End F1 Score ($\text{F1}_{\text{e2e}}$).
  - Secondary: Determinate F1 ($\text{F1}_{\text{det}}$), Precision, Recall, Abstention Rate, Disagreement Rate, Mean Query Latency (ms).

---

## 4. Benchmark Dataset Composition ($N=80$)
- **Positive Partition ($N_1 = 40$):** Verified retracted papers sampled from Crossref Retraction Watch dataset, stratified across:
  - Multidisciplinary: Nature (8), Science (4), PNAS (4), PLOS ONE (4)
  - Biomedical / Life Sciences: Elsevier / Cell Press (8), Springer Nature (6)
  - Physical / Engineering: Wiley (3), IEEE (3)
  - Publication years: 2001 to 2023; Retraction years: 2005 to 2024.
- **Negative Control Partition ($N_0 = 40$):** Unretracted, highly cited seminal works published in identical venues and years, verified to have zero retraction, correction, or withdrawal flags.

---

## 5. Failure Modes and Genuine Negative Result Definition
- **Expected Failure Mode 1 (Silent False Negatives in Crossref):** Publishers failing to populate Crossmark `updated-by` relations, causing Crossref to report `NOT_RETRACTED` on retracted papers.
- **Expected Failure Mode 2 (OpenAlex Opaque Status):** OpenAlex flagging a paper as retracted without providing the corresponding retraction notice DOI or explanation.
- **Genuine Negative Result Condition:** If the empirical results demonstrate that:
  $$\text{Recall}_{M_{\text{prop}}} \le \text{Recall}_{B_0} \quad \text{and} \quad \text{F1}_{\text{e2e}}(M_{\text{prop}}) \le \text{F1}_{\text{e2e}}(B_0)$$
  and Crossref contributes zero unique detections while increasing latency and complexity, the hypothesis $H_1$ is **REFUTED**, representing a genuine negative result. This outcome will be reported transparently without post-hoc manipulation.

---

## 6. Actual Outcome
- Pathway B selected with scientific and operational justification.
- 80-DOI benchmark architecture and comparator rules finalized.
- Variables, failure modes, and negative result criteria pre-registered.
- **Official SAVE Deliverable:** Chosen contribution pathway and executable comparison plan recorded.
