# Three ways to build a working-memory equation

All three approaches were built and tested. None met the agreed accuracy target on the new passages. **2. Learn the smaller decisions** had the lowest average error among the three on this particular test. This ranking is descriptive; the paired comparisons below determine what differences the evidence supports.

We are trying to reproduce the scores from your Jev-based program, using calculations that run locally. Equation length was unrestricted. Approaches 4 and 5 were excluded: no specialist formulas selected by passage category, and no additional local language-model helper or semantic embeddings. The same existing grammar parser supplied text measurements.

## What we actually did

- Used all 120 old passages as practice material. Even the old test passages count as practice now because their results have already been seen.
- Tested candidate formulas by keeping whole pairs of related passages together across five practice folds. All preprocessing and fitting stayed inside the training portion of each fold.
- Compared 40 direct-formula candidates, 10 smaller-decision candidates, and 42 ledger/ablation/baseline candidates. A two-variant word-count comparator was also fitted on the same practice data. Development results selected the formulas; they were not presented as independent confirmation.
- Wrote 48 new passages in 24 independent paired families, with controlled changes and lengths 26–57 words. They are authored examples, not an independently sampled collection of textbooks.
- Froze the equations and saved their 208 local predictions before requesting any new Jev answers. The fresh answers could not influence the equations.
- Ran Jev three times per passage and used the middle complete score for each reading step. Evaluated 208 steps from 48 passages and 24 families. Missing steps: 0; complete families: 24/24.

## The results in plain English

“Exact” means the equation gave the same displayed number as the middle Jev-based score. “Average error” means how many score units it missed by; lower is better. Related passage families receive equal weight.

| Approach | Exact | Within 1 unit | Average error | Error before rounding |
|---|---:|---:|---:|---:|
| 1. Find patterns directly | 40.0% | 81.4% | 0.855 | 0.847 |
| 2. Learn the smaller decisions | 41.7% | 88.1% | 0.740 | 0.775 |
| 3. Keep a running list of ideas | 32.7% | 85.6% | 0.888 | 0.925 |
| Simple word-count formula, refitted on all practice data | 29.5% | 85.9% | 0.917 | 0.962 |
| Same running-list formula, with earlier ledger cleared | 31.6% | 85.2% | 0.888 | 0.920 |
| Best separately tuned formula with earlier ledger cleared | 34.3% | 83.7% | 0.891 | 0.891 |
| Previous experiment’s frozen equation | 39.0% | 81.7% | 0.846 | 0.872 |
| Previous experiment’s frozen word-count formula | 28.8% | 85.2% | 0.931 | 0.964 |
| Simple frequencies of intermediate roles | 30.0% | 87.7% | 0.874 | 0.878 |

The original target was at least 95% exact agreement and no more than 0.10 average error, including the underlying unrounded equation. These were proposed research targets, not standards for measuring people’s working memory.

## How Popper shaped the test

