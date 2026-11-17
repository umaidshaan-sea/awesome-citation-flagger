# Prompt 02 — Research gap and evidence map

**Updated:** 17 November 2026 | **Status:** evidence-limited corrective deliverable, not independently verified publisher truth.

**SAVE:** Differentiation of status detection, independently validated truth, and separate notice-link provenance.

| Prior source or behavior | Supported finding | Unresolved gap addressed here |
|---|---|---|
| Crossref 2025 integration notice | Crossref REST can include Retraction Watch retraction signals and publisher source labels | A self-DOI typed retraction must not be discarded as missing status |
| OpenAlex works schema | `is_retracted` may draw on Retraction Watch, Crossref, PubMed and title cues | Provider agreement is not an independent second opinion |
| Original pipeline | One status boolean and one notice field conflated | Separate status from distinct notice link and unknown status |
| Frozen course benchmark | 40 RW positive labels and 40 presumed negative controls | Independently adjudicated control labels and publisher notices absent |

**Finding:** A comparative reanalysis can demonstrate a correct software distinction, but the available evidence cannot support a novel algorithm that improves true status recall over the best corrected source.

**Cross-reference:** `audit/CORRECTIONS_AND_LIMITATIONS.md` and `configs/analysis_amendment_2026-11-17.yaml`. Historical superseded versions of this prompt file remain at `audit/original_prompt_outputs/02_gap_matrix.md`.
