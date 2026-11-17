# AI Tools for Research --- Lab Assignment 02

## Prompt 02: Evidence-Based Research Gap Matrix

**Student:** Md Umaid Shaan\
**Date:** 21 October 2026\
**Project:** *An Automated Pipeline for Flagging Outdated Citations in
AI-Recommended Literature*

## 1. Evidence Boundary

This gap analysis is based on the submitted 12-page literature review
PDF. The evidence locations below describe what the review reports; they
do not independently verify every original publication. Proposed gaps,
research questions, and experiments are **INFERRED**. The novelty of
every candidate gap remains **UNKNOWN** until a dedicated search of
related work, systems, and datasets has been completed.

## 2. Candidate Research Gaps

### G1. Provenance-Aware Reconciliation of Retraction-Status Sources

**Evidence and location:** Review Section 2.3, page 3; Section 3.4, page
4; Section 6, pages 8--9; references \[6\] and \[7\]. The review reports
inconsistent or incomplete propagation of retraction information and
motivates provenance, timestamps, and conflict handling.

**Interpretation:** The review-reported limitation is that status
records may be inconsistent or incompletely propagated. The **INFERRED**
candidate gap is to quantify whether multi-source reconciliation
improves on a single-source check. The review does not prove that no
prior comparison exists.

**Research question:** On a fixed, independently labeled set, how does
provenance-aware reconciliation compare with a single-source check when
providers disagree or return no status?

**Possible experiment:** Compare a one-source baseline with a
multi-source reconciliation method. Measure precision, recall,
false-negative rate, unresolved-status rate, source-disagreement rate,
and lookup latency. Adjudicate conflicts and preserve source evidence.

**Verification risks:** Verify the original papers and provider access.
Majority vote is not automatically ground truth. Novelty remains
**UNKNOWN**.

### G2. Temporal Evaluation: Status at Recommendation Time Versus Current Status

**Evidence and location:** Review Section 2.3, page 3; Section 3.4, page
4; Sections 6.1--6.2, pages 8--9.

**Interpretation:** The review identifies status changes over time and
temporal evaluation as challenges. The **INFERRED** candidate gap is to
compare time-aware decisions with decisions based only on a current
snapshot.

**Research question:** When retraction happens after an earlier
recommendation, does a time-aware checker classify historical status
more accurately than a current-snapshot checker?

**Possible experiment:** Use records with reliable event dates and, if
possible, historical snapshots. Evaluate status-as-of-time and current
status separately; report temporal errors and unresolved historical
cases.

**Verification risks:** Historical snapshots may be unavailable, and
current API responses may not support retrospective evaluation. Novelty
remains **UNKNOWN**.

### G3. Combining Retraction Status with Citation Intent and Context

**Evidence and location:** Review Section 2.2, page 2; Section 3.2,
pages 3--4; references \[4\] and \[12\].

**Interpretation:** The review's conceptual discussion indicates that
the same retracted paper may be mentioned critically or historically, or
used as current evidence. The **INFERRED** candidate gap is to measure
whether context helps reduce false alarms without concealing a retracted
status.

**Research question:** Does citation intent or context help distinguish
historical or critical mentions from risky positive use better than
status-only flagging?

**Possible experiment:** Compare status-only detection with
status-plus-context analysis on a manually annotated citation-context
set. Report class-wise precision and recall, along with representative
false positives and false negatives. Keep the fact of retraction
separate from the assessment of how the paper is used.

**Verification risks:** This requires context data and annotation
guidelines. Intent labels do not prove that a citation factually
supports a claim. Verify the suitability and access conditions of any
intended citation-intent dataset, including SciCite. Novelty remains
**UNKNOWN**.

### G4. Evidence-Grounded Explanations for Flags

**Evidence and location:** Review Section 6.4, pages 8--9; Sections
5--6.

**Interpretation:** The review identifies a need for transparent
explanations. The **INFERRED** candidate gap is to compare structured,
evidence-linked explanations with free-form explanations for
traceability and completeness.

**Research question:** Do evidence-linked template explanations provide
more verifiable reasons for retraction flags than free-form
explanations?

**Possible experiment:** Generate explanations from status, source,
event date, identifier, and retrieval timestamp. Ask human reviewers to
score traceability, completeness, and unsupported claims using a
predefined rubric.

**Verification risks:** This requires a clear evaluation rubric and
human review. Novelty remains **UNKNOWN**.

### G5. End-to-End Pipeline Ablation and Failure Analysis

**Evidence and location:** Review Section 4 and Table 1, page 6; Section
6, pages 8--9; Section 7, pages 9--10.

**Interpretation:** The review reports that conventional recommenders
focus on relevance and identifies limited end-to-end evaluation. The
**INFERRED** candidate gap is to isolate the contributions of identifier
resolution, status lookup, and conflict handling.

**Research question:** Which stages contribute most to reliable
retraction-status identification, and what failure types remain after
each stage is added?

**Possible experiment:** Compare an identifier-to-single-source checker
with versions that add identifier normalization and multi-source
reconciliation. Measure resolution failures, status errors, unresolved
cases, and runtime; include qualitative failure analysis.

**Verification risks:** This requires a functioning baseline and an
evaluation dataset. Do not claim recommendation quality if the system
only audits publication status. Novelty remains **UNKNOWN**.

