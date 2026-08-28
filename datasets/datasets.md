
# Datasets

Relevant datasets for research on scholarly literature, citation analysis, citation contexts, and scientific paper recommendation are collected below. These datasets can support the development and evaluation of an automated pipeline for flagging potentially outdated citations in AI-recommended literature.

## 1. OpenAlex

**Source:** OpenAlex

**Description:**  
OpenAlex is an open catalog of scholarly works, authors, institutions, sources, topics, and citation relationships. It provides bibliographic metadata and information about relationships between scholarly publications.

**Application:**  
OpenAlex can be used to retrieve publication dates, citation counts, references, authors, and related scholarly works. For this project, these data can help compare the age of a cited paper with newer research and identify citations that may require further review.

**Link:**  
[OpenAlex](https://openalex.org/)

[OpenAlex Documentation](https://docs.openalex.org/)

---

## 2. Semantic Scholar Open Research Corpus (S2ORC)

**Source:** Allen Institute for AI / Semantic Scholar

**Description:**  
The Semantic Scholar Open Research Corpus (S2ORC) is a general-purpose corpus for natural language processing and text-mining research over scientific papers. It provides machine-readable scientific-paper information and is now available through the Semantic Scholar data platform. :contentReference[oaicite:0]{index=0}

**Application:**  
S2ORC can be used to analyze scientific text, references, and citation information. For this project, it can support citation-context analysis and help determine whether newer research provides updated information related to an older cited source.

**Link:**  
[S2ORC Dataset](https://github.com/allenai/s2orc)

[Semantic Scholar Datasets](https://www.semanticscholar.org/product/api)

---

## 3. SciCite

**Source:** Allen Institute for AI

**Description:**  
SciCite is a dataset developed for citation-intent prediction in scientific publications. It provides examples for classifying the purpose or intent of citations within scientific text. The dataset was released with the research work on structural scaffolds for citation-intent classification. :contentReference[oaicite:1]{index=1}

**Application:**  
SciCite can be used to analyze how citations function within scientific writing. For this project, citation-intent information can help distinguish different uses of references and provide contextual evidence when evaluating whether an older citation is still appropriate for a particular claim.

**Link:**  
[SciCite Dataset and Project](https://github.com/allenai/scicite)

---

## Dataset Relevance

| Dataset | Main Information | Application in This Project |
|---|---|---|
| **OpenAlex** | Scholarly metadata and citation relationships | Analyze citation age, publication dates, citation activity, and newer related research |
| **S2ORC** | Machine-readable scientific papers and text | Analyze scientific text, references, and citation contexts |
| **SciCite** | Citation-intent information | Analyze the purpose and context of citations |

These datasets provide complementary information for an automated citation-auditing pipeline. OpenAlex can support bibliographic and temporal analysis, S2ORC can support scientific-text and reference analysis, and SciCite can support citation-context and citation-intent analysis.