Each proposal had to make a prediction that could fail. We fixed the failure criteria in advance, looked for counterexamples, and retained unfavorable results. Surviving a test provides provisional support within its conditions; it does not establish a perfect universal formula. This follows [Popper’s *Science as Falsification*](https://tildesites.bowdoin.edu/~j.knockel/falsification/), especially conclusions 2, 5–7 and footnote 3. The fold separation, locked predictions and bootstrap uncertainty are modern safeguards used here, not inventions attributed to Popper.

Each claimed improvement was at least 0.10 fewer error units. The uncertainty ranges below resample whole families and are widened to cover the three planned comparisons together. An interval entirely below 0.10 challenges that promised amount of improvement; one crossing 0.10 leaves it unresolved. This is a statistical assessment of a specified predictive claim, not a logical disproof of every possible formula.

| Predeclared claim | Observable result that challenges it | Actual test | Improvement and uncertainty | Current status |
|---|---|---|---|---|
| The revised direct formula improves on the old equation by 0.10. | An improvement interval entirely below 0.10 | New direct formula against the frozen old formula | -0.009 [-0.103, +0.085] | Specified improvement contradicted under these measurement assumptions |
| Learning the smaller decisions improves on direct prediction by 0.10. | An improvement interval entirely below 0.10 | Smaller-decision pipeline against direct pipeline | +0.115 [+0.013, +0.214] | Unresolved at this sample size |
| Keeping the running list improves on clearing its earlier contents by 0.10. | An improvement interval entirely below 0.10 | Matched algorithms and rules, with or without prior ledger state | -0.000 [-0.057, +0.053] | Specified improvement contradicted under these measurement assumptions |

Positive differences mean the proposed method made smaller errors. The smaller-decision method's entire interval is above zero: this supports a positive improvement on this benchmark. But its interval includes improvements smaller than 0.10, so the promised size remains unsettled. The direct revision and historical ledger did not survive their declared minimum-improvement tests.

Exact formulas, source and data hashes, individual predictions and all candidate outcomes are preserved. We did not revise any frozen prediction after receiving the new answers.

## What each equation does, and what its failure teaches us

**1. Find patterns directly.** We tested the original text measurements and 18 added measurements of grammatical connections. The added measurements did not win the practice comparison: best MAE 0.79257 versus 0.79160 for the original set. The selected equation starts with a number, adds 250 conditional corrections, and rounds the result. This retains the failed structural-feature revision. Any gain over the older frozen equation would support the selected pipeline; it would not establish that the discarded added measurements helped. The old comparator also had less training data, so this is a pipeline comparison rather than an isolated algorithm experiment.

**2. Learn the smaller decisions.** Each locally extracted piece gets probabilities for three roles: starts a counted group, joins a group, or serves as background. A separate equation estimates extra relationship units. Its final calculation is:

`score = max(0, floor(sum(predicted counted-group probabilities) + predicted extra units + 0.5))`

The probabilities and extra-unit estimate are fully exported conditional equations. The same counting identity reproduced all 1,632 cached individual Jev-derived scores when supplied with actual Jev judgments. That is a diagnostic showing the arithmetic is recoverable, not a result for the local predictor. At prediction time it has to estimate those judgments from text. Compared with approach 1, it also uses different local inputs; the test therefore compares whole implementations, not a clean causal isolation of intermediate supervision. Averaging component judgments across repeats differs slightly from taking the median total; that diagnostic gap was 0.01882 error units on old data and is recorded.

**3. Keep a running list.** The program tracks named ideas and relationships, reuses identities, applies explicit pronoun/group rules, and retires items after 8 local grammatical events. A fitted weighted-sum equation turns the resulting measurements into a count. Its matched comparison uses the same rules and fitting method while clearing the earlier ledger. Both are allowed to parse the prefix, so the comparison specifically tests explicit stored state. On practice data the matched advantage was 0.0613; the best separately tuned version without history was almost tied with the ledger. The ledger also loses the direction of some relations: “Mira follows Noel” and “Noel follows Mira” can share one identity. That is a concrete representation limitation, although it does not by itself prove their required counts should differ.

**A concrete counterexample to these ledger inputs.** On old data, “Draw a perpendicular line at the marked point” consistently scored 3, while “Examine two handwritten copies of a short passage” consistently scored 1. Yet the selected ledger gave them exactly the same 30 numerical measurements. Five such conflicting groups were found among 389 repeat-consistent old steps, without rounding or binning the measurements. A deterministic equation receiving identical inputs must return the same output, so no increase in equation length alone can make this exact input set reproduce both recorded answers. This is a limitation of these measurements and reference observations; it does not disprove the 95% benchmark target or the possibility of a richer text equation. [Exact collision audit](exact_collisions.md).

## Reference quality and checks

Jev repeats disagreed at 57/208 evaluated steps. The app marked 187 steps provisional and 113 as coverage-limited. Those flags were preserved. Results on wholly repeat-consistent steps were also calculated:

- 1. Find patterns directly: average error 0.795.
- 2. Learn the smaller decisions: average error 0.672.
- 3. Keep a running list of ideas: average error 0.810.

We verified local extraction and reference offsets, exact exported arithmetic, no teacher fields in prediction inputs, no network use during prediction, no leakage between paired families, and unchanged source/model hashes. The ledger passed 18 focused tests; the smaller-decision model passed 6; the direct model passed 5. These checks support correct execution of the experiment, not the truth of its scientific conjectures. Reproducing Jev estimates is distinct from validating actual learners’ working-memory demand.

**A limitation in the reference procedure itself.** In two near/far paired tests, the app's 12-prior-item limit omitted original rule details only in the farther-away version. For one rule it dropped the original membership, badge and time-threshold pieces; for the other it dropped the original blue-lamp piece and the linking predicate. The full text was still in the prefix, but those occurrences were absent from the item decisions. The near variants scored 5–6 across repeats; both far variants consistently scored 3. This confirms omitted candidates and a changed score, not that the omission was the sole cause. A separate controlled change to the cap is needed to test that explanation. The main experiment's reference scores and results remain unchanged. [Reference audit](distance_reference_audit.md).

The fresh set is small and deliberately constructed. Bootstrap ranges describe variation across these 24 families; they do not guarantee performance on unseen authors, subjects, lengths, languages, reader profiles or Jev versions. Provisional Jev answers and incomplete candidate selection also limit the strength of conclusions about cognitive load.

## Cost and timing

New collection: $3.4218 from reported input usage; $3.4425 including conservative unknown-use reservations. Combined with the old experiment: $13.4034, under the original $15 cap. The saved equations require no Jev calls to run.

Predictions locked: 2026-09-22 18:51:26 UTC. First fresh paid request: 2026-09-22 18:52:08 UTC. Automated integrity checks enforce this order.

## The next test worth running

First, test the reference procedure's cap on a separate copy: keep passage, reader, prompt and scoring rules fixed, change only the allowed earlier candidates, and repeat the two audited pairs. If the count pattern remains despite retaining the omitted rule details, that would challenge the cap explanation. Keep these diagnostic results separate from this frozen benchmark.

For equation research, keep approach 2 unchanged as the comparator. Give a revised version explicit measurements of who acts on whom and which earlier object a reference points to. Test those changes on new paired passages, with predictions frozen before collecting answers and the same 0.10 minimum improvement rule. That tests a specific proposed repair within approaches 1–3. These are proposed next experiments, not work claimed as completed here.

## Files

- [Research protocol](protocol.md): predictions, possible failures and analysis rules recorded before fresh outcomes.
- [Research log](research_log.md): decisions, revisions and their reasons.
- [Detailed results](final_results.json) and [every final prediction](final_predictions.jsonl).
- [Failure analysis](failure_analysis.md): specific counterexamples and paired challenges.
- [Offline calculator instructions (in research-round2.zip)](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/download/research-data-v1/research-round2.zip): run and inspect all three formulas locally.
- [Complete research archive (in research-round2.zip)](https://github.com/AustinAWay/Equation-From-Jev-Research/releases/download/research-data-v1/research-round2.zip): code, equations, data, candidate records and frozen reference provenance.
