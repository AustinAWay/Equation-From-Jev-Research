# Equations from Jev research

**Can a locally computed equation reproduce the scores of a Jev-based text analysis app?**

This repository documents an exploratory attempt by [AustinAWay](https://github.com/AustinAWay) to answer that question. The reference is the fixed **Working-Memory-Jev / Passage app procedure**, including its prompts, reader profile, candidate limits and score calculation. It is not a direct measurement of a person's working memory, and it is not simply a raw number returned by the Jev API.

**Result: none of the tested equations met the original target of 95% exact agreement and at most 0.10 units of unrounded error.** A larger component model reached 47.7% and 47.3% on two different fresh tests. Later, more directly expressed equations reached 42.0–43.4% on a reused comparison set, while a flexible equation using only word count reached 42.5%. The research produced reproducible approximations and a record of failures, not a validated cognitive-load formula.

## Start here

- [Results and interpretation](docs/RESULTS.md): what worked, what failed, and which tests were fresh.
- [Methods and limitations](docs/METHODS.md): target definition, family weighting, repeated references, selection and uncertainty.
- [Equations explained](docs/EQUATIONS.md): the compact notation and the full fitted parameters it represents.
- [Reproduce the results or score text](docs/REPRODUCING.md).
- [Data dictionary and complete archive](docs/DATA.md).
- [Publication review](docs/REVIEW.md): checks performed for this release and their limits.

## The final direct-equation comparison

All entries below use the **same 100 passages, 910 reading steps and 50 paired families**. Agreement is averaged equally across families. This set was already examined in earlier work; these later comparisons are exploratory, even though its labels were excluded from fitting and model selection.

| Equation / control | Exact agreement | Mean absolute error |
|---|---:|---:|
| Gaussian equation, selected using development folds | 42.0% | 0.754 |
| Direct logistic equation, selected linear specification | 42.3% | 0.746 |
| Cubic spline equation | 43.4% | 0.746 |
| **Flexible word-count-only equation** | **42.5%** | **0.711** |
| Earlier 32-term arithmetic equation | 39.1% | 0.715 |
| Earlier larger component model | 47.3% | 0.634 |
| Always return 2 | 34.4% | 0.927 |

The 43.4% spline result is the highest observed among the three later full-text equation types. **The Gaussian equation was the winner selected before comparison**, at 42.0%. Choosing the spline after seeing this table would require a new test. The constant baseline is not random guessing. The spline's advantage over that baseline is about **8.9 percentage points**, not 8.9% relative improvement.

The development set contained **688 passages, 4,726 steps and 344 families**. Each reference target is the median of three saved app analyses. These are synthetic English educational challenge passages with a fixed grade-six reader profile. There are no student outcomes or human memory measurements.

## Run a reproducibility check

Python 3.9.6 was used for the recorded release check. Start from the repository root:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/verify_results.py
```

This reproduces the comparison table and all **4,550 predictions from five compact equations** using saved measurements, without Jev access. To regenerate the measurements from raw text, install the pinned parser model and add `--features`; see [full instructions](docs/REPRODUCING.md).

## Data and research record

The repository includes development and comparison rows, saved measurement matrices, exact parameters, readable reports, and verification tools. The [research-data-v2 release](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/tag/research-data-v2) contains the larger research records: raw app responses, repeated analyses, unsuccessful requests, candidate searches, rejected equations, source snapshots, protocols, audits and accounting.

The [archive index](provenance/release-manifest.json) identifies each download and its SHA-256 checksum. Exclusions are recorded explicitly: redundant nested archives, installed environments, serialized training/cache files and presentation media. Numerical JSON equations and collected reference data remain included. Personal machine paths and unnecessary operational wording are sanitized, with original and published hashes recorded. Old reports and raw records are historical evidence; the navigation and qualifications in this README and `docs/` describe this publication.

## What would improve the evidence?

Freeze a specific revised equation and a strong length-only control, then test them on an independently sourced corpus that has not influenced development. Use matched examples to challenge claims about order and reference tracking. A claim about human working memory would additionally require appropriate human measurements. Neither a good app fit nor a failed search settles that question.

See [rights and source provenance](docs/RIGHTS.md). No Jev model weights or credentials are included.
