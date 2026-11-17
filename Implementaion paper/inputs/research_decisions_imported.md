# Research Decisions Log

## Project
**Title:** An Automated Pipeline for Flagging Outdated Citations in AI-Recommended Literature  
**Status:** Stage 1 — literature review intake  
**Last updated:** 2026-10-21  
**Source reviewed:** `Ai_citation_flagger-3.pdf` (12 pages)

## Evidence conventions
- **VERIFIED:** Directly supported by an inspected source, file, or reproducible execution.
- **INFERRED:** A reasoned interpretation or hypothesis awaiting confirmation.
- **UNKNOWN:** Evidence is missing or insufficient.

## D001 — Establish the submitted review's scope
- **Status:** VERIFIED
- **Decision:** Treat the submitted PDF as the initial scope document.
- **Reason:** The review explicitly covers citation recommendation/ranking, citation context and intent, temporal scholarly status, post-retraction citation behavior, and AI-era citation integrity.
- **Source/evidence:** `Ai_citation_flagger-3.pdf`, abstract and Sections 2–5 (pages 1–6).
- **Next action:** Check whether the cited works support the review's gap claims; update this entry if the evidence changes.

## D002 — Distinguish the review's claims from established field-wide gaps
- **Status:** VERIFIED
- **Decision:** Treat the six gaps in Section 7 as claims made by the submitted review, not as independently established novelty claims yet.
- **Reason:** A review's synthesis does not by itself establish that no relevant benchmark, method, or end-to-end system exists.
- **Source/evidence:** `Ai_citation_flagger-3.pdf`, Section 7 (pages 9–10).
- **Next action:** Verify relevant papers, datasets, tools, and more recent work before finalizing a novelty claim.

## D003 — Define the first implementation's scope
- **Status:** UNKNOWN
- **Decision:** Do not yet commit to detecting every meaning of “outdated.”
- **Reason:** The review itself distinguishes explicit status events such as retraction from broader, harder-to-label notions such as supersession or evidence becoming obsolete.
- **Source/evidence:** `Ai_citation_flagger-3.pdf`, Section 2.3 (page 3) and Section 6.5 (page 9).
- **Next action:** Choose an operational definition and label taxonomy after inspecting the existing repository, available data, and feasibility constraints.

## D004 — Establish a verified baseline
- **Status:** UNKNOWN
- **Decision:** Do not claim a baseline, working implementation, or performance result until code and outputs are inspected or reproduced.
- **Reason:** No implementation or experiment has yet been verified in this project log.
- **Source/evidence:** Initial intake; no repository, dataset, test output, or experiment log inspected.
- **Next action:** Inspect the existing GitHub repository or ask the user to upload the relevant source files and outputs.

## D005 — Keep status checks evidence-grounded and auditable
- **Status:** INFERRED
- **Decision:** A feasible initial system may be strongest if it prioritizes explicit, externally verifiable status events and returns provenance and check timestamps.
- **Reason:** The review emphasizes distributed status information, temporal validation, and explainable output; deterministic status signals are more directly testable than broad epistemic obsolescence.
- **Source/evidence:** `Ai_citation_flagger-3.pdf`, Sections 3.4, 6.2, and 8.1 (pages 4, 8, and 10).
- **Next action:** Validate this design choice against available APIs/data and the existing implementation.

## Review scope summary
- Citation recommendation and ranking methods, including text/content, graph, and semantic approaches.
- Citation context, intent, and citation framing.
- Retraction, correction, supersession, versions, and temporal validity.
- Persistence of citations to retracted work and inconsistent propagation of status information.
- AI-generated citation reliability and external verification.
- Proposed pipeline stages: candidate generation, identifier normalization, status retrieval, temporal validation, context/intent analysis, risk scoring, and explainable output.

## Research questions — provisional, not yet adopted
1. **RQ1 (INFERRED):** How reliably can an automated pipeline identify explicit scholarly status events for AI-recommended references when identifiers and metadata vary?
2. **RQ2 (INFERRED):** Does adding status-aware checks reduce unsafe recommendations compared with a relevance-only or metadata-only baseline on a labeled evaluation set?
3. **RQ3 (INFERRED):** How often do missing, conflicting, or delayed status records prevent a correct decision?
These are candidate questions only. Adopt or revise them after repository, dataset, and related-work inspection.

## Experiment registry
No experiments have been run or verified yet. Do not report metrics until an experiment is executed and its inputs, configuration, and outputs are retained.

## Open questions
- What exactly counts as “outdated” in the first version: retracted only, retracted/corrected/withdrawn, or broader supersession?
- What is the input: an AI-generated bibliography, a list of DOIs, citation contexts, or a live recommender?
- Which repository files and existing outputs are available?
- Which status sources can be used, and what are their coverage, licensing, and rate limits?
- What labeled dataset or annotation process can support evaluation?
- Which baseline is appropriate and reproducible?
- What evaluation split prevents leakage between related papers or status events?

## Next actions
1. User provides the current GitHub repository URL or uploads source code, README, dependency files, test outputs, and any dataset/sample records.
2. Inspect the implementation before proposing code changes.
3. Verify the core literature and the novelty claims in Section 7.
4. Define a narrow, operational outdatedness taxonomy.
5. Select a baseline and pre-register evaluation metrics before running experiments.

## Change history
- 2026-10-21: Created initial log after inspecting the 12-page literature review.
