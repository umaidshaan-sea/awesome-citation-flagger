# AI Tools for Research --- Lab Assignment 02

## Prompt 01: Research Workspace and Decision Log

**Student:** Md Umaid Shaan\
**Date:** 21 October 2026\
**Project:** *An Automated Pipeline for Flagging Outdated Citations in
AI-Recommended Literature*

## 1. Research Scope Summary

The attached review examines whether scholarly papers recommended by
citation-recommendation systems or AI tools remain appropriate to cite
at the time of recommendation. It distinguishes topical or semantic
relevance from scholarly-status and contextual validity.

The review covers five connected themes:

1.  **Citation recommendation and ranking:** approaches ranging from
    text and bibliographic matching to contextual, network-based, and
    deep-learning methods.
2.  **Citation context, intent, and framing:** the role a citation plays
    in supporting, contrasting with, or contextualizing a particular
    claim.
3.  **Retraction and broader outdatedness:** including corrections,
    superseded versions, and evidence overtaken by later findings.
4.  **Persistence of citations to retracted work:** including
    inconsistent propagation of retraction information across platforms.
5.  **AI-era citation integrity:** the need for transparent,
    evidence-backed status checks in AI-assisted scholarly workflows.

The review proposes a conceptual multi-stage pipeline involving
identifier resolution, bibliographic and publication-status retrieval,
temporal validation, citation-context and intent analysis, semantic
relevance assessment, risk scoring, and explanations. This is a proposed
design, not a verified executable implementation.

## 2. Evidence Labels

To keep the research process auditable, claims and decisions use the
following labels:

-   **VERIFIED:** Directly supported by the attached review or by a
    source or output inspected for this submission.
-   **INFERRED:** A reasoned proposal derived from the review that
    requires further testing.
-   **UNKNOWN:** Not established from the materials currently inspected.

A claim made by the literature review is not automatically treated as
independently verified evidence from the original publication. Original
papers and their specific findings must be checked before final claims
are made.

## 3. Current Project State

  -----------------------------------------------------------------------
  Item                    Status                  Evidence or note
  ----------------------- ----------------------- -----------------------
  Completed literature    **VERIFIED**            The attached review
  review exists                                   PDF.

  Research area           **VERIFIED**            Citation
                                                  recommendation,
                                                  citation intent,
                                                  retraction/status
                                                  awareness, and AI
                                                  citation integrity.

  Separate executable     **VERIFIED (student     The GitHub repository
  research implementation clarification)**        is the work currently
                                                  available; no separate
                                                  executable research
                                                  implementation exists.

  Initial scope           **VERIFIED (student     Begin with explicit
                          decision)**             retraction-status
                                                  detection.

  Dataset access and      **UNKNOWN**             No dataset has yet been
  readiness                                       downloaded, licensed,
                                                  inspected, or
                                                  evaluated.

  Original-paper claims   **UNKNOWN /             Original publications
  independently verified  INCOMPLETE**            still need checking.

  Novelty of proposed gap **UNKNOWN**             No dedicated,
                                                  systematic novelty
                                                  search has been
                                                  completed.

  Experimental results    **UNKNOWN / NOT YET     No code execution or
                          GENERATED**             measured performance is
                                                  claimed.
  -----------------------------------------------------------------------

## 4. Decisions and Rationale

### D001 --- Use the attached review as the starting evidence base (**VERIFIED**)

Keep the project within citation integrity for AI-recommended
literature. Evidence: review Sections 1--3 and 5--7.

### D002 --- Separate relevance from citation integrity (**VERIFIED as a review framing**)

Semantic relevance does not prove that a source is safe or appropriate
to recommend. Evidence: review Sections 1, 2.1--2.3, and 5--6.

### D003 --- Narrow the initial scope to explicit retraction status (**INFERRED / working decision**)

Retraction is an observable publication-status event, while broader
outdatedness is less directly benchmarked and may require more
subjective labels. The first experiment should avoid overly broad
labels. Evidence: review Section 2.3 and Section 6.

### D004 --- Candidate gap: status-source provenance and disagreement (**INFERRED**)

Compare a single-source status check with provenance-aware
reconciliation across multiple sources. Evidence: review Sections 3.4
and 6. This is a candidate research direction, not a novelty claim.

### D005 --- Make no novelty claim before a dedicated search (**Project rule**)

The proposed gap must be checked against neighboring work. Verify
original papers, existing systems, datasets, and more recent research
before claiming that the gap is novel.

### D006 --- Do not claim implementation or experiments that have not occurred (**VERIFIED**)

The student clarified that no separate executable research
implementation exists. The next step is to inspect the available
repository, verify data access, and build a reproducible baseline.

## 5. Immediate Next Actions

1.  Verify the original papers on post-retraction citation behavior,
    status propagation, and AI tools citing retracted literature.
2.  Search neighboring work on status aggregation, provenance-aware
    reconciliation, timestamped status histories, and benchmarks.
3.  Check official data-provider access, terms of use, available fields,
    and rate limits.
4.  Define a labeled test set and an independent ground-truth protocol.
5.  Implement and test a single-source retraction-status baseline before
    adding multi-source reconciliation.
6.  Record actual commands, outputs, dependencies, code versions, and
    deviations. Do not report hypothetical metrics as experimental
    results.

## 6. Working Research Question

**Provisional and INFERRED:** On a fixed set of scholarly works with
independently verified retraction labels, how does provenance-aware
reconciliation of multiple status sources compare with a single-source
status check in detecting retracted works and handling missing or
conflicting records?

This question is provisional. It should be finalized only after data
access, provider coverage, and the availability of an independently
verified evaluation set have been checked.

## 7. Research Accountability

Maintain a decision log in which each important choice records its
status, rationale, evidence, unresolved uncertainty, and next
verification action. The log should distinguish the review's reported
claims from independently verified findings and proposed experiments. No
experimental result, performance metric, or novelty claim should be
presented until supported by actual evidence.
