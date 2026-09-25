# Continued equation search: result

**The selected equation matched the app exactly 47.7% of the time on the fresh test.** The unchanged previous-best equation matched 40.4% on those same passages. The new equation's displayed score was within one unit 87.7% of the time, with average absolute error 0.683 units. It did not reach the original target of 95% exact agreement and at most 0.10 raw-score error.

This test does not establish the specified improvement. The uncertainty range leaves at least one part unresolved.

The exact-match change was **+7.26 percentage points**, with an uncertainty interval from 2.42 to 12.16 points. Displayed-score error changed by **-0.059 units**, with an interval from -0.123 to 0.005. Negative error change means improvement. These are paired 97.5% intervals for the two predeclared primary claims, adjusted to aim for 95% joint coverage under the bootstrap assumptions.

## What we tried and why

In a diagnostic calculation, replacing the old equation's item decisions with the app's recorded decisions reduced far more error than replacing its extra relationship counts. That made item decisions a useful repair target. This comparison does not isolate a cause of error, and a predictor that already needs the app's answers cannot replace it.

We tested richer word and grammar measurements, learning the final count directly, and learning smaller item decisions. We also changed the addition rule: choosing the most likely total can differ from counting every item whose individual chance reaches one half. On the initial 488-passage development set, word frequency gave a small improvement. A change in training weights and a fixed 50/50 combination of two predictors made those development results worse, so they were retained as failed attempts and dropped from the final candidates. No passage-specialist routing or new semantic language model was added.

All 488 previous passages became development material. We collected 200 additional passages, making 688 in 344 paired scenario families. The additional passages averaged 86.7 words, compared with 56.6 for the earlier material. This changes both the amount and the content of training data; any added-data effect cannot be credited to quantity alone.

The development comparison kept related passages together in five folds. We then selected **Choose the most likely total, with word frequency**, using the rule fixed in advance: most exact development matches, then smaller displayed-score error, then a fixed name tie-breaker. We saved all final predictions before requesting any final reference answers. The final result was not used to switch winners.

## What the fresh test measures

The final set contained **100 passages in 50 paired scenario families and 908 reading steps**. A reading step is a point in the passage where the app assigns a score. The set was authored and sealed before the new development material. Each passage received three complete app analyses; the middle of the three scores was the reference answer at each step. Each scenario family contributes equally, and each reading step within a family contributes equally. Thus the percentages are family-weighted averages, not simple pooled fractions of steps.

These were AI-authored educational challenge passages, using one fixed grade-six reader profile, app version, prompts and capped candidate procedure. This is a test of agreement with that app procedure, not a representative sample of all writing and not a human working-memory study. The reference disagreed across repeats at 282 steps. We retained 875 provisional steps and 908 steps carrying coverage warnings, as specified in advance. Provisional means at least one run marked that step's score as tentative. Coverage warnings apply to the whole passage and also include missing coverage metadata; they do not establish that every individual step was affected. No missing scores were dropped: 0 steps were missing.

The complete raw analyses were independently replayed through the frozen frontend. All 300 replays, three-repeat medians, source and reader-profile checks passed. The standalone calculator also matched the saved equations with networking and access to the original workspace denied. Those checks establish faithful implementation, not psychological validity.

Reference collection used documented original and amended transport settings. Repeated service-busy responses and timeouts prompted longer waits and retries of failed requests. The amended transport returned the first successful response unchanged and kept the original rules for judging its answer. Existing complete analyses, failures and unknown-cost reservations were preserved. This changes the collection procedure, while retaining the frozen score calculation and all equation predictions. The mixed collection history is included in the independent reference audit and final-results.json; it must not be described as identical execution throughout.

## Results for every frozen equation

|Equation|Exact match|Displayed-score error|Within one unit|Raw-score error|
|---|---:|---:|---:|---:|
|Direct score equation, selected for exact matches|44.5%|0.750|86.4%|0.754|
|Direct score equation, selected for smaller errors|44.8%|0.721|87.2%|0.747|
|Direct score equation, original measurements|43.4%|0.761|85.7%|0.762|
|Item decisions, original measurements|46.3%|0.766|85.0%|0.766|
|Item decisions, richer grammar measurements|47.5%|0.757|85.0%|0.757|
|Item decisions, grammar and word measurements|47.2%|0.747|85.2%|0.747|
|Add the expected item contributions|46.7%|0.691|87.1%|0.735|
|Item decisions, also using word frequency|47.1%|0.739|86.0%|0.739|
|Choose the most likely total|47.3%|0.681|88.3%|0.681|
|Choose the most likely total, with word frequency **(selected before the test)**|47.7%|0.683|87.7%|0.683|
|Previous best equation, unchanged|40.4%|0.742|87.7%|0.774|
|Previous primary equation, unchanged|38.5%|0.773|87.1%|0.790|
|Word-count baseline|37.3%|0.810|84.7%|0.849|
|Same selected method, trained on the earlier 488 passages|47.7%|0.685|87.4%|0.685|

