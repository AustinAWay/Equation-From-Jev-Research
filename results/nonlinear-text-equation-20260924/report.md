# More complex equations learned from final Jev scores

**Yes: final Jev results can serve as the answer key for learning an equation. This run did that directly. The new equations improved on the previous simple formula in observed accuracy, but did not establish an advantage over a flexible word-count-only equation.**

The experiment fitted 36 full-text specifications and six word-count controls. It tried curved feature effects (splines), Gaussian comparisons with learned reference patterns, and direct sums/products of measurements. Each candidate was checked in five development folds, with related passages always kept together. Both compact 38-measurement and expanded 302-measurement representations were tested. All selected models converged; every final fitted arithmetic export independently reproduced its numerical predictor.

| Equation | Development exact agreement | Existing 100-passage comparison |
| --- | ---: | ---: |
| Gaussian equation — selected before comparison | 38.3% | 42.0% |
| Direct logistic equation (linear candidate won) | 38.1% | 42.3% |
| Cubic-curve equation | 38.3% | 43.4% |
| Flexible word-count-only control | 37.6% | 42.5% |
| Previous 32-term formula | 36.0% | 39.1% |
| Previous large model | 45.6% | 47.3% |
| Always answer 2 | — | 34.4% |

The Gaussian equation was selected by development performance, before evaluating the comparison answers. The cubic-curve equation happened to score highest among the new full-text candidates on the comparison set. Selecting it now and calling that an independent success would use the comparison answers to choose the winner. Both results remain visible.

The selected equation has 38 measured inputs and **6,942 saved numerical parameters**. Its gain over the prior direct formula is +2.89 percentage points, with a descriptive 95% family-bootstrap interval of -1.57 to +7.21. Its difference from the flexible word-count equation is -0.48 points, interval -4.22 to +3.28. Both intervals include zero. The earlier large model remains more accurate on this comparison.

## Attempts to expose the explanation to failure

| Claim | Challenge | Result | What follows |
| --- | --- | --- | --- |
| The equation uses information from the text | Shuffle complete input vectors across steps | 42.0% aligned versus 27.4% shuffled mean | The inputs have predictive association with these labels |
| It uses information beyond current-step word count | Shuffle vectors only among steps with exactly the same word count | Shuffled mean 38.3%; 3/500 shuffles reached the observed result | Some conditional association is suggested; this is a diagnostic, not proof of meaning or a causal mechanism |
| Added complexity gives useful improvement beyond length | Compare with a flexibly fitted length-only equation | 42.0% versus 42.5%; difference interval includes zero | Useful incremental predictive improvement is not established |
| These equations measure human working memory | Compare with human outcomes | No such data in this experiment | Unvalidated |

Predicting score 1 is no longer almost absent: the selected equation gets 46.0% of the Jev-score-1 steps correct. However, it still struggles with higher scores. The complete per-score table and prediction distribution are in results.json. This does not rescue the missing advantage over the length-only control.

## A more specific obstacle than equation length

A training-only diagnostic found 128 groups with identical expanded 302-number input vectors but conflicting Jev reference scores. Most have literally the same visible text and boundaries, which may reflect reference variability or information outside the visible-prefix formulation. Seven conflicting groups contain different visible text. One reorders earlier sentences while leaving all measured numbers unchanged; the later phrase “and it is eight.” receives median scores 1 versus 3.

A deterministic equation cannot output two different answers for an identical input vector. More coefficients alone cannot distinguish those examples. The next justified feature revision is to encode order and which entity or relationship a later phrase refers to. That revised claim should be challenged using equal-length, reordered or reference-swapped text pairs. The diagnostic is a limit on these particular training records; it is not an estimated ceiling for new text.

## Scope and reproducibility

Training used 688 passages / 4,726 steps / 344 families. Selection used five folds. Evaluation reused 100 passages / 910 steps / 50 families whose aggregate results and examples were already inspected in earlier work. Comparison labels were excluded from fitting, scaling, knot placement, center choice and model selection, but this remains exploratory reuse rather than fresh blind confirmation. Each reference is the median of three saved Jev-app runs, with all earlier disagreements and provisional/coverage flags retained. No new Jev requests were made.

All families receive equal total weight. The bootstrap resamples whole families. Every exported comparison prediction file is hash-bound and its row identifiers checked before comparison labels are read. The initial Gaussian solver hit its iteration limit under a stricter tolerance; the same fixed grid was rerun uniformly with the spline tolerance and a higher iteration limit. Initial failed results are preserved. Platform matrix warnings were checked against finite arrays and an independent arithmetic replay, including probabilities.

The target change from regression/rounding to final-score classification is part of this experiment. Any gain cannot be attributed solely to nonlinear complexity; the linear logistic candidate is retained as a control. Classifiers only output score categories present in development training, so an unseen score category remains a limitation.

Files: equation.md explains the selected formula; full-equation.txt lists all numerical constants; selected-equation.json is machine-readable; results.json contains every comparison and interval; selection.json records the pre-evaluation choice and hashes; example-calculations.json replays the first passage from raw text; each model subdirectory preserves all candidate results and independent runtime code.
