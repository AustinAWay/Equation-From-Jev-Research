# Working-memory equation: research round 2

Recorded before any round-2 fitting or new Jev reference collection. User authorized approaches 1–3 only. This is research code, not an app release.

## Question and scope

Can locally calculable equations reproduce the frozen Passage app's Jev-derived reading-step scores on new English passages under the existing grade-six reader profile? Equations may be arbitrarily long. No passage-type-specific specialist routing and no new local language model or semantic embeddings will be used. The existing frozen grammatical parser is retained as a measurement tool, as in round 1.

## Popper's contribution

Each conjecture must risk being wrong. We specify predictions before observing fresh answers, actively seek counterexamples, retain failures, and distinguish a failed particular equation from the much broader possibility of an equation. A surviving test gives provisional corroboration within these conditions, never a proof of universal accuracy. Source: Karl Popper, *Science as Falsification* (1963), conclusions 2, 5–7 and footnote 3, https://tildesites.bowdoin.edu/~j.knockel/falsification/ (read 2026-09-22).

Grouped cross-validation, predeclared thresholds, held-out prediction files and bootstrap intervals are modern safeguards used to implement critical testing; they are not attributed to Popper.

## Three conjectures and risky predictions

1. Direct formula: explicit measurements of grammatical connections between ideas improve direct score prediction over the old surface-count equation. Compare the original measurement set and a structural extension on identical family folds. Fresh-test prediction: the selected direct equation reduces family-weighted absolute error by at least 0.10 units relative to the frozen round-1 equation.
2. Smaller decisions: predicting intermediate Jev judgments locally, then applying counting rules, improves on learning only the final number. Fresh-test prediction: this equation reduces error by at least 0.10 units relative to approach 1. Also compare against a trivial intermediate-label baseline and inspect an oracle computation using actual reference judgments solely as a diagnostic; oracle scores are never deployed predictions.
3. Running ledger: explicitly tracking identities, reuse, grouping and retirement across reading steps improves prediction. Fresh-test prediction: the stateful equation reduces error by at least 0.10 units relative to its no-history ablation. Compare it with approaches 1 and 2 as secondary comparisons.

All three retain the round-1 aspirational fidelity test: at least 95% exact agreement and no more than 0.10 mean absolute error, including underlying unrounded output when rounding is used. Thresholds are research choices, not human/clinical validation standards.

For improvement claims, compute paired differences by passage family. Positive improvement means lower error. A simultaneous 98.33% bootstrap interval (Bonferroni across the three primary contrasts) wholly above 0.10 provisionally corroborates the specified improvement; wholly below 0.10 contradicts that magnitude under stated measurement assumptions; an interval spanning 0.10 leaves it unresolved. Report point estimates and ordinary 95% intervals as descriptive context. Missing a performance threshold on this finite benchmark is a benchmark failure, not a logical disproof of every possible equation.

## Development, freezing and fresh tests

All 120 old passages (60 paired families, 544 complete step references) are development material now. The old final-test results have already been seen and cannot provide independent confirmation for this round. Use five family folds fixed in folds.json, with seed 20260922. Related variants stay together. Fit preprocessing, selection and intermediate classifiers within training folds; choose candidates only by out-of-fold family-weighted error, tie-break exact agreement, then fixed name order. No length penalty. Retain candidate definitions, equations, predictions and failures. Cross-validation is selection evidence, not a final unbiased performance estimate.

The new corpus will contain 24 independent paired families (48 passages), including controlled changes and broader lengths. Author and record all texts and pair expectations before labeling. Fitting workers cannot inspect it. After fitting, freeze every selected equation and its source hashes. Generate and hash local predictions on the new text before requesting Jev's answers. No target, intermediate Jev answer, reference count or cache enters prediction.

Then collect three full Jev analyses per new passage, same frozen source, model, prompt, reader profile and internal sample count as round 1. Use the median complete score per step; report missingness, repeat disagreement and provisional flags. Never silently replace missing scores. Preserve all attempted passages and document exclusions. Do not adjust formulas after viewing fresh outcomes. Any subsequent repair requires another new final test.

Primary metrics weight each family equally, then each reading step within family equally (the existing round-1 convention). Bootstrap whole paired families, 10,000 draws, seed 20260922. Report fresh paired-contrast results, stable-reference sensitivity, worst errors and controlled-pair counterexamples. These generated examples do not establish textbook-wide or human-memory accuracy.

## Failure diagnosis and spending

Before interpreting a failed prediction, check export/evaluator parity, source/offset consistency, reference missingness, stochastic disagreement, and whether app counting can be recovered from available intermediate judgments. Diagnose failures without retroactively changing their criteria.

Existing conservative cost ledger: $9.960881868 of $15. Remaining: $5.039118132. New collection capped at $4.90, using the existing reservation ledger. A budget stop is reported as incomplete evidence, not as success or an excuse to change the target. No paid service is needed for final formula inference.

## Deliverables

Three implemented research approaches and the no-history ablation; explicit equations/rules and offline predictors; all development attempts and fresh predictions; raw reference provenance; a plain-English report containing claim → possible falsifier → actual test → result → limitation → status; and the strongest next test justified by the results.