Displayed-score error is the average distance between the equation's whole-number answer and the app's answer. Raw-score error uses the equation's defined unrounded output when it has one. Full descriptive 95% intervals are in final-results.json. The selected equation's exact-match interval is 43.14 to 52.16%; its raw-error interval is 0.601 to 0.771 units. The original target concerns both exact agreement and raw error.

## Which claims survived?

|Claim|Result that would count against it|Test and result|Status and limit|
|---|---|---|---|
|The selected equation reaches the original fidelity target.|Fresh-test exact agreement below 95% or raw-score error above 0.10.|47.7% exact; 0.683 raw error.|Point targets not met; this particular equation has not solved the task.|
|At least five percentage points more exact matches than the previous best.|The entire paired interval lies below +5 points.|+7.26 points; interval 2.42 to 12.16.|unresolved. Fixed designed sample and reference procedure.|
|Displayed-score error does not increase.|The entire paired error-change interval lies above zero.|-0.059; interval -0.123 to 0.005.|unresolved. Same reference and sampling limits.|
|Some better equation is possible.|This broad existence claim needs a specified equation class and conditions to be sharply testable.|Only the recorded candidate equations were tested.|Failure here does not show that every possible equation will fail.|

This follows Popper's critical approach by making particular proposed repairs risk failure, preserving failures and distinguishing the tested claims from broader hopes. The folds, saved prediction freeze and bootstrap intervals are modern statistical safeguards. A probabilistic performance claim is not logically disproved by one mistaken prediction.

## Matched comparisons, treated as exploratory

|Change|Exact-match change (points)|Unadjusted 95% interval (points)|Displayed-error change|
|---|---:|---:|---:|
|direct richer inputs|+1.13|-2.26 to 4.78|-0.011|
|component structure|+1.19|-3.14 to 5.38|-0.009|
|component lexical|-0.31|-3.18 to 2.72|-0.009|
|component count rule|+0.08|-3.49 to 3.51|-0.066|
|frequency hard|-0.12|-2.18 to 1.85|-0.008|
|frequency with count mode|+0.40|-1.00 to 1.83|+0.002|
|count rule with frequency|+0.61|-2.81 to 4.02|-0.056|
|added development data|+0.05|-2.91 to 2.86|-0.001|

These comparisons help diagnose possible improvements. They have unadjusted intervals and do not create additional confirmed discoveries or replace the primary result.

## What is usable now

The numerical equation and an offline calculator are delivered. They make no Jev requests after fitting, but still require local computation, the existing grammar parser and the specified software dependencies. The equation is a large collection of fitted numerical if/then rules plus arithmetic; it is not a short readability formula. See equation-explained.md for the plain-English explanation and full-equation.txt for every fitted numerical rule.

In a separate local timing check, the selected equation processed 20 development passages of 52–146 words, taking a median 1.13 seconds per passage after setup. These were new to that process; repeated, cached passages were timed separately. The calls included parsing, text measurements, model loading and scoring, with networking blocked. This is an observed timing on this machine, not a speed guarantee or an accuracy test. See local-runtime.md for the setup times and limits.

A useful next discriminating test would freeze a specific new repair, then test it on a new independently sourced set with the same reference procedure and comparison rules. A repeated gain there would increase confidence that the repair transfers; failure would count against it. Changing this equation after seeing this final set requires another fresh test.

The full research record, including failed candidates, operational service interruptions and preserved accounting, accompanies these files. Previous-round outputs remain unchanged.

## Reference usage

This continuation saved 900 full reference analyses: 600 for the 200 new development passages and 300 for the 100 final passages. Reported-token cost was estimated at **$73.14**. Conservative accounting including retained unknown-usage reservations totals **$440.31**; that larger number is not a confirmed bill. These figures exclude assistant use and local computation. The original request ledgers are counted once; recovery snapshots and merged copies add no new spending. See costs.json.

## Additional development tests

While the final reference answers were collected, three separately documented development experiments tested shared corrections, whole-number classification and a running score estimate. None met its prospective improvement rule. They did not change the frozen final equations or use this final test. See [the short follow-up summary](additional-experiments.md); all protocols, rejected equations and independent audits are retained in the research archive.
