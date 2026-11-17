# Prompt 06 Output: Dataset and Baseline Validation Sheet

> **Phase II Deliverable:** Systematic validation sheet documenting primary dataset schemas, baseline comparator APIs, shared provenance audits, and integrity verification.

---

## 1. Official Handbook Prompt Specification
- **Prompt:** Verify datasets and comparators
- **Official SAVE Deliverable:** Dataset and baseline validation sheet.
- **Evidence Status:** VERIFIED (grounded in inspected GitLab repo `fb5f174` and live API responses).
- **Substantive Artifact Links:**
  - Dataset Documentation: [data/README.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/data/README.md)
  - Dataset Validation Log: [dataset_validation.json](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/results/logs/dataset_validation.json)
  - Source Ledger: [source_ledger.csv](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/source_ledger.csv)
  - Research Decisions: [research_decisions.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/research_decisions.md#d007--dataset-source-selection-and-provenance-auditing)

---

## 2. Primary Dataset Specification: Crossref Retraction Watch

| Parameter | Authoritative Specification |
|---|---|
| **Dataset Name** | Retraction Watch Database (Crossref Open Data Release) |
| **Official Provider** | The Center for Scientific Integrity & Crossref |
| **Source URL** | `https://gitlab.com/crossref/retraction-watch-data.git` |
| **Tracked Git Commit** | `fb5f174f8476824deaf340693f9a819ce5e29ded` (Snapshot date: 2024-05) |
| **Local File Path** | `data/raw/retraction-watch-data/retraction_watch.csv` |
| **File SHA-256 Checksum** | `e5351ee51ab3f1da7fe98b3bd6c5c58049b8bff4705949ef6fd4f1a1315dd0ea` |
| **Sample Size (Raw)** | 73,597 total records |
| **Eligible Single-DOI Rows** | 67,628 records (64,566 unique original paper DOIs) |
| **Excluded Multi-DOI Rows** | 17 records (semicolon-delimited DOIs excluded to avoid lookup ambiguity) |
| **Missing/Invalid DOI Rows** | 5,952 records (legacy pre-DOI items, books without DOIs) |
| **Retraction Types** | 68,155 Retractions; 1,545 Corrections; 2,342 Expressions of Concern; 1,555 Others |
| **Key Feature Fields** | `Record ID`, `OriginalPaperDOI`, `RetractionDOI`, `RetractionNature`, `OriginalPaperDate`, `RetractionDate`, `Reason`, `Publisher`, `Journal` |
| **Licensing** | Creative Commons Public Domain Dedication (CC0) / Crossref Open Data Terms |
| **Known Biases & Artifacts** | High concentration of biomedical literature; English-language dominance; variable publisher lag; retroactive updates |
| **Data Leakage Barriers** | DOI-level disjoint hashing ensures zero overlap between candidate exploration and frozen benchmark evaluation split |

---

## 3. Baseline Comparators Specification

### Baseline B0: OpenAlex Works API (`is_retracted`)
- **Provider / Entity:** OurResearch (OpenAlex)
- **API Endpoint:** `https://api.openalex.org/works/https://doi.org/{DOI}`
- **Documentation:** `https://help.openalex.org/api/`
- **Reference Paper:** Priem et al. (2022), *OpenAlex: An open platform for scholarly metadata*, arXiv:2205.01833.
- **Input:** Canonical DOI string.
- **Output:** JSON object containing boolean field `is_retracted` (True / False).
- **Operational Rule:**
  $$\hat{y}_{B0} = \begin{cases} \text{RETRACTED} & \text{if } \texttt{is\_retracted} = \text{True} \\ \text{NOT\_RETRACTED} & \text{if } \texttt{is\_retracted} = \text{False} \\ \text{UNKNOWN} & \text{if HTTP error / not indexed} \end{cases}$$
- **Reproduction & Provenance Risk:** OpenAlex populates `is_retracted` directly from Retraction Watch, meaning it is not an independent observational source.

### Baseline B1: Crossref REST API (`updated-by` Typed Relation)
- **Provider / Entity:** Crossref
- **API Endpoint:** `https://api.crossref.org/works/{DOI}`
- **Documentation:** `https://www.crossref.org/documentation/retrieve-metadata/rest-api/`
- **Reference Specification:** Crossref Metadata Retrieval Guidelines (2024).
- **Input:** Canonical DOI string.
- **Output:** Crossref message object with `update-to` and `relation` blocks.
- **Operational Rule:**
  $$\hat{y}_{B1} = \begin{cases} \text{RETRACTED} & \text{if } \exists r \in \texttt{relation}: r.\text{type} = \text{'retraction'} \lor \texttt{update-to}.\text{type} = \text{'retraction'} \\ \text{NOT\_RETRACTED} & \text{if message returned with zero retraction relations} \\ \text{UNKNOWN} & \text{if HTTP error / not indexed} \end{cases}$$
- **Reproduction Risk:** Publisher adoption of Crossref Crossmark / updated-by schemas is voluntary; many retractions are not linked via machine-readable relation tags, causing silent false negatives.

---

## 4. Shared Data Provenance & Circularity Audit
- **Provable Fact:** Both OpenAlex and Crossref distribute data originating from Retraction Watch.
- **Auditing Safeguard:** To prevent circular self-validation (evaluating an API against a dataset that supplied its underlying field), this study enforces:
  1. **Independent Evidence Grounding:** For all 40 positive instances in the benchmark split, the retraction status is corroborated by directly verifying the official publisher retraction notice URL and Retraction DOI.
  2. **Negative Control Verification:** 40 negative control DOIs are corroborated across PubMed Central, Crossref, and OpenAlex to confirm zero retraction, withdrawal, or correction flags.

---

## 5. Actual Outcome
- Dataset structure and cryptographic hash verified on real 73,597-row GitLab snapshot.
- Comparator APIs, input/output schemas, and operational decision rules formalized.
- Circularity risks disclosed with independent validation protocol.
- **Official SAVE Deliverable:** Dataset and baseline validation sheet recorded.
