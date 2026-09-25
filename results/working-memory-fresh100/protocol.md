# A new test of the unchanged equation

Question: On 100 new passages, how often does the frozen equation give exactly the same score as the Jev-based app?

The equation is `component_frequency_count_mode`, SHA256 `be1a6884cb99d4a7d56759c9ae81e8d75d4b140963cfc0e568908e023303d781`. No fitting, equation editing, winner selection or feeding these results into the separate autonomous search is allowed during this test.

1. Write 100 new educational passages in 50 pairs covering different topics, lengths and sentence structures. Check them for overlap with the existing material. Each pair changes a meaningful relationship or instruction; no expected score direction is imposed.
2. Save every equation prediction, the passages, the program versions and this protocol before requesting Jev's answers.
3. Run the same frozen app three times per passage: Jev `jev-1.13.0`, prompt `passage-2026-09-21.2`, two samples per question, the existing grade-six visible-text learner profile, and the existing app scoring procedure. Use the middle of the three scores at each reading step. Preserve missing results, disagreements and warnings.
4. Compare the saved predictions with those reference scores. Primary outcome: exact agreement. Secondary descriptions: within one unit, mean absolute error and signed error. Give each of the 50 passage families equal weight, and each step within its family equal weight, as in the earlier experiment. Also show the unweighted step count for transparency.
5. Calculate a descriptive 95% uncertainty interval by resampling whole families 20,000 times, seed 20260924. Compare with 45.61390328084203% (earlier five-fold development estimate) and 47.70801489518487% (the earlier fresh-test estimate). Neither is a known population truth. Do not claim that a similar number or an interval containing 45.6% proves equality. Do not quietly discard incomplete passages or publish a partial result as the final percentage.

This tests whether the equation's earlier approximate level of agreement survives new examples. A result clearly below the earlier level is evidence against that generalization under these conditions. All failures count; the equation stays unchanged. This is a Popper-style attempt to expose mistakes, with modern statistical safeguards, not a proof that the equation is correct.

Limit: these are newly authored examples, not a random sample of everything people read. The reference is the Jev-based app, not measured human working memory. Differences could reflect the new text mix or reference variability as well as the equation. A genuinely external corpus would be the next stronger test.

Collection is an ordinary resumable program, with one process and two concurrent analyses. It uses the previously tested timeout/retry transport, logs every paid request and retries only missing analyses. Limits: $500 of configured charged-or-reserved accounting, 200,000 requests, six collector invocations, 24 hours. These are generous guardrails, not predicted spending; the earlier test's recorded usage was about $30. Provider billing is not independently confirmed by this log.
