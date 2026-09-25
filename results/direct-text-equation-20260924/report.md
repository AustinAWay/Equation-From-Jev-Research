# Direct text equation: what happened

**An actual text-measurement equation was fitted, but its additional measurements have not yet shown a clear advantage over word count alone.** This is a candidate predictor of the Jev app’s output, not a validated measure of a person’s working memory.

The correction was to expose the path from text to numerical measurements to an ordinary arithmetic sum. The earlier equation also used text measurements; it was not a fixed “add two” rule. However, it hid those measurements inside hundreds of learned rule trees. The video did not explain that path adequately.

The new equation has 32 terms. Inputs include letters, sentence counts, long-syllable words, repetition, punctuation, pronouns, grammatical links, and distances to earlier repeated words. It uses only the current step and earlier text. All coefficients, definitions and a reproducible calculation are saved here.

| Method | Exact agreement with Jev |
| --- | ---: |
| New direct arithmetic formula | 39.1% |
| Word-count-only formula | 36.8% |
| Always answer 2 | 34.4% |
| Always answer 3 | 29.0% |
| Previous large model | 47.3% |

Predictions still concentrate on common scores: **794 of 910** are 2 or 3. The new arithmetic form does not by itself solve that weakness.

Continuous-score correlation: **0.596** for the new equation, versus **0.593** for word count alone. These are correlations, not accuracy percentages.

Shuffling whole text-measurement vectors among the 910 steps reduced exact agreement to **29.2%** on average over 500 shuffles (middle 95%: 26.3%–32.0%). None reached the unshuffled result. This demonstrates an association between the measured text and its saved labels; it does not identify meaning, human memory or the importance of any individual feature.

The gain over word count was **+2.29 percentage points**; its descriptive family-bootstrap interval was **-0.08 to +4.58 points**. It includes zero. The gain over the constant guess also had an interval including zero. The earlier large model was clearly more accurate on this comparison set.

| Claim | What would count against it | Test and outcome | Status |
| --- | --- | --- | --- |
| The formula uses text information | Shuffling complete text vectors preserves its performance | 39.1% correct alignment versus 29.2% shuffled average | Preliminary text/label association |
| The extra measurements improve on word count | No clear advantage over the length-only formula | 39.1% versus 36.8%; difference interval includes zero | Not established |
| This measures human working-memory load | Failure against direct human measurements | No human measurements available | Untested |

The 688 development passages (4,726 steps; 344 families) were used for five-fold family-separated selection among 32 fixed candidates. Candidates used linear sums or quadratic sums/products and 5, 10, 20 or 32 selected terms. The selected linear formula was fitted on all development rows and frozen before this evaluation. Each family receives equal weight.

The evaluation reused the previous 100 passages (910 steps; 50 families), with the median of three saved Jev app runs per step. These data were never used to fit or select this equation, but the research team had previously seen this comparison set and aggregate results. This is exploratory reuse, not a new blind confirmation. All prior reference disagreements, provisional flags and coverage limitations remain.

Reasoning: a model that merely exploits common scores should survive removing the connection between text measurements and answers. It did not. A model whose extra inputs add useful information beyond length should beat a length-only predictor convincingly. This test did not establish that. That distinction keeps the explanation open to being wrong instead of labeling any improvement a success.

The next informative test is a fresh set of text pairs matched for length but differing in references, nested clauses and relationships. Freeze any candidate beforehand. If its predictions fail to track corresponding Jev-score changes, the claim that it captures more than surface length is weakened. Direct human data would be required for a claim about people.

Verification: every candidate was checked for finite inputs, coefficients and predictions. A local matrix-operation warning prompted a refit using explicit sums; the selected specification and scores were unchanged, and the final run has no runtime warnings. The readable exported arithmetic reproduced all 910 comparison predictions to numerical precision. Some candidate searches selected fewer than the requested terms because measurements were redundant; those warnings are retained. No new Jev requests were made.

Files: equation.md (full readable equation), equation.json (full precision), results.json (all controls and intervals), development-search.json (every candidate), example-calculations.json (first passage, every step), comparison-predictions.json (every prediction and measurement), verification.json (replay checks).
