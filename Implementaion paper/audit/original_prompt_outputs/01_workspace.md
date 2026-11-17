# Prompt 01 Output: Accountable Research Workspace and Decision Log

> **Provenance Notice:** Imported prior work from student submission `ATR_MSE2026009.pdf` (pages 1–4) and `Prompt_01_Research_Workspace.md`, dated 21 October 2026. Labeled as imported prior student work, audited and structured for autonomous project execution.

---

## 1. Official Handbook Prompt Specification
- **Prompt:** Setup an accountable research workspace
- **Official SAVE Deliverable:** Workspace and decision log; review scope.
- **Evidence Status:** VERIFIED (imported from inspected PDF and markdown transcripts).
- **Substantive Artifact Links:**
  - Base Literature Review: [MSE_09_Umaid-1.pdf](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/inputs/MSE_09_Umaid-1.pdf)
  - Prior Work Transcript: [ATR_MSE2026009.pdf](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/inputs/ATR_MSE2026009.pdf)
  - Research Decisions Log: [research_decisions.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/research_decisions.md)
  - Operating Guidelines: [AGENTS.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/AGENTS.md)
  - Execution Plan: [PLAN.md](file:///Users/umaid/.gemini/antigravity/scratch/citation_retraction_study/PLAN.md)

---

## 2. Research Scope Summary

The submitted 12-page literature review examines whether scholarly publications recommended by AI literature discovery and citation recommendation tools remain academically and empirically valid to cite at the time of recommendation. It critically distinguishes between *topical or semantic relevance* and *scholarly status validity*.

The review synthesizes literature across five core interconnected themes:
1. **Citation Recommendation and Ranking:** Approaches progressing from early bibliographic coupling and co-citation analysis toward contextual, graph-based (GNNs), and deep transformer embeddings.
2. **Citation Context, Intent, and Framing:** The functional semantic role a citation plays (e.g., background, method, comparative critique) and whether downstream citations adopt the cited findings unreservedly.
3. **Retraction and Broader Outdatedness:** Typology of academic invalidation, spanning formal retraction notices, expressions of concern, errata/corrections, version supersession, and substantive empirical obsolescence.
4. **Persistence of Citations to Retracted Work:** Sociological and technical phenomena where retracted studies continue to accumulate uncritical citations due to fragmented status dissemination across discovery platforms.
5. **AI-Era Citation Integrity:** Emerging risks where Large Language Models (LLMs) and retrieval-augmented generation (RAG) pipelines ingest outdated or retracted studies without provenance verification, propagating scientific errors into newly drafted literature.

---

## 3. Accountable Research Workspace Structure
The project workspace is established at `/Users/umaid/.gemini/antigravity/scratch/citation_retraction_study` with standardized subdirectories:
```
citation_retraction_study/
├── AGENTS.md                 # Persistent instructions & auditing rules
├── PLAN.md                   # Milestone execution plan (Prompts 01–18, Gates G1–G4)
├── STATUS.md                 # Real-time progress and telemetry
├── research_decisions.md     # Sequential decision registry (D001–D015)
├── source_ledger.csv         # Verified primary bibliography and API sources
├── evidence_ledger.csv       # Epistemic claim tracking
├── artifact_manifest.csv     # Cryptographic hashes of all deliverables
├── deviations.md             # Formal log of scope refinements
├── ai_assistance_log.md      # Human-AI collaboration provenance
├── inputs/                   # Immutable copies of base review & student records
├── prompt_outputs/           # Official deliverable files for Prompts 01–18
├── src/                      # Audited Python source code modules
├── tests/                    # Deterministic unit and edge-case test suites
├── scripts/                  # Data downloading, validation, and evaluation runners
├── configs/                  # Frozen experimental protocol YAML
├── data/                     # Raw, processed, and split dataset artifacts
├── notebooks/                # Secondary replication Jupyter notebooks
├── results/                  # Raw logs, processed metrics CSV, and publication figures
└── paper/                    # 6–10-page LaTeX manuscript, BibTeX, and compiled PDF
```

---

## 4. Epistemic Conventions & Baseline Decision Log Summary
The workspace strictly implements a three-state epistemic labeling convention:
- **`VERIFIED`:** Directly supported by an inspected source document, official API response, or reproducible terminal execution output.
- **`INFERRED`:** A reasoned hypothesis or architectural derivation awaiting experimental corroboration.
- **`UNKNOWN`:** Missing, unmeasured, or unresolved evidence.

**Initial Decisions Logged:**
- `D001 (VERIFIED)`: Ingest submitted 12-page review as project boundary.
- `D002 (VERIFIED)`: Distinguish review's synthesis claims from field-wide novelty until empirically audited.
- `D003 (VERIFIED)`: Narrow operational scope of experimental study to formal retraction events.
- `D004 (VERIFIED)`: Select single-source baselines B0 (OpenAlex) and B1 (Crossref) for comparative benchmarking against proposed multi-source pipeline.
- `D005 (VERIFIED)`: Treat unresolved API lookups as `UNKNOWN` rather than `NOT_RETRACTED`.

---

## 5. Actual Outcome
- Accountable workspace directory tree initialized.
- Governance documents (`AGENTS.md`, `PLAN.md`, `STATUS.md`, `research_decisions.md`, `source_ledger.csv`, `evidence_ledger.csv`, `artifact_manifest.csv`) created and populated.
- Base literature review scope transcribed and verified.
- **Official SAVE Deliverable:** Workspace and decision log; review scope successfully recorded.
