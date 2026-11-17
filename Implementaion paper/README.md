# Citation retraction classifier

Offline reproduction of retraction classification using the frozen 80-DOI benchmark and 160 cached Crossref/OpenAlex responses from 4 November 2026.

## Run

Python 3.10+ is required. From this folder:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r codes/requirements.txt
cd codes
python3 scripts/reanalyze_cached.py
python3 scripts/render_corrected_artifacts.py
python3 -m unittest discover -s tests -v
```

The replay writes CSV/JSON outputs to `results/processed/`. The rendering step writes five PDF/PNG figure pairs and five LaTeX tables to `results/figures/` and `results/tables/`. No API access or full raw Retraction Watch download is required.

## Files

- `codes/src/`: DOI normalization, classifiers, metrics, data validation and the previous classifier used for the diagnostic comparison.
- `codes/scripts/`: benchmark replay and figure/table generation.
- `codes/tests/`: rule, input-validation and frozen-benchmark regression tests.
- `datasets/`: frozen benchmark and cached API evidence.
- `results/`: reproducible metrics, evidence, figures and tables.

The `codes/data` and `codes/results` relative symlinks preserve script paths. Clone with symlink support, available by default on macOS/Linux.

## Interpretation and provenance

Crossref retraction status and a distinct notice DOI are separate signals. The current classifier accepts a typed retraction even when its DOI equals the article DOI. The previous rule rejected some such records; its diagnostic comparison remains in the outputs. The current frozen-sample results are 40 detected positives, 36 negative controls and 4 unknown controls for each method, with 32 distinct notice links among the 40 positives.

These results are agreement with provisional benchmark labels, not independently adjudicated population accuracy. Retraction Watch, Crossref and OpenAlex share data sources. Title mismatches and unresolved controls remain in the outputs. Figure/table generation reproduces this fixed benchmark; its summary annotations are specific to these 80 records.

This is a reduced runtime distribution of the supplied research package, which included AI-assisted development records and later result corrections. The complete supplied provenance and manuscript materials remain available in repository commit `d4805fa1b1264b366638db981ee6d618169f4866`. This cleanup changes packaging, not authorship or the underlying evidence.
