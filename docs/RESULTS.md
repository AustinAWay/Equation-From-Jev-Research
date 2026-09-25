# Results, without changing the meaning of the tests

The tested models did not achieve near-exact reproduction of the app. The later direct-equation experiments also did not establish an advantage over a flexible word-count predictor.

## Research sequence

| Stage | Main result | Interpretation |
|---|---|---|
| Initial search | Selected equation: 31.2% exact agreement | Failed the fidelity target; mean error slightly worse than the word-count baseline. |
| Round 2 | Smaller-decision approach: 41.7% on 48 new passages | Best observed of the three tested approaches; target still missed. |
| Round 3 | Preselected smaller-error combination: 38.5% on 80 new passages | Best observed primary candidate was 40.5%; these are different selection statements. |
| Round 4 | Preselected frequency/count-mode model: 47.7% on 100 new passages / 908 steps | Previous model: 40.4% on these same passages. Target still missed. |
| Further fresh test | Frozen round-4 model: 47.3% on another 100 passages / 910 steps | Descriptive 95% family-bootstrap interval: 42.9–51.6%. |
| Direct arithmetic follow-up | 32-term formula: 39.1%; linear word count: 36.8% | Reused the further-fresh-test set; no clear incremental advantage. |
| Nonlinear follow-up | Preselected Gaussian: 42.0%; spline: 43.4%; flexible word count: 42.5% | Same reused comparison; spline is not a freshly validated winner. |
| Autonomous search | 181 completed attempts; best development result 43.5%, previous model 45.6% | Repeated development-set selection, not fresh-test accuracy. |

Percentages from different test sets are not a learning curve. Text mix, reference variability and model choices changed. Earlier final-test data were deliberately admitted into later development sets; a test's role is specific to its research stage. The later 688-passage development set does not include the 100-passage further-fresh-test comparison.

## The comparisons that matter

For the preselected Gaussian equation, the advantage over the 32-term formula was 2.89 percentage points, with a descriptive 95% family-bootstrap interval of −1.57 to +7.21. Its difference from flexible word count was −0.48 points, interval −4.22 to +3.28. Neither establishes an improvement. The spline's observed advantage over word count was only 0.86 points, and it was observed after examining multiple equation types.

Round 4 improved observed exact agreement over the unchanged previous model by 7.26 points. Its adjusted interval was 2.42–12.16 points; the prespecified claim required at least five points. The displayed-error change was −0.059 units, interval −0.123 to +0.005; the second claim required no increase. Those specific joint improvement claims remained unresolved. A favorable point estimate is not the same as passing the stated test.

Globally shuffling the selected Gaussian model's input vectors reduced agreement to 27.4% on average. Shuffling within equal-word-count groups gave 38.3%; 3 of 500 shuffles reached the observed score. These are exploratory association diagnostics, not proof that the model understands text or isolates a cognitive mechanism. Repeated steps and constructed families limit an exchangeability interpretation.

The expanded training representation contained identical feature vectors with conflicting recorded targets. This establishes a deterministic-fit limitation for those recorded rows. It does not estimate a universal accuracy ceiling, show that all possible features will fail, or prove that 95% expected agreement is impossible.

## Original reports

- [Initial search](../results/working-memory-equation/report.md)
- [Round 2](../results/working-memory-equation-round2/report.md)
- [Round 3](../results/working-memory-equation-round3/report.md)
- [Round 4](../results/working-memory-equation-round4/report.md)
- [Further fresh test](../results/working-memory-fresh100/report.md)
- [Direct arithmetic](../results/direct-text-equation-20260924/report.md)
- [Nonlinear equations](../results/nonlinear-text-equation-20260924/report.md)
- [Autonomous search status](../results/equation-autopilot/status.md)

All statements about performance concern agreement with the saved app procedure. This release is an exploratory research record, not a peer-reviewed validation study.
