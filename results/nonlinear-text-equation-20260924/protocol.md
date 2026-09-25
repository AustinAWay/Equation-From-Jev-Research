# Learning nonlinear equations directly from Jev's final results

User request: try more complex mathematical equations, working backward from final Jev outputs to measured properties of the source text.

Question: Can nonlinear equations trained directly on final Jev scores improve prediction over the earlier linear formula and flexible word-count-only equations?

The final Jev score is the training target. No intermediate predicted Jev decisions, teacher explanations or labels enter the input. Measurements use only current and earlier visible text. This run changes both the functional form (nonlinear) and the fitting objective (classify each final integer score rather than average scores and round). These are separate possible explanations of an improvement; do not attribute the whole gain to equation complexity alone.

Data: 688 existing development passages, 4,726 reading steps, 344 families. Inputs comprise 38 transparent current/prior text counts and grammar measurements, plus a larger set re-extracted by the existing prefix-only text measurement code. No passage/topic identities, future text, learned word-identity tables, or Jev outputs are features. All scalers, spline knots, kernel centers and fitted coefficients use training-fold data only. Five GroupKFold folds keep families together. Give each family equal weight, then each step in a family equal weight.

Finite candidate search, fixed before evaluation:

1. Cubic spline features followed by a multinomial logistic equation: compact or expanded inputs; 3 or 5 knots; C = 0.01, 0.1 or 1. Twelve candidates. Run the same six settings with word count only for a flexible baseline.
2. Gaussian radial-basis equations followed by multinomial logistic output: compact or expanded inputs; 128 centers sampled without replacement from training rows using family weights and a fixed seed; dimension-normalized length scales 0.5, 1 or 2; C = 0.1, 1 or 10. Eighteen candidates. Add the standardized original measurements to the Gaussian terms so the equation can represent a global trend as well as local deviations.
3. Logistic equations over direct measured inputs or their squared/product terms. Compact inputs only; degrees 1 and 2; C = 0.01, 0.1 or 1. Six candidates. The degree-1 equations help separate changing the target-fitting objective from adding nonlinear terms.

Select one winner per family and the overall winner using family-weighted development out-of-fold exact agreement, breaking ties by lower absolute error and smaller parameter count. Record every candidate and convergence failure. Freeze selected model parameters and comparison predictions before scoring. No adjustments against comparison results.

The existing fresh100 set has already been inspected in prior work. Reusing its 100 passages / 910 steps / 50 families is exploratory comparison, not a fresh blind test. Its labels remain outside fitting and candidate selection. Jev references are the middle of three saved full app runs. No new paid calls are needed.

Challenges to the explanation: compare against always 2, always 3, the prior direct formula, the old large model, and the newly fitted word-count-only baseline. Shuffle whole feature vectors globally, then within exact current-word-count groups, 500 times each. A deterministic equation's shuffled predictions are equivalent to evaluating the permuted feature vectors. The latter preserves sentence length and challenges the claim that other text information matters. Report exact agreement, mean absolute error, prediction distribution and each target score's accuracy. Use paired family bootstrap differences against baselines; these descriptive intervals do not repair prior comparison-set exposure or multiple-candidate exploration.

A better numerical fit only supports prediction of the app's outputs within these conditions. If length-preserving shuffling retains the accuracy, or the flexible length-only baseline is as good within uncertainty, the claim that richer text information helps is not established. If the best candidate does not improve over the earlier model, say so. No outcome will be called proof of a human working-memory equation. Save the full mathematical formula, parameters and independent replay check so the result is inspectable and runnable without Jev.
