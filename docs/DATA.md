# Data dictionary and complete research archive

## Data in the repository

| File | Contents / key |
|---|---|
| `data/development.jsonl` | 4,726 reading-step rows from 688 passages / 344 families. |
| `data/comparison.jsonl` | 910 steps from 100 passages / 50 families; the later reused comparison set. |
| `data/comparison-corpus.jsonl` | One source-text record per comparison passage. |
| `data/train.npz` | 4,726 × 302 feature matrix, targets, family weights and row IDs. |
| `data/comparison-features.npz` | 910 × 302 feature matrix, weights and IDs; intentionally has no `y` array. |
| `data/features.json` | Ordered feature names, compact/expanded indices and feature policy. |
| `data/folds.json` | Five grouped development folds; no family crosses training and validation within a fold. |
| `data/round3-final-predictions.csv` | 9,056 rows: 16 models × 566 steps; do not count models as additional samples. |
| `data/round4-final-predictions.jsonl` | 12,712 rows: 14 models × 908 steps; same caution. |
| `results/` | Original reports, predictions, diagnostics and machine-readable results. |
| `models/` | Exact numerical exports; see the equation guide. |

`id` identifies a passage within its stage. `family` identifies a related pair and the resampling/split unit. `segment_id` identifies a reading step. Join on `(id, segment_id)` within a stage, and include `model` for long-form model comparisons. Do not merge stages using a segment ID alone.

`passage` is the complete source text. `start` and `end` are UTF-16 code-unit offsets; `segment_text` is the scored span. `target` is the middle of three reference scores; `repeat_targets` preserves all three. `prediction` is the whole-number model score. A `raw_prediction` or `pre_round_prediction` can differ and is defined by that model's output rule. The target units are app-score units, not seconds, bits, or a validated biological memory unit.

`provisional` means at least one repeat marked the score tentative. `coverage_limited` includes passage-level coverage warnings or absence of an explicit all-clear flag. `inconsistent` records unequal repeated targets. `source`, `domain`, `genre`, `length_band`, and `primary_challenge` describe constructed examples; they are not human measurements. Some earlier stages use additional fields documented in their protocols.

## Download all saved research records

Each archive extracts under `research/`. Download all seven into `downloads/`, check them, then extract into the same directory. They do not overwrite one another's study files. The internal `MANIFEST.json` documents that archive separately; inspect it within its ZIP before extracting multiple archives, since that manifest filename is shared.

```sh
gh release download research-data-v1 --repo AustinAWay/Equation-From-Jev-Research --dir downloads
python scripts/verify_archives.py downloads --members
```

| Archive | Download size | Included files | Raw JSON files* |
|---|---:|---:|---:|
| [research-round1.zip](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/download/research-data-v1/research-round1.zip) | 188.8 MB | 4,122 | 360 |
| [research-round2.zip](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/download/research-data-v1/research-round2.zip) | 28.4 MB | 371 | 144 |
| [research-round3.zip](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/download/research-data-v1/research-round3.zip) | 371.4 MB | 3,357 | 1,800 |
| [research-round4.zip](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/download/research-data-v1/research-round4.zip) | 1099.4 MB | 3,026 | 1,800 |
| [research-fresh100.zip](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/download/research-data-v1/research-fresh100.zip) | 47.4 MB | 363 | 300 |
| [research-direct-nonlinear.zip](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/download/research-data-v1/research-direct-nonlinear.zip) | 2.4 MB | 87 | 0 |
| [research-autopilot.zip](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/download/research-data-v1/research-autopilot.zip) | 45.5 MB | 603 | 0 |

The archives contain **11,929 files**, about **12.43 GB** before compression and **1.78 GB** to download. SHA-256 checksums are recorded in [release-manifest.json](../provenance/release-manifest.json) and the release's `SHA256SUMS` file.

*Raw-file counts include preserved copies and recovery snapshots. They are **not counts of independent analyses**; use record IDs, repeat numbers, provenance hashes and the collection ledgers to deduplicate. Earlier final-test passages become later development material, so summing stage sample sizes also double counts passages.

## Where to find the underlying data

- **Round 1:** `research/work/equation-research/data/raw/`, corpus partitions and the complete candidate search. The frozen original app is under `research/work/repo-angle-review/`.
- **Round 2:** `research/work/round2/fresh/`; approach-specific numerical equations, raw references, collision diagnostics and predictions remain together.
- **Round 3:** `research/work/round3/`; development expansion, final holdout, repeatability studies, cap diagnostics, all saved candidates and audits.
- **Round 4:** `research/work/round4/reference/`; original, recovery and merged transport records are preserved. The final admitted reference directory is `reference/final-transport/data/`. The portable historical checker is `package/bundle-final/`.
- **Further fresh test:** `research/work/fresh100-20260924/reference/raw/`; 300 analyses for 100 passages, plus ledgers and transport amendments.
- **Direct and nonlinear:** `research/work/direct-text-equation-20260924/` and `research/work/nonlinear-text-equation-20260924/`, with their `research/outputs/` results. These reused saved references and made no new Jev calls.
- **Autopilot:** the saved autonomous development search, its 181 completed attempts, stopping status, selected candidate and smoke checks. These are development results only.

Raw analysis JSON normally contains a passage `record`, a `repeat` number, collection time, provenance hash, complete `analysis`, saved `scores` and sometimes transport metadata. Budget events include failures and reserved unknown usage; they are not all successful calls. JSON/JSONL schemas evolve across rounds; preserve each directory's metadata with its rows.

## Coverage and exclusions

This is the equation study's local research record as found for publication. Separate education-index and literature-review projects are outside its scope. [archive-exclusions.json](../provenance/archive-exclusions.json) identifies 631 excluded files and their original hashes: nested ZIPs, serialized fitting/cache objects and presentation media. Installed environments, `.git`, bytecode, cache directories and housekeeping files are omitted. Small explicitly vendored source snapshots retain their own notices.

All eligible raw JSON, text corpora, numerical JSON equations, predictions, failed-request records and search logs in the inventoried study folders are included. Duplicate numeric/source copies remain where they document a historical package or recovery path. Each source file's bytes were checked during packaging. Retained local paths in original scripts are historical provenance, not portable execution instructions.
