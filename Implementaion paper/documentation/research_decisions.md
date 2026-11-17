# Scientific Decision Log — Corrective Audit

| Decision | Rationale | Evidence |
|---|---|---|
| D-A01: Preserve frozen 80 DOI strings | Avoid retrospectively improving the selected benchmark | `data/splits/benchmark_80_frozen.csv` |
| D-A02: Reinterpret Crossref self-DOI typed retractions as positive | The relation contains explicit type `retraction`; notice-link ability is a separate property | 160 cached JSON records; `src/core.py` |
| D-A03: Separate status vs distinct notice fields | Avoid equating missing notice link with missing retraction flag | `results/processed/benchmark_results.csv` |
| D-A04: Report only benchmark-label agreement | Positive labels and tools share Retraction Watch; negatives unadjudicated | `results/processed/title_audit.csv`, source docs |
| D-A05: Exclude synthetic latency and exaggerated significance | No independently measured warm cache data, no method discordance | Legacy generator in `audit/original_scripts/` |
| D-A06: Declare post-hoc change | Correction made after seeing legacy outcome | `configs/analysis_amendment_2026-11-17.yaml` |
