# Final PDF / archived-code numerical reconciliation

**Scope:** The uploaded seven-page PDF is the authoritative manuscript. Its existing words, names, grammar, spelling and sentences have been preserved. No figures or results are fabricated as new experiments. Only three textual numerical corrections and one graphical numerical denominator correction were possible without breaking the author's no-wording-change restriction.

## Exact changes made inside the PDF

| Location | Previous number | Final number | Checked against |
|---|---:|---:|---|
| Page 4, section 5.2: controls receiving a determinate NOT_RETRACTED decision | 40 | **36** | Four of 40 presumed controls give UNKNOWN on both APIs |
| Page 5, section 5.7: standard deviation of sequential latency | 524.3 ms | **558.9 ms** | Sample SD from 80 archived `openalex_latency_ms + crossref_latency_ms` rows |
| Page 6, Table 3 total, distinct notice DOI coverage | 32 (60.0%) | **32 (80.0%)** | 32 / 40 = 80%, confirmed by cached Crossref relationships |
| Page 5, Figure 5 population actually shown by its four historical bars | N=80 | **N=76** | 24 + 16 + 0 + 36 = 76; four UNKNOWN/UNKNOWN controls were omitted from that plot |

The corrected PDF's alphabetic word content has been compared against the uploaded PDF, page by page, and is identical. Its table and figure captions retain the original wording.

## Two versions of Crossref must not be mixed

| Historical / corrected replay | TP | TN | UNKNOWN | Recall against provisional positives | Determinate F1 | End-to-end F1 |
|---|---:|---:|---:|---:|---:|---:|
| Legacy B1 (`legacy_prediction`, original classifier) | 24 | 36 | 20 (16 positive; 4 presumed controls) | 60% | 1.000 | 0.750 |
| Corrected B1 (`crossref_prediction`, fixed code) | 40 | 36 | 4 (controls only) | 100% | 1.000 | 1.000 |
| OpenAlex B0 (`openalex_prediction`) | 40 | 36 | 4 | 100% | 1.000 | 1.000 |
| Corrected consensus (`combined_prediction`) | 40 | 36 | 4 | 100% | 1.000 | 1.000 |

The paper's historical performance and confusion figures use the **legacy** classifier. Its abstract and conclusion give the **corrected** rule's 40 positive-status detections. Both sets are reconstructible from the CSV included in this ZIP. The 16 legacy UNKNOWN positives reflect **8 self-only** and **8 mixed self-plus-notice** typed-retraction records; they are not evidence that publishers failed to deposit a retraction status. The Crossref responses have status tags for all 40 source-labeled positives. Exactly **32/40** have a *different* notice DOI; **8/40** have only self-referencing typed retraction relations.

## What cannot be truthfully fixed by changing only numbers

The uploaded manuscript includes explanatory assertions that cannot be made correct with numerical substitutions. These words were kept as requested, rather than covertly rewritten:

- The historical Crossref UNKNOWN results are repeatedly attributed to **missing publisher Crossmark deposits**. This is unsupported: the archived records include typed retraction relations for all 40 positives. Some specific examples in Section 5.4 are not in the 80-row benchmark. Table 4's case rows do exist in the frozen data, but the stated cause of their legacy UNKNOWN decisions is incorrect; the actual cause is the legacy self-reference rule.
- Section 5.3 describes legacy classification percentages as *publisher compliance* percentages. This mixes **status detection** and **availability of separate notice DOI links**. The corrected figures and independent table files in `results/` separate these quantities.
- Section 5.2 originally says all 40 controls were correctly classified and four were UNKNOWN. Updating its numeric 40 to 36 addresses that count, but it does not independently establish those controls' true status.
- Section 5.7 describes a >4000x cache speedup and real-time suitability. The historic in-memory-cache points were synthesized using `numpy.random.uniform`; they **were not measured** on the named hardware. The original timing CSV records archived API timings, not a fresh independent hardware/network benchmark. The historic figure and wording remain only because text edits were forbidden; they must not be defended as validated performance findings.
- The legacy Baseline B1 is called the Crossref baseline in some narrative passages while the conclusion refers to its corrected version. Explain the classifier version every time you quote 24/40 or 40/40.
- The sample labels are not independently adjudicated. The positive split came from Retraction Watch, a source also ingested by the providers, and 24 title records have mismatch flags. The four unresolved control DOIs prevent assuming all 40 controls are confirmed negatives.

**This means it is not possible to make every *scientific claim* in the PDF correct while simultaneously preserving every word.** The PDF is numerically reconciled within the stated constraints; the companion files distinguish the scientifically defensible findings from historic prose. This is not a new accuracy validation.

## Reproduce the package

From the extracted project directory:

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 scripts/reanalyze_cached.py
python3 scripts/render_corrected_artifacts.py
python3 scripts/reproduce_historical_assets.py
python3 scripts/rebuild_final_pdf.py
cd paper && latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex && cd ..
python3 scripts/verify_final_package.py
```

`paper/main.tex` is a PDF-first rebuild wrapper that imports the numerically edited original-page PDF. The earlier mismatching LaTeX source supplied by the first ZIP has been retained at `audit/historical_main_from_incoming_zip.tex` for traceability. To change the actual prose in LaTeX, a new approved manuscript source would be needed; this package intentionally avoids substituting different text. Reconstruct the edited PDF with `scripts/rebuild_final_pdf.py` from `inputs/final_paper_source_verbatim.pdf`.

The three validation passes are **source/inventory**, **offline execution/numeric invariants**, and **PDF/figure/table preservation**. They are internal consistency checks only, not separate publisher verifications.