## 3. Provisional Ranking of the Three Leading Gaps

  --------------------------------------------------------------------------------
  Rank           Candidate gap      Significance   Feasibility      Rationale and
                                                                    caveat
  -------------- ------------------ -------------- ---------------- --------------
  1              **G1 ---           High practical Moderate,        Narrow and
                 Provenance-aware   relevance      conditional on   measurable;
                 status                            provider access  novelty still
                 reconciliation**                  and a small      needs a
                                                   independently    dedicated
                                                   verified set     search.

  2              **G2 --- Temporal  High           Low to moderate  Strong
                 evaluation**                      if historical    conceptual
                                                   snapshots are    fit, but data
                                                   difficult to     availability
                                                   obtain           is the main
                                                                    risk.

  3              **G3 --- Status    High           Moderate to low  A useful
                 plus citation                     for a first      extension
                 intent/context**                  implementation   after status
                                                   because          detection;
                                                   annotation adds  intent cannot
                                                   complexity       replace
                                                                    explicit
                                                                    status
                                                                    evidence.
  --------------------------------------------------------------------------------

This ranking is a provisional feasibility assessment, not a novelty
ranking. G4 is best treated as a downstream usability evaluation; G5 is
an evaluation design that can be applied to the selected pipeline.

## 4. Provisional Recommendation and Primary Research Question

**INFERRED recommendation:** Build a transparent single-source
retraction-status checker, then compare it with provenance-aware
reconciliation across two or more status sources, provided access and
terms of use are verified. Treat the single-source checker as the
baseline and reconciliation as the proposed modification. Represent
unresolved or conflicting status explicitly.

**Primary research question:**

> On a fixed set of scholarly works with independently verified
> retraction labels, how does provenance-aware reconciliation of
> multiple status sources compare with a single-source status check in
> detecting retracted works and handling missing or conflicting records?

## 5. Candidate Measurements

-   **Precision and recall** for retracted-work detection.
-   **False-negative rate** for retracted works.
-   **Unresolved-status rate.**
-   **Source-disagreement rate.**
-   **Identifier-resolution failure rate.**
-   **Lookup latency**, with test conditions documented.

No numeric success threshold is set because the dataset, provider
coverage, and baseline behavior are not yet known. Define the decision
rule before examining final test results. No metrics have been measured
at this stage.

## 6. Original References to Verify First

The following bibliographic details are reproduced from the submitted
review and must be checked against the original publications before they
are relied on as verified evidence.

1.  **Bar-Ilan, J. & Halevi, G. (2017).** "Post retraction citations in
    context: a case study." *Scientometrics*, 113, 547--565. DOI:
    [10.1007/s11192-017-2242-0](https://doi.org/10.1007/s11192-017-2242-0).
    Review reference \[2\].
2.  **Candal-Pedreira, C. et al. (2020).** "Does retraction after
    misconduct have an impact on citations? A pre--post study." *BMJ
    Global Health*, 5(11), e003719. DOI:
    [10.1136/bmjgh-2020-003719](https://doi.org/10.1136/bmjgh-2020-003719).
    Review reference \[3\].
3.  **Cohan, A. et al. (2019).** "Structural scaffolds for citation
    intent classification in scientific publications." *NAACL-HLT 2019*,
    3586--3596. DOI:
    [10.18653/v1/N19-1361](https://doi.org/10.18653/v1/N19-1361). Review
    reference \[4\].
4.  **Färber, M. & Jatowt, A. (2020).** "Citation recommendation:
    approaches and datasets." *International Journal on Digital
    Libraries*, 21(2), 375--405. DOI:
    [10.1007/s00799-020-00288-2](https://doi.org/10.1007/s00799-020-00288-2).
    Review reference \[5\].
5.  **Frampton, G., Woods, L. & Scott, D. A. (2021).** "Inconsistent and
    incomplete retraction of published research." *PLOS ONE*, 16(10),
    e0258935. DOI:
    [10.1371/journal.pone.0258935](https://doi.org/10.1371/journal.pone.0258935).
    Review reference \[6\].
6.  **Labenbacher, S. et al. (2026).** "Performance of AI tools in
    citing retracted literature: content analysis." *Journal of Medical
    Internet Research*, 28, e88766. DOI:
    [10.2196/88766](https://doi.org/10.2196/88766). Review reference
    \[13\].

## 7. Verification Checklist Before Coding

-   [ ] Open each selected original paper and confirm its bibliographic
    metadata.
-   [ ] Check whether its findings support the exact claim attributed to
    it in the review.
-   [ ] Search for existing systems and benchmarks on status
    aggregation, cross-provider conflicts, and provenance.
-   [ ] Verify provider endpoints, available fields, rate limits, terms
    of use, and status-history availability.
-   [ ] Define independent ground truth and adjudication rules before
    evaluating providers.
-   [ ] Record data access, code version, commands, and genuine outputs;
    do not report results until runs have occurred.

## 8. Limitations and Evidence Status

The gap matrix is a structured set of candidate directions derived from
the submitted review, not proof that these gaps are novel. The first
candidate, provenance-aware reconciliation, is recommended because it
can be expressed as a measurable comparison, but it depends on access to
suitable status sources and an independently verified test set. If these
prerequisites are not met, the scope or experiment must be revised and
the reason documented.
