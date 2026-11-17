# External status and manual adjudication — not completed

- **Archived API capture:** 4 November 2026. Original 80 Crossref + 80 OpenAlex JSON files are kept in `data/processed/api_cache/`.
- **Reanalysis:** offline replay of those archived files. 40/40 source-labeled positives show typed Crossref retraction relations. This is *label agreement*, not externally established detection accuracy.
- **Live API:** attempted in this ChatGPT environment on 17 November 2026, but outbound container networking failed at DNS resolution, and direct API URLs were inaccessible through the browser retrieval tool. **No refreshed API dataset was produced.**
- **Executable live check:** `python3 scripts/live_api_spotcheck.py` checks 8 self-only positives and four historical controls; `--all` checks all 80. Run on a network-connected machine or Colab. Its output is a *new* timestamped folder under `results/live/` and never replaces frozen records.
- **Independent manual assessment:** none of the 80 cases was independently adjudicated against verified publisher notices in this revision. `audit/independent_adjudication_queue.csv` prioritizes all 40 controls and the 8 self-only cases (48 rows). Its status is PENDING, not VERIFIED.
- **Crossref publisher statements and article landing pages:** these can provide additional evidence but should be recorded with the reviewer name, timestamp, direct URL, claimed status, and whether the notice is the original paper's DOI or a separate document.
- **External bibliography spot checks:** verified the official Crossref 29 January 2025 blog publication date, 27 October 2021 publication of Frampton et al. in PLOS ONE, and 2019 NAACL citation for Cohan et al. These checks do not validate benchmark articles.
