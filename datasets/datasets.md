# Datasets

This section contains datasets relevant to scholarly literature analysis, citation relationships, scientific-paper processing, and citation-context analysis. These datasets can support the development of an automated pipeline for identifying and flagging potentially outdated citations in AI-recommended literature.

---

## 1. S2ORC — Semantic Scholar Open Research Corpus

**GitHub Dataset:**  
https://github.com/allenai/s2orc

**Description:**  
S2ORC (Semantic Scholar Open Research Corpus) is a large-scale corpus of scientific papers designed for natural language processing and text-mining research. It contains machine-readable scholarly literature and information related to scientific documents and citations. The original dataset has since been integrated into the Semantic Scholar dataset infrastructure. :contentReference[oaicite:0]{index=0}

**Why it is related to this topic:**  
S2ORC is highly relevant to **An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature** because the project requires scholarly papers and citation information to identify older references and compare them with related research. It can support citation analysis, scientific-paper retrieval, and identification of newer literature that may supersede or provide updated information compared with an older citation.

**Use in the project:**
- Analyze scientific papers and bibliographic information.
- Examine citation relationships.
- Retrieve related scholarly literature.
- Compare older cited papers with newer research.
- Support automated citation-age and relevance analysis.

---

## 2. PeerRead

**GitHub Dataset:**  
https://github.com/allenai/PeerRead

**Description:**  
PeerRead is a dataset of scientific paper drafts and peer reviews. The dataset contains more than 14,000 paper drafts and more than 10,000 textual peer reviews from research venues including ACL, NIPS, and ICLR. Its structured data also includes paper metadata, references, and reference mentions with citation contexts. :contentReference[oaicite:1]{index=1}

**Why it is related to this topic:**  
PeerRead is relevant because an automated citation-auditing pipeline needs to understand **how references are used within scientific papers**. Its reference and reference-mention information can support analysis of citation contexts and the relationship between a citation and the surrounding research claim.

**Use in the project:**
- Analyze scientific-paper text.
- Extract and examine references.
- Study citation contexts.
- Analyze reference mentions within papers.
- Support research-paper and citation analysis.

---

## 3. CiteSeer Dataset

**GitHub Dataset:**  
https://github.com/ZPowerZ/citeseer-dataset

**Description:**  
The CiteSeer dataset repository contains a collection of 3,312 scientific papers together with their citation relationships. It provides two main files: `citeseer.content`, containing paper descriptions and class labels, and `citeseer.cites`, containing the citation graph between papers. :contentReference[oaicite:2]{index=2}

**Why it is related to this topic:**  
CiteSeer is directly useful for **citation-network analysis**, which is an important component of identifying potentially outdated citations. The citation graph can be used to examine which papers cite other papers and to study relationships between older and newer publications.

**Use in the project:**
- Analyze citation networks.
- Examine citing and cited papers.
- Study relationships between scientific publications.
- Support citation-ranking and graph-based analysis.
- Identify citation patterns that may indicate outdated references.

---

## Dataset Comparison

| Dataset | Main Data | Relevance to Project |
|---|---|---|
| **S2ORC** | Scientific papers and citation-related information | Finding and comparing scholarly literature and citations |
| **PeerRead** | Paper text, references, and citation contexts | Understanding how citations are used in research papers |
| **CiteSeer** | Papers and citation graph | Analyzing relationships between cited and citing papers |

## Most Relevant Dataset

Among these datasets, **S2ORC is the most relevant** to this project because the proposed pipeline needs a large collection of scholarly papers and citation information to compare existing citations with newer research. **PeerRead** is particularly useful for citation-context analysis, while **CiteSeer** is useful for studying citation-network relationships.
