# Methods and limits

## Target and unit of analysis

The target is a reading-step score calculated by a frozen version of [Working-Memory-Jev / Passage](https://github.com/AustinAWay/Working-Memory-Jev), using Jev assessments and the app's own scoring logic. Reader assumptions, prompts, app source and candidate limits are recorded in each collection's metadata. Scores are not capped at the reader's slot budget. The fixed profile is grade six; a single fitted equation does not establish performance for other profiles.

For the later experiments, three complete app analyses produce three scores at each step. Their median is the reference label. Within one paired scenario family, every reading step has equal weight; every family has equal total weight. For family f with n_f rows and F total families, row weight is 1/(F n_f). Exact agreement is the sum of these weights over matching rows. Mean absolute error uses the same weights on absolute whole-number differences. This differs from counting every step equally across the entire corpus.

For example, the further fresh test has 423 exact matches out of 910 rows (46.5% pooled), while the family-weighted rate is 47.3%. Neither number means that 47 of the 100 entire passages were scored perfectly.

## Development and selection

The final direct experiments use 688 development passages in 344 related families. Five grouped folds hold whole families out together. Scaling, feature selection, spline knots, kernel centers and fitted coefficients are learned inside training folds. IDs and family labels are grouping metadata, not model inputs. Prefix feature extraction receives only passage text and UTF-16 step boundaries, and stops parsing at the end of the step.

The nonlinear experiment evaluated 36 full-text specifications and six word-count controls. Development performance selected a winner for each equation type, then the overall Gaussian winner; fitted parameters and comparison predictions were frozen before the later evaluation. The direct arithmetic experiment tested 32 specifications. Repeated choices made across research rounds remain exploratory; grouped cross-validation does not eliminate adaptive overfitting.

The component-model pipeline is different from the compact prefix-only equations: it obtains reading steps and candidate spans using whole-passage extraction. Later text may affect segmentation. It must not be described as a strictly streaming text-to-score system.

## Reference quality

On the 910-step further fresh test, repeat scores differed at 267 steps, 880 carried a provisional flag, and all 910 had a passage coverage warning or lacked an explicit all-clear flag. On round 4's different 908-step test, the corresponding counts were 282, 875 and 908. All rows were retained. A passage-level warning does not prove that every step is wrong. A provisional score is neither a validated answer nor a guaranteed lower bound.

Collection settings changed to handle service errors: longer waits, retries and concurrency amendments are recorded. Round 4's final reference has 62 original-setting analyses and 238 amended-transport analyses. Saved successful responses and model predictions were preserved, but this is not identical execution throughout. Reported token costs and conservative reservations are estimates, not invoices.

## Uncertainty and interpretation

Bootstrap comparisons resample whole families, retaining the pairing between models on a family. Later comparison intervals are descriptive and do not repair prior exposure to that test set. The round-4 primary comparison uses two 97.5% intervals; the round-3 six primary comparisons use adjusted 99.1667% intervals. Other comparisons are marked exploratory in the original reports.

There is no random population sample, independent human validation, blinded external authorship of the corpus, or demonstrated transport to other Jev/app versions. Synthetic paired passages share construction habits. Repeated reference labels can disagree even with fixed visible input. A failed numerical prediction could reflect representation, fitting, segmentation, target variability, or the reference procedure; it does not identify a psychological cause.

## Claims and tests

| Claim | What challenges it | Present status |
|---|---|---|
| A tested equation reaches 95% agreement with at most 0.10 unrounded error | Performance short of either fixed target | Not achieved by the reported candidates. |
| Richer measurements usefully beat text length | Strong length-only control performs similarly on the same data | Not established for the later direct equations. |
| The fitted function uses some text/label association | Removing that association retains performance | Shuffle diagnostics suggest association within these records. |
| The model measures human working memory | Failure against appropriately collected human outcomes | Not tested. |
| No possible equation could work | Would require a defined class and justified impossibility argument | Not established by this search. |

Preserving unsuccessful predictions is part of the evidence. No failed trial was removed to improve the headline result.
