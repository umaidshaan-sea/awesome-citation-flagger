# Automated Verification of Retraction Status in AI Citation Recommendation

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Unit Tests](https://img.shields.io/badge/tests-13%2F13%20passed-brightgreen.svg)]()
[![Gates G1-G4](https://img.shields.io/badge/Gates-G1--G4%20Verified-success.svg)]()
[![Platform: Apple Silicon & Colab](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Colab-lightgrey.svg)]()

> **M.Tech AI Research / Lab Assignment 02: From Review to Research**  
> **Student:** Md Umaid Shaan (`MSE2026009`)  
> **Topic:** Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature  
> **Manuscript:** [`paper/manuscript.pdf`](paper/manuscript.pdf) (8 pages double-column, IEEE/ACM style)

---

## 1. Executive Summary and Problem Brief

Large Language Models (LLMs) and retrieval-augmented generation (RAG) engines frequently recommend scientific papers based on semantic textual similarity without verifying their current validity. Because scientific literature changes over time through formal retractions and corrections, AI systems routinely propagate discredited findings as authoritative citations.

This repository provides a fully reproducible, audited research-engineering benchmark evaluating automated retraction verification across major scholarly metadata infrastructures:
- **Baseline $B_0$ (OpenAlex Works API):** Boolean `is_retracted` indicator.
- **Baseline $B_1$ (Crossref REST API):** Machine-readable `updated-by` typed relation.
- **Proposed Method ($M_{\text{prop}}$):** Provenance-aware consensus pipeline that queries OpenAlex for high-recall detection and Crossref for machine-readable notice DOI provenance linking.
- **Epistemic Output Space:** Formally separates $\mathcal{Y} = \{\text{RETRACTED}, \text{NOT\_RETRACTED}, \text{UNKNOWN}\}$ to prevent missing or unindexed data from silently masquerading as negative proof.

---

## 2. Key Empirical Findings ($N=80$ Balanced Frozen Benchmark)

| Evaluation Method | Precision (det) | Recall | F1 (determinate) | F1 (end-to-end) | Coverage | Notice Provenance |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Baseline $B_0$ (OpenAlex)** | 1.000 | 1.000 | 1.000 | 1.000 | 95.0% | 0.0% (No Notice DOIs) |
| **Baseline $B_1$ (Crossref)** | 1.000 | 0.600 | 1.000 | 0.750 | 75.0% | 60.0% (Notice DOIs) |
| **Proposed $M_{\text{prop}}$ (Consensus)** | **1.000** | **1.000** | **1.000** | **1.000** | **95.0%** | **60.0% (Verified Notices)** |

### Core Scientometric Insights:
1. **The Crossref Silent Notice Gap:** Crossref machine-readable relations missed **40.0% of retractions** (16/40) because publishers failed to deposit Crossmark update metadata, causing end-to-end $\text{F1}_{\text{e2e}}$ to drop to 0.750.
2. **Shared Data Provenance:** OpenAlex achieves 100% recall because it directly mirrors the Retraction Watch database acquired by Crossref. Multi-source architectures do not consult two independent truths; they reconcile curated registry intelligence with publisher deposit infrastructure.
3. **The Value of Consensus:** The proposed pipeline matches 100% recall while enriching 60.0% of cases with **official, machine-readable retraction notice DOIs**, transforming an unexplainable Boolean indicator into an audited proof of status.

---

## 3. Repository Structure

```
AITR_Lab02_MSE2026009_Citation_Retraction/
├── README.md                           # This comprehensive guide
├── requirements.txt                    # Pinned, tested dependencies
├── configs/
│   └── protocol_v1.yaml                # Pre-registered experimental protocol (Seed: 20261028)
├── data/
│   ├── README.md                       # Provenance, schemas, multi-DOI filtering rules
│   ├── raw/
│   │   └── retraction_watch.csv        # Snapshot (commit: fb5f174f..., SHA-256: e5351ee5...)
│   └── splits/
│       └── benchmark_80_frozen.csv     # Frozen 80-DOI benchmark (40 retracted + 40 controls)
├── src/
│   ├── __init__.py
│   ├── core.py                         # Canonical DOI normalization & epistemic classes
│   ├── data.py                         # CSV parsing, multi-DOI exclusion, stratified sampling
│   ├── openalex_baseline.py            # Baseline B0 (OpenAlex Works API client)
│   ├── crossref_baseline.py            # Baseline B1 (Crossref REST API client)
│   ├── consensus_pipeline.py           # Proposed M_prop consensus algorithm
│   └── metrics.py                      # Determinate vs end-to-end F1, McNemar paired test
├── tests/
│   ├── __init__.py
│   ├── test_doi_normalization.py       # Unit tests for DOI edge cases & regex
│   ├── test_dataset_validation.py      # Unit tests for Retraction Watch ingestion & split
│   └── test_metrics.py                 # Unit tests for F1 formulas & abstention penalties
├── scripts/
│   ├── download_dataset.py             # Reproducible GitLab clone script
│   ├── validate_dataset.py             # Hash verification and schema validation
│   ├── environment_test.py             # Pre-experiment environment smoke test
│   ├── build_and_run_benchmark.py      # Executes live SSL benchmark evaluation
│   └── generate_figures.py             # Renders publication figures & LaTeX tables
├── results/
│   ├── processed/
│   │   ├── benchmark_results.csv       # Raw 80-row experimental output
│   │   └── metrics_summary.json        # Compiled evaluation metrics
│   ├── figures/
│   │   ├── metric_comparison.png       # Figure 1 (PNG & PDF)
│   │   └── disagreement_breakdown.png  # Figure 2 (PNG & PDF)
│   ├── tables/
│   │   ├── comparative_metrics_table.tex # Table 1 LaTeX source
│   │   └── disagreement_cases.tex      # Table 2 LaTeX source
│   └── logs/
│       └── environment_smoke_test.json # Hardware, Python, and package smoke log
├── paper/
│   ├── main.tex                        # 8-page IEEE/ACM manuscript source
│   ├── references.bib                  # 15 independently verified primary references
│   ├── manuscript.pdf                  # Compiled camera-ready PDF
│   ├── figures/                        # Embedded publication vector & raster graphics
│   └── tables/                         # Embedded LaTeX tables
├── prompt_outputs/                     # Authentic deliverables for Prompts 01 through 18
├── research_decisions.md               # Logged research decisions D001 through D015
├── deviations.md                       # Documented scientific deviations DEV-001 to DEV-004
├── ai_assistance_log.md                # Human-AI collaboration provenance matrix
└── artifact_manifest.csv               # SHA-256 hashes and verification status for all files
```

---

## 4. Environment Setup and Verification

### Prerequisites
- Python 3.10, 3.11, 3.12, 3.13, or 3.14
- Git
- Internet connection (for live Crossref & OpenAlex REST queries; offline fallback cached in `benchmark_results.csv`)
- Optional for LaTeX compilation: `tectonic` (`brew install tectonic` on macOS, or `apt install tectonic` on Ubuntu)

### Step 1: Clone and Set Up Virtual Environment
```bash
git clone <repository_url> citation_retraction_study
cd citation_retraction_study

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 2: Run Verification Smoke Tests
```bash
# Run all 13 unit tests
python3 -m unittest discover -s tests -v

# Run environment verification test
python3 scripts/environment_test.py
```
*Expected Result:* All 13 unit tests pass (`Ran 13 tests ... OK`), and `results/logs/environment_smoke_test.json` reports `"overall_status": "PASS"`.

---

## 5. End-to-End Reproduction Instructions

### Step 1: Validate Dataset Integrity
```bash
python3 scripts/validate_dataset.py
```
*Expected Output:*
- Checks `data/raw/retraction_watch.csv` against pre-registered SHA-256 hash `e5351ee51ab3...`.
- Confirms 73,597 raw rows and safe exclusion of 17 compound multi-DOI rows.

### Step 2: Run the Benchmark Experiment
```bash
python3 scripts/build_and_run_benchmark.py
```
*Expected Output:*
- Queries OpenAlex and Crossref for each of the 80 frozen DOIs in `data/splits/benchmark_80_frozen.csv`.
- Saves individual responses and classification outputs to `results/processed/benchmark_results.csv`.
- Computes determinate and end-to-end F1 metrics, McNemar paired statistics, and exports `results/processed/metrics_summary.json`.

### Step 3: Regenerate Publication Figures and Tables
```bash
python3 scripts/generate_figures.py
```
*Expected Output:*
- Generates `results/figures/metric_comparison.png` and `disagreement_breakdown.png`.
- Generates LaTeX tables `results/tables/comparative_metrics_table.tex` and `disagreement_cases.tex`.

### Step 4: Recompile the Research Manuscript
```bash
cd paper
tectonic main.tex
cp main.pdf manuscript.pdf
cd ..
```
*Expected Output:* Produces `paper/manuscript.pdf` (8 pages, zero missing citations, zero LaTeX errors).

---

## 6. Compute Telemetry and Execution Budget

All experiments and evaluations were measured on consumer-grade hardware:
- **Processor:** Apple Silicon M2 (8 cores: 4 performance + 4 efficiency)
- **RAM:** 16 GB Unified Memory
- **Operating System:** macOS 15.0 Darwin 24.6.0
- **Total Compute Runtime:**
  - Unit Tests: 0.18 seconds
  - Benchmark SSL Network Queries ($N=80$): ~44.8 seconds (sequential, respectful of API pools)
  - Figure & Table Generation: 1.12 seconds
  - LaTeX Paper Compilation (`tectonic`): 4.2 seconds
- **Compute Cost:** \$0.00 (entirely open-source, local execution, free public APIs)

---

## 7. Minimum Reproduction Checklist for Secondary Peer

To verify this research independently in under 5 minutes:
- [ ] Run `python3 -m unittest discover -s tests -v` $\rightarrow$ Confirm `13/13 passed`.
- [ ] Run `python3 scripts/validate_dataset.py` $\rightarrow$ Confirm dataset SHA-256 matches `e5351ee51ab3...`.
- [ ] Inspect `data/splits/benchmark_80_frozen.csv` $\rightarrow$ Confirm 40 positive retractions and 40 landmark controls.
- [ ] Run `python3 scripts/build_and_run_benchmark.py` $\rightarrow$ Confirm Table 1 numbers match:
  - OpenAlex Recall = 1.000, F1_e2e = 1.000
  - Crossref Recall = 0.600, F1_e2e = 0.750
  - Proposed Recall = 1.000, Notice DOIs = 60.0%
- [ ] Inspect `paper/manuscript.pdf` $\rightarrow$ Confirm 8 pages total, references on page 8.

---

## 8. Threats to Validity and Scientific Scope

1. **Construct Validity (Narrowed Scope DEV-001):** "Outdated citations" is strictly defined as formal journal retractions with verifiable DOIs. Unretracted papers with outdated methodologies or failed replications are outside this operational definition.
2. **Internal Validity (Historical Records):** Positive ground truth is derived from the official Crossref Retraction Watch snapshot corroborated against primary publisher landing pages.
3. **External Validity ($N=80$ Frozen Benchmark):** $N=80$ is well-stratified across major publishers (Nature, Elsevier, Springer Nature, Wiley, PLOS, Science, IEEE), but performance on obscure or predatory journals with non-standard DOI prefixes may exhibit higher abstention rates.

---

## 9. Ethics, AI Provenance, and Coursework Policy

- **Coursework Boundary:** This project was developed as coursework for Lab Assignment 02 by student Md Umaid Shaan (`MSE2026009`).
- **AI Use Disclosure:** AI pair-programming assistance (Antigravity) was utilized for scaffold creation, LaTeX formatting, and unit testing under strict human oversight. All research decisions, problem narrowing, formula corrections, and verification gates were directed and audited by the student. Complete prompt-by-prompt provenance is preserved in [`ai_assistance_log.md`](ai_assistance_log.md) and [`prompt_outputs/18_ai_audit.md`](prompt_outputs/18_ai_audit.md).
- **No External Side Effects:** No coursework was submitted automatically; no unauthorized Git repositories were published.

---

## 10. Citation and License

### Citation
```bibtex
@article{shaan2026retraction,
  author    = {Shaan, Md Umaid},
  title     = {Automated Verification of Retraction Status in {AI} Citation Recommendation: An Empirical Audit of {Crossref} and {OpenAlex} Metadata Provenance},
  journal   = {M.Tech AI Research Laboratory Papers},
  year      = {2026},
  volume    = {2},
  number    = {MSE2026009},
  pages     = {1--8}
}
```

### License
This repository is open-sourced under the [MIT License](LICENSE). Retraction Watch data is licensed under Creative Commons Public Domain Dedication (CC0).
