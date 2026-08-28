# GitHub Implementations

This section contains existing GitHub implementations related to citation recommendation, citation-context analysis, scientific-paper representation, and scholarly literature recommendation. These projects provide practical approaches that are relevant to developing an automated pipeline for flagging potentially outdated citations in AI-recommended literature.

---

## 1. BERT-GCN for Paper Citation

**GitHub:**  
https://github.com/TeamLab/bert-gcn-for-paper-citation

**Description:**  
This project implements a context-aware citation recommendation model that combines BERT with Graph Convolutional Networks (GCN). The repository provides code for citation recommendation and includes the **FullTextPeerRead** dataset, which was created by processing the original PeerRead dataset. The dataset contains citing and cited paper IDs, citation-context text, and publication years. :contentReference[oaicite:1]{index=1}

**Dataset Used:**  
PeerRead / FullTextPeerRead

**Relevance to the Topic:**  
This is one of the most directly relevant implementations for the project because it combines **citation context, paper metadata, publication years, and citation relationships**. These features can be adapted to compare an existing citation with newer research and identify citations that may be outdated.

**GitHub Repository:**  
https://github.com/TeamLab/bert-gcn-for-paper-citation

---

## 2. SCINCL — Scientific Document Representations with Citation Embeddings

**GitHub:**  
https://github.com/malteos/scincl

**Description:**  
SCINCL is an implementation for learning scientific document representations using citation embeddings and neighborhood contrastive learning. The project uses **S2ORC** data and includes experiments involving citation graphs, scientific-paper representations, and the SciDocs benchmark. :contentReference[oaicite:2]{index=2}

**Dataset Used:**  
S2ORC

**Relevance to the Topic:**  
The project is relevant because an automated outdated-citation pipeline needs to compare scientific papers and determine relationships between older and newer research. Citation-based document representations can help retrieve papers that are semantically or bibliographically related to an existing citation.

**GitHub Repository:**  
https://github.com/malteos/scincl

---

## 3. Citeomatic

**GitHub:**  
https://github.com/allenai/citeomatic

**Description:**  
Citeomatic is an open-source citation recommendation system developed for recommending relevant citations for scientific documents. It provides implementation components for training and evaluating citation recommendation models.

**Dataset Used:**  
Scientific-paper and citation data used for citation recommendation experiments.

**Relevance to the Topic:**  
Citation recommendation is an important component of the proposed pipeline. Citeomatic provides a useful starting point for generating **alternative or newer candidate citations** that can subsequently be checked against the age and relevance of an existing citation.

**GitHub Repository:**  
https://github.com/allenai/citeomatic

---

## 4. SPECTER — Scientific Document Embeddings

**GitHub:**  
https://github.com/allenai/specter

**Description:**  
SPECTER is an implementation of a document-level representation model designed specifically for scientific papers. It learns scientific document representations using citation-informed training, allowing papers to be represented in a space where related scientific documents can be identified.

**Dataset Used:**  
Semantic Scholar scientific-paper data and citation relationships.

**Relevance to the Topic:**  
SPECTER is highly relevant to the **literature-retrieval stage** of an outdated-citation pipeline. Given an older cited paper, scientific document embeddings can be used to retrieve semantically related papers, including newer publications that may provide more current evidence.

**GitHub Repository:**  
https://github.com/allenai/specter

---

## 5. S2ORC — Scientific Paper Processing

**GitHub:**  
https://github.com/allenai/s2orc

**Description:**  
The S2ORC repository provides the original code and documentation associated with the Semantic Scholar Open Research Corpus. S2ORC was designed for NLP and text-mining research over scientific papers and includes machine-readable scientific-paper information. The current S2ORC data is maintained through the Semantic Scholar dataset infrastructure. :contentReference[oaicite:3]{index=3}

**Dataset Used:**  
S2ORC

**Relevance to the Topic:**  
S2ORC is relevant because the proposed system requires large-scale scholarly documents and citation information. It can support **citation extraction, paper comparison, literature retrieval, and identification of newer research** related to an older citation.

**GitHub Repository:**  
https://github.com/allenai/s2orc

---

## 6. PeerRead

**GitHub:**  
https://github.com/allenai/PeerRead

**Description:**  
PeerRead provides both data and code for analyzing scientific papers and peer reviews. The repository contains more than 14,000 paper drafts, review information, and code for processing and predicting aspects of scientific papers. :contentReference[oaicite:4]{index=4}

**Dataset Used:**  
PeerRead

**Relevance to the Topic:**  
PeerRead is relevant because it provides scientific-paper text and structured research-paper information. It is particularly useful for studying how citations and references occur within scientific documents and forms the basis for the **FullTextPeerRead** dataset used by the BERT-GCN citation-recommendation implementation.

**GitHub Repository:**  
https://github.com/allenai/PeerRead

---

## Implementation Summary

| Implementation | Dataset / Data | Main Purpose | Relevance |
|---|---|---|---|
| **BERT-GCN for Paper Citation** | PeerRead / FullTextPeerRead | Context-aware citation recommendation | Citation context, publication years, and citation relationships |
| **SCINCL** | S2ORC | Scientific document representation | Finding related and newer research |
| **Citeomatic** | Citation recommendation data | Citation recommendation | Generating alternative candidate citations |
| **SPECTER** | Semantic Scholar data | Scientific document embeddings | Retrieving semantically related papers |
| **S2ORC** | S2ORC | Scientific-paper processing | Citation and literature analysis |
| **PeerRead** | PeerRead | Scientific-paper analysis | Paper and citation-context research |

## Most Relevant Implementations for This Project

The three implementations most closely related to **An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature** are:

1. **BERT-GCN for Paper Citation** — useful for citation-context and citation-year analysis.
2. **SCINCL** — useful for finding related scientific papers using citation-based representations.
3. **SPECTER** — useful for retrieving semantically related scientific papers that can serve as newer alternatives.

Together, these approaches can support several stages of the proposed pipeline: **citation-context analysis → related-paper retrieval → comparison with newer literature → outdated-citation flagging**.
