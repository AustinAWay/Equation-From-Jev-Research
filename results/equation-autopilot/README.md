# Self-running equation search

This is an ordinary local program. After launch, it keeps changing and testing equations without asking an AI agent to choose the next experiment. **Training uses no agent tokens and makes no model API calls.**

Open **status.md** for progress. Reopen it to see the latest update.

- **Start.command** starts the search or resumes its saved work. Opening it again while running does not launch another search.
- **Stop.command** asks it to stop and saves completed work. An interrupted attempt resumes from the same proposed equation.
- **best-equation.json** contains every learned numerical parameter of the best successfully exported search candidate. It appears after the first complete candidate and is updated after verified improvements.
- **best-candidate.json** records that equation's development results. A search candidate can still be worse than the existing equation; check the comparison in status.md.

These launchers are local scripts for this Mac. They require this workspace and its existing Python dependencies. The computer must stay powered on. The program prevents idle sleep while active; closing the laptop, restarting it or manually sleeping it can interrupt computation. It does not automatically start on login.

## What it does automatically

1. Reuses the saved 688 passages, 4,726 reading steps and their Jev scores.
2. Tries a few starting equation families, then preferentially changes stronger candidates. Twenty percent of later proposals explore other starting points.
3. Changes numerical settings, text-measurement groups, score-selection rules and arithmetic terms. Available added terms include sums, differences, products, ratios, minimums and maximums. Related passages stay together in five training/evaluation groups.
4. Learns coefficients and numerical branching rules using ordinary mathematical fitting. It tests all five groups, gives each passage family equal weight, and ranks candidates by exact matches followed by smaller average error.
5. For a new best candidate, fits its final equation and checks that the exported numerical rules reproduce the fitted model on all development rows. It saves the equation only after that check passes.
6. Keeps trial settings, outcomes and failures so a stopped search can resume. The search can fail or plateau; success is not guaranteed by more iterations.

The search space includes linear equations, ensembles of numerical decision rules and boosting, using the existing text parser and explicit measurements. It does not add a pretrained semantic model or separate specialists for different passage types. Its choices are constrained by the programmed search space; it cannot invent arbitrary new meanings or measurements.

## Bounds for this run

- Up to **12 hours per launch**, **1,000 total attempts**, or **150 attempts without a meaningful exact-match gain**, whichever stops it first.
- Approximately two CPU cores for fitting; each scoring or export operation has a ten-minute timeout.
- Stops early if a verified candidate reaches **95% exact agreement and at most 0.10 average error on the development comparison**.
- Stops on repeated calculation failures or a failed equation export, recording the reason. Resume retries a failed export without recomputing the candidate's already saved comparison.

An improvement of at least 0.1 percentage points relative to the best at that moment resets the stalled-progress counter. Smaller improvements are still saved. Each equation returns a whole-number score, so its raw and displayed outputs are the same number.

The settings are in config.json. Once a run has started, changing code or settings requires a new run directory: the program refuses to mix incompatible checkpoints silently. Restarting the unchanged settings resumes saved work and gives the next launch its own 12-hour allowance, while retaining the total attempt limit.

## What its results mean

**This is an automated development search, not a new independent accuracy study.** It can overfit the repeatedly reused evaluation groups even though each individual fit excludes its evaluated families. Earlier research has also used this data. Reaching the development target produces a candidate requiring a genuinely new, untouched test; it does not prove that working memory has been solved.

The existing equation achieved about **45.6%** on this development comparison. Its earlier **47.7%** result came from different, fresh-test passages. Compare this program with the 45.6% development baseline in the status file. The previous final-test set is not an input to this search.

This follows the requested critical-testing approach: an equation must risk failure on withheld families; failed attempts remain in the log. An independent final test is still needed after adaptive search. Agreement with the app is not validation against human working memory.

## Running a saved candidate

The learned function is fully numerical: explicit coefficients or tree thresholds/leaves, text transformations, optional arithmetic terms and a whole-number output rule. The existing grammar parser still supplies the input measurements. Nothing needs to be learned again when using the saved equation.

For supplied reading-step records, the local command is:

```
python3 autopilot.py predict --rows reading-steps.jsonl --model best-equation.json
```

Each input line supplies `passage`, `start` and `end` in the original app's UTF-16 character-offset convention. Optional IDs are passed through; target/teacher fields are ignored. This is a research interface, not a new reading UI.

The detailed trial records and logs live in the run directory named in config.json. Existing research results and archives are unchanged.
