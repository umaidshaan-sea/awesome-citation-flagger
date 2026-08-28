
# GitHub Implementations

This section contains existing GitHub implementations related to scientific paper recommendation, citation recommendation, citation analysis, and automated scholarly literature discovery. These implementations provide practical examples of technologies and approaches relevant to developing an automated pipeline for flagging potentially outdated citations in AI-recommended literature.

## 1. Citeomatic

**Repository:** AllenAI Citeomatic

**What it implements:**  
Citeomatic is an open-source citation recommendation system designed to help users find relevant citations for research-paper drafts. The repository contains code for training and evaluating citation recommendation models and includes trained models and instructions for reproducing the associated research. It is backed by the Semantic Scholar OpenCorpus dataset. :contentReference[oaicite:1]{index=1}

**Why it is relevant:**  
Citeomatic is directly related to citation recommendation. Its approach provides a useful reference point for the recommendation stage of an automated pipeline. A citation-auditing system could build on similar recommendation techniques and add a temporal verification stage to identify potentially outdated citations.

**GitHub:**  
https://github.com/allenai/citeomatic

---

## 2. Citation Recommendation based on Citation Contexts

**Repository:** Citation Recommendation based on Citation Contexts

**What it implements:**  
This project implements a scientific article recommendation system that recommends relevant citations based on citation contexts. It uses information-retrieval approaches including query expansion, spelling correction, BM25, TF-IDF, and latent semantic indexing. :contentReference[oaicite:2]{index=2}

**Why it is relevant:**  
Citation context is important when determining whether a reference actually supports a particular claim. This implementation provides a practical example of using citation context for citation recommendation and can inform the citation-context analysis component of an outdated-citation detection pipeline.

**GitHub:**  
https://github.com/prabhat1081/Citation-Recommendation-based-on-citation-contexts

---

## 3. Citation Recommendation for Research Papers via Knowledge Graphs

**Repository:** Citation Recommendation for Research Papers via Knowledge Graphs

**What it implements:**  
This implementation provides source code for a citation recommendation approach based on knowledge graphs. It uses citation information and scientific-paper representations and includes code for constructing citation graphs and performing citation-recommendation ranking. The repository also uses SPECTER embeddings and other scientific-text representations. :contentReference[oaicite:3]{index=3}

**Why it is relevant:**  
Citation networks and knowledge graphs can help identify relationships between papers. These relationships can be useful for finding newer papers connected to an older citation and determining whether a cited work may have been superseded by later research.

**GitHub:**  
https://github.com/arthurbrack/citation-recommendation-kg

---

## 4. PaperFlow

**Repository:** OpenRaiser PaperFlow

**What it implements:**  
PaperFlow is a scientific-paper recommendation and research workflow system. It supports personalized paper discovery, paper ranking, reading, feedback, and adaptive recommendations. It provides command-line and local browser interfaces for discovering and managing research papers. :contentReference[oaicite:4]{index=4}

**Why it is relevant:**  
PaperFlow demonstrates how automated scientific-paper recommendation can be incorporated into a complete research workflow. Its recommendation and feedback mechanisms are relevant to the AI-recommended-literature component of this project. An outdated-citation pipeline could operate as an additional verification layer after papers are recommended.

**GitHub:**  
https://github.com/OpenRaiser/PaperFlow

---

## 5. NLP-based Scientific Article Suggestion System

**Repository:** SWE-599 NLP-based Scientific Article Suggestion System

**What it implements:**  
This project implements an NLP-based academic paper recommendation system. It monitors publications using the OpenAlex API and matches newly published papers against researcher profiles using a two-stage retrieval-augmented generation (RAG) pipeline. :contentReference[oaicite:5]{index=5}

**Why it is relevant:**  
The project demonstrates the use of OpenAlex, NLP, retrieval, and RAG for scientific-paper recommendation. These technologies are relevant to identifying newer research that could be compared with citations produced by an AI recommendation system.

**GitHub:**  
https://github.com/senaoz/SWE-599

---

## 6. S2ORC

**Repository:** Semantic Scholar Open Research Corpus

**What it implements:**  
S2ORC is an open research corpus and associated software for machine-readable scientific papers. The repository provides resources for working with scientific-paper metadata and full text and includes tools such as `s2orc-doc2json` for converting scientific documents into structured JSON. :contentReference[oaicite:6]{index=6}

**Why it is relevant:**  
S2ORC is highly relevant to automated citation analysis because scientific papers contain references and citation mentions that can be processed computationally. Structured paper information can be used as input for extracting citations, analyzing citation contexts, and comparing cited papers with newer literature.

**GitHub:**  
https://github.com/allenai/s2orc

---

## Summary

| Implementation | Main Function | Relevance |
|---|---|---|
| **Citeomatic** | Citation recommendation | Provides a foundation for recommending relevant citations |
| **Citation Recommendation based on Citation Contexts** | Context-based citation recommendation | Supports citation-context analysis |
| **Citation Recommendation via Knowledge Graphs** | Knowledge-graph citation recommendation | Supports citation-network and related-paper analysis |
| **PaperFlow** | Personalized scientific-paper recommendation | Demonstrates automated literature discovery and recommendation |
| **NLP-based Scientific Article Suggestion System** | NLP/RAG paper recommendation | Demonstrates finding newer and relevant research |
| **S2ORC** | Scientific-paper processing and corpus resources | Supports automated paper, reference, and citation analysis |
