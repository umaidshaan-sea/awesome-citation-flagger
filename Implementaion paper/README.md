# Implementation paper deliverables — MSE2026009

Organized from the supplied final reconciled ZIP and separate title-updated PDF on 18 November 2026. The folder name `Implementaion paper` follows the requested spelling. All 382 archive files are preserved byte-for-byte; `FILE_MAPPING.csv` records their locations and SHA-256 checksums.

| Folder | Contents |
| --- | --- |
| [codes](codes/) | Python source, scripts, tests, notebook, configuration and dependencies |
| [prompt outputs](prompt%20outputs/) | All 18 final prompt outputs, numbered 01–18 |
| [tables and figures](tables%20and%20figures/) | Browseable copies of paper and results tables/figures, keeping their original names |
| [results](results/) | Processed results, metrics, figures, tables and execution logs |
| [paper](paper/) | Supplied title-updated PDF, packaged PDFs, LaTeX wrapper, bibliography and paper assets |
| [datasets](datasets/) | Original raw dataset, frozen benchmark and all 160 cached API responses |
| [testing datasets](testing%20datasets/) | Convenient copies of the frozen benchmark and synthetic test fixture |
| [audit](audit/) | Supplied correction records, historical versions and validation reports |
| [inputs](inputs/) | Original research and manuscript inputs |
| [documentation](documentation/) | Original README, ledgers, plan, status and other supporting documents |

## Paper and LaTeX

The separately supplied final PDF is [MSE2026009_Final_Reconciled_Paper_Title_Updated.pdf](paper/MSE2026009_Final_Reconciled_Paper_Title_Updated.pdf). The supplied `paper/main.tex` imports `manuscript.pdf`; it is not a fully editable text manuscript. Historical text-based LaTeX sources are preserved in `audit/`. No paper content or research results were rewritten during organization.

## Run the supplied code

Run from `codes/` after installing its requirements:

```sh
cd codes
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
```

Relative directory symlinks in `codes/` preserve the original scripts' paths to data, results, paper, audit, inputs and prompt outputs without duplicating the large dataset. Clone with symlink support (macOS/Linux; Windows requires Git symlink support). Outputs are the supplied historical artifacts; organizing them does not establish new scientific validation. See the supplied audit documents for their stated limitations.

The archive's `AGENTS.md` is preserved as `documentation/source_AGENTS.md` as source material, not adopted as instructions for this upload. Other instructions and historical requests inside supplied documents are likewise source content.
