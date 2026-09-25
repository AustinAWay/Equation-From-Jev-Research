# Reproduce the release

No API key or paid reference call is required for any command below. These checks replay saved results; they do not create new evidence of predictive validity.

## Environment

From the repository root, use the Python environment described in the README. The recorded publication replay used Python 3.9.6, NumPy 2.0.2, SciPy 1.13.1, spaCy 3.8.11, en_core_web_sm 3.8.0 and wordfreq 3.1.1. Exact historical environment records are in `provenance/original-environment.txt`; the smaller `requirements.txt` specifies the direct runtime dependencies. Other Python/platform combinations have not been exhaustively checked.

```sh
python -m pip install -r requirements.txt
python scripts/verify_results.py
```

The check recomputes all eight comparison rows, replays five compact models across 910 steps, checks the five development folds, and checks 5,636 median-of-three labels. NumPy files are loaded with `allow_pickle=False`.

## Re-extract measurements from raw text

```sh
python -m pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl
python scripts/verify_results.py --features
```

This additionally compares all 302 measurements for all 910 comparison steps with the saved matrix, and tests selected rows after replacing future text. Parsing runs locally. The replay disables network connections in its Python process.

## Score a specified reading step

```sh
PYTHONPATH=src python -m jev_equations.predict --model gaussian --text "A soap film stretches across a wire rectangle."
```

Use `--model spline`, `polynomial`, `linear` or `word-count` for the other compact models. `--text-file passage.txt` reads UTF-8 text. For a step in a longer passage, pass its `--start` and `--end` in **UTF-16 code units**. If omitted, the entire supplied text is treated as one step; this CLI does not reproduce the app's automatic step segmentation. Retain preceding text so the model can measure references to it.

Class probabilities are not calibrated estimates of reliability or human load. The default Gaussian model is the development-selected later direct equation, not the most accurate historical model.

## Reproduce the larger component model

Download `research-round4.zip` from the release, verify its checksum, and extract it. The original complete checker is at `research/work/round4/package/bundle-final/`; run its README commands from that directory. Keep its folders together. It contains the historical model registry, equations and measurement code. The public compact CLI intentionally has a different, explicitly bounded input contract.

## Full history and retraining

Extract all research ZIPs into one directory: each writes under `research/` with the original `work/` and `outputs/` structure. `MANIFEST.json` inside each ZIP lists every included member and original/published hashes. `scripts/verify_archives.py` can check the downloads against `provenance/release-manifest.json`.

After extracting all archives, recompute the earlier final-test arithmetic and the 300 raw further-fresh-test analyses with:

```sh
python scripts/verify_history.py research
```

Historical scripts include machine-specific paths, orchestration records and old assumptions; they are an audit archive rather than a one-command training package. Original source paths have been retained there where they are part of the recorded procedure. The five compact prediction paths are the portable, freshly tested interface in this repository. Do not start historical collectors simply to reproduce metrics: they require separate service credentials and can incur costs. Future experiments must use a new untouched test set.

Historical SHA-256 freezes record what the original procedure wrote. A manifest supplied beside its own data is an integrity check, not an independently timestamped preregistration or a digital signature.
