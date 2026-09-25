# Working-memory equation experiment

The experiment did not find a reliable replacement for Jev. The selected equation matched 31.2% of unseen reading-step scores; its mean error was slightly worse than a word-count baseline. Start with [the report](report.md).

## Included

- `equation.txt` and `equation.json`: the complete selected formula and exact arithmetic specification.
- `research_log.md`: decisions, hypotheses, revisions, failures and results.
- `failure_analysis.md`: diagnosis after the final test; no further fitting.
- `final_results.json` and `final_predictions.jsonl`: preserved final evaluation.
- `iterations.jsonl`: all 540 successful final-development configurations.
- `reference-report.json`: reference repeatability and coverage.
- `checker/`: runnable offline prototype. It approximates Jev-derived scores; it is not validated as a working-memory measurement.
- `full-experiment.zip`: code, all corpus partitions, raw analyses, candidate equations, intermediate comparisons, tests and frozen reference source. Training-library binary snapshots and temporary caches are omitted; all mathematical equations and predictions are retained.

## Run the saved equation

Use a Python environment matching `dependencies.json` and install `checker/requirements-inference.txt` plus the spaCy `en_core_web_sm` version 3.8.0 model. These dependencies are already present in the environment used for this experiment.

From this folder:

```sh
python3 checker/predict_local.py --equation equation.json --text "Put the red block beside the blue block. Compare their heights."
```

The checker reads no Jev key and blocks network connections. It extracts the reading steps, measures text locally and evaluates the saved mathematical expression. `equation_output` is the final integer prediction; `pre_round_prediction` is the underlying continuous value. The example is only a software demonstration.

## Reproduce research

Unzip `full-experiment.zip` and read `equation-research/README.md`. The frozen source, profile, model and prompt versions are recorded in the metadata. Reference collection needs a separately supplied API key; no credentials are bundled. Existing raw analyses can be rescored without new Jev calls. The final test is already used: a new research round needs new final-test families.
