# Evaluation / Viva explanation sheet

## 30-second overview

> My project checks scholarly article retraction metadata before an AI system uses a
> citation. I compare OpenAlex's Boolean retraction status with Crossref's typed
> retraction updates, and I distinguish a retraction warning from having a separate
> notice DOI. I audited 80 frozen DOIs using archived API responses. The original code
> had wrongly called 16 Crossref retraction records UNKNOWN because their update
> entries included the original article DOI. After fixing that rule, Crossref,
> OpenAlex and their combined method all flag the 40 benchmark positives, and only
> 32 have a separate notice DOI. I report this as selected-label agreement, not as
> independently confirmed real-world accuracy.

## Key numbers to memorize

| Observation | Value | Meaning |
|---|---:|---|
| Frozen DOIs | 80 | 40 RW-listed positives, 40 presumed controls |
| OpenAlex positive-label matches | 40/40 | Status flag, no separate notice evidence |
| Crossref corrected positive-label matches | 40/40 | Typed status even if update DOI = original DOI |
| Combined positive-label matches | 40/40 | Equal to both corrected baselines; no detection advantage |
| Crossref separate notice DOI | 32/40 = **80%** | Link differs from article DOI |
| Crossref self-only retraction status | 8/40 = **20%** | Still explicitly flagged as retracted |
| Both APIs return 404 for controls | 4/40 | UNKNOWN, not true negatives |
| Frozen title mismatches | 24 total: 1 positive, 23 controls | Strong class imbalance; review required |
| Unit tests | 21 passing | Eight added regression/archived-invariant tests in total |

## Likely examiner questions

**Q: Why did your old Crossref baseline get only 60% recall?**  
A: The precise bug was precedence of an `ambiguous` flag: if **any** same-DOI retraction entry was present, it returned UNKNOWN even if a distinct notice also appeared. Exactly 8 positive cases were self-only and 8 mixed. A simple separate-notice-required rule would have detected 32/40 rather than the observed 24/40. The archive actually has typed retraction
metadata for all 40 positives.

**Q: What is your contribution if the combined approach does not beat Crossref?**  
A: A reproducible metadata-quality audit, safe tri-state handling and a clear
separation of status signals from separately linkable notice evidence. I am not
claiming a novel machine-learning architecture or significant recall improvement.

**Q: Why is 100% recall not proof your model is perfect?**  
A: The positives were selected from Retraction Watch, which both data providers
use. The controls were not fully independently adjudicated, so data leakage and
selection bias can inflate scores. These are nominal benchmark-label results.

**Q: What does UNKNOWN mean?**  
A: An API cannot provide enough information (e.g., 404), or there is a status
conflict such as reinstatement that needs manual review. UNKNOWN is *never*
equivalent to NOT_RETRACTED.

**Q: What's the difference between 40 status signals and 32 notices?**  
A: A `retraction` relation whose DOI is the original article establishes a typed
status but cannot link to a separate retraction notice. For 32 records we found
a different retraction DOI within the archived Crossref relations.

**Q: Can Crossref and OpenAlex independently verify each other?**  
A: Not in this setup. Both ingest Retraction Watch material and the positives
came from that very dataset. Source agreement is partly circular.

**Q: What would you do next for a publishable study?**  
A: Independently check each DOI against publisher notices, correct title/DOI
mismatches, create a new pre-registered held-out split, capture timestamped live
API results and compare sensitivity and error types again.

## Demonstrate the work live (offline)

```bash
python3 -m unittest discover -s tests -v
python3 scripts/reanalyze_cached.py
python3 scripts/render_corrected_artifacts.py
```

Inspect `results/processed/benchmark_results.csv` for individual evidence traces,
`results/processed/title_audit.csv` for questionable items and
`results/processed/audit_statistics.json` for count assertions. **Do not** say that
independent publisher adjudication or new live API queries were performed here.

## Additional viva questions

**Q: What does F1 determinate measure?**
A: It excludes UNKNOWN decisions. For the legacy classifier it was 1.000, but operational end-to-end F1 fell to 0.750 after penalizing 16 positive abstentions. Reporting 60/80 decision coverage (75%) makes missing decisions visible.

**Q: Why are the controls a problem?**
A: 23/40 control titles have a substantial cached DOI-title mismatch, versus 1/40 positives; another four controls return 404. The presumed negatives were not independently adjudicated, so those records cannot establish specificity.

**Q: Were your checks independent validation?**
A: No. The three passes check source bytes, code consistency and PDF integrity internally. They are not independent publisher-status adjudications.

**Q: Did you verify all 80 records using current APIs?**
A: No. Live retrieval was attempted but blocked in this environment. The package includes an optional script and 48-case manual priority queue for a later separate verification.

**Q: What is the original CSV SHA-256?**
A: `e5351ee51ab3f1da7fe98b3bd6c5c58049b8bff4705949ef6fd4f1a1315dd0ea`.
