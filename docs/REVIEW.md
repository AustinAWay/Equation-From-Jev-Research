# Publication review

This review checks whether the release supports its own claims. It is a computational and methodological review of the existing work, not peer review or an independent replication.

## Corrections made in the public presentation

1. The target is the fixed Jev-based app score. Human cognitive load and working memory are not established outcomes.
2. The 43.4% spline result is a highest observed comparison result. The development-selected Gaussian equation scored 42.0%.
3. The reused 100-passage set is explicitly marked exploratory in the later experiments.
4. The flexible word-count control (42.5%) and the earlier larger model (47.3%) appear beside the new equations.
5. The constant-score baseline is identified accurately; it is not described as random guessing.
6. Family-weighted percentages refer to reading steps, not entire passages; differences are expressed in percentage points.
7. Model size, target variability, provisional scores, coverage flags and transport amendments remain visible.
8. Failed trials, conflicting-feature examples, null comparisons and numerical convergence failures remain in the research record.

## Fresh release checks

[reproduction.json](../provenance/reproduction.json) records recomputation of the eight-model comparison table, exact replay of 4,550 predictions, all 910 raw-text feature rows, the five grouped folds, and 5,636 median reference labels. The selected equation's bytes match its saved selection hash. The publication audit also checks earlier final-test arithmetic and raw repeat records; see the machine-readable checks in `provenance/`.

Archive preparation checks source-file hashes while copying, records explicit exclusions, checks credentials before upload, and verifies the resulting ZIP members and published SHA-256 checksums. A second publication pass removed personal machine paths, a quoted operational instruction and unnecessary tool-specific wording. Rechecked model parameters, corpus text, scores and predictions remain unchanged. Local verification establishes that the released computations match the saved experiment. It does not establish that the experiment's sample is representative, that its scores are psychologically valid, or that a metadata timestamp is independent evidence of blinding.

## Strongest next test

Select and freeze a concrete repair to order/reference features using development data only. Compare it with a flexible word-count baseline on a separately sourced corpus and on length-matched reference/order pairs. Keep grouping, missing-data handling, reference settings and success thresholds fixed in advance. Human validation is a separate necessary study for claims about people.

## Sanitized publication revision

The replacement release generalizes personal machine paths and unnecessary operational wording in 469 files. All 16 other dataset/model exports are byte-identical to the first publication; the component-model export differs only in provenance path keys. All compact-model replays still pass, and all eight archived offline-package integrity manifests were checked after their dependent hashes were updated. The earlier download release has been withdrawn. Prior commits and copies made while the first publication was public may still exist; this replacement is not a claim of retroactive erasure.
