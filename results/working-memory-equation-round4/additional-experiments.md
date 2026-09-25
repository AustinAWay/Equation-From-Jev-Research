# The extra experiments did not improve the equation enough to advance

We tested three ways to improve its agreement with the reference app. None cleared the improvement threshold written before its test.

Each experiment used the same **688 development passages**, covering 4,726 reading steps. The target was the median of three reference-app scores under the fixed learner profile. Related passages stayed together in 344 families, with each family receiving equal weight.

To advance, the highest-ranked candidate had to gain **at least two percentage points of exact agreement without increasing average error**. Falling short on either requirement counted as failure.

| Experiment | Idea tested | Best exact agreement | Average error |
|---|---|---:|---:|
| Existing equation | Unchanged comparison | 45.61% | 0.710 score units |
| Shared adjustment | Combine two equations using a linear rule or small tree | 42.57% | 0.737 |
| Whole-number classification | Choose the likeliest adjustment or final score, rather than round an average | 44.71% | 0.757 |
| Running score estimate | Use the previous predicted score distribution to help interpret the current one | 45.64% | 0.708 |

The table shows the highest-ranked candidate from each experiment, selected by exact agreement first, then average error. Every candidate and failure is preserved in the research records.

The first two ideas reduced exact agreement and increased error. The weakest history setting gained only **0.02774 percentage points**, far below the required two points. Stronger history settings reduced exact agreement. The tiny positive result is preserved as a development candidate, not promoted as a confirmed improvement.

The existing counting equation works like this:

**Score = most likely primary-item total + rounded prediction of additional relationship units.**

For each candidate item, a local numerical model estimates its chance of needing its own unit. The equation combines those chances into probabilities for different totals, chooses the most likely total, then adds the predicted relationship units. If totals tie, it chooses the smaller one. It treats the item decisions as independent when combining them—a simplifying assumption, not an established fact about comprehension. The numbers are model estimates, not proven calibrated probabilities.

The shared-adjustment experiments used extra family splits inside each evaluation split. Their training predictions came from base equations that had seen neither the predicted family nor the families reserved for evaluation. The history experiment learned typical score changes only from training families, carried forward predicted distributions, and reset at each passage. It never received an actual score from the passage being evaluated. Independent audits reproduced the results and checked the separation and arithmetic.

These are **adaptive development experiments**: earlier results helped choose the methods, and the same development data were reused. Those extra splits also gave some underlying equations fewer training examples, which could affect the comparison. This is not confirmation on new passages.

The results reject advancing these specific repairs. They do not prove that a better equation is impossible, or that the app's scores measure human working memory accurately. The frozen final test and its registered equations were unchanged. Any future candidate would need its own prospective test and fresh confirmation.
