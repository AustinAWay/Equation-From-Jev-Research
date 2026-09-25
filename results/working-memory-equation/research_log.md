# Equation discovery research log

## Objective
Discover a mathematical equation, with no length or complexity limit, that reproduces frozen Passage Jev-based per-reading-step scores on unseen passages using local text measurements only.

## Decisions made before data collection
- Use the existing application scoring code, not a newly invented Jev rubric.
- Freeze source version, reader profile and model.
- Start with 60 independently authored passage families, two variants each: 36 train, 12 validation, 12 sealed test families. Final coverage is a pilot, not a broad claim across all text.
- Related variants and repeat runs remain in the same split. Equal family weighting for headline metrics.
- Target is median of three available full analysis runs; missing and provisional labels remain visible. Preserve all raw responses.
- Features use source text available by each step and never teacher outputs. All text measurement and prediction must run offline.
- Select candidates using train and validation only. Open test once after freezing a candidate. If later inspected for revision, retire those cases from final validation.
- Proposed targets retained from approved plan: >=95% exact rounded agreement and <=0.1 mean absolute error, with simpler baseline comparisons. No claim of success from training accuracy.
- No penalty or rejection merely for equation length. Explore weighted, nonlinear and piecewise mathematical expressions.
- Document short scientific rationales, parameters, measurements and outcomes, not unverifiable retrospective narratives.

## Execution record
- Located configured local app and isolated read-only source copy. Credentials stay in the existing local configuration and are never copied into research artifacts.
- Delegated independently authored corpus, local feature measurements, and exact application-score recording.

### First live pilot
Two real Passage analyses returned all nine step scores. Reported API cost was $0.052649478 across 181 HTTP requests, including the app's internal samples and retries. The pilot established end-to-end extraction and exact frontend score recording; one run per passage does not establish repeatability. Proceed with three runs per passage, within a $15 experiment ceiling. Keep source, profile, prompt and samples fixed.

### Pre-fit safeguard review
Independent review found and corrected potential stale-fit reuse when adding data, missing train/test family checks, and repeat-metadata defaults. Candidate identity now includes eligible development data, feature implementation and repeat count. Final opening permanently records access before evaluation, including failed attempts. Freeze the strongest simple comparator with the candidate. The simple baselines are training mean, step word count, and the two reading-level ingredients (sentence length and average syllables); they are fitted to these scores rather than assumed to measure memory.

### Additional pre-fit equation family
Include radial equations: a weighted sum of exponential terms measuring similarity in standardized local text measurements. This is a continuous alternative to piecewise conditions and can represent a long nonlinear equation directly. Hyperparameters cover 16, 32 and all 231 measured inputs, three smoothness levels, and three regularization strengths. Added before inspecting development results. Export parity is checked on fresh synthetic values.

### First qualitative reference finding
For the identical step “Cover several leaves with a clear bag,” the completed three-run targets are [{"id": "science_01_a", "target": 2, "repeat_targets": {"1": 2, "2": 2, "3": 1}}, {"id": "science_01_b", "target": 1, "repeat_targets": {"1": 1, "2": 1, "3": 1}}]. The phrase occurs in different preceding contexts. A step-length-only equation cannot distinguish these cases. This supports retaining the already planned context/repetition features; it is not yet a test of a new fitted equation. Jev itself varies on some steps, so repeated-score stability is reported independently.

### Engineering pilot: first fitted equations
While reference collection continued, froze 64 complete reading-step labels from seven science families that all belong to the permanent training partition. Used five families for fitting and two for temporary error inspection; this is explicitly not the final validation or test result. The snapshot and assignments are preserved in pilot-labels.jsonl and pilot-manifest.json.

86 configurations completed. Best continuous pilot equation was polynomial_k8_d2_a0.1: temporary-validation MAE 0.633253, exact agreement 44.95%. Reading-ingredient baseline MAE was 0.798976; length-only baseline 0.833299; constant mean 1.012650. A different polynomial achieved 64.14% exact agreement with MAE 0.698293, illustrating that the two objectives can disagree. All pilot claims are restricted to two temporary evaluation families.

Largest mistakes included overestimating a descriptive evaporation/condensation sentence (2 versus 3.552), and underestimating instructions to place a fulcrum (3 versus 1.715) and draw connections between water-cycle stages (6 versus 4.931). Hypothesis for the next revision: generic action/argument measurements may distinguish manipulating several relationships from describing a familiar process. This is a hypothesis from observed errors, not a demonstrated cognitive mechanism. Add 20 topic-independent prefix-local features and rerun the exact same pilot; retain both versions and report whether the revision helps.

### Integer-output experiment
The reference is an integer count at each step. In addition to continuous equations, test an explicit max(0,floor(f(x)+0.5)) equation. Preserve the underlying continuous errors as pre_round metrics; label integer outputs honestly. Apply this option to simple baselines too. There is no change to the success thresholds, and final selection still uses only development data.

### Final comparison precision
Before any test collection or inspection, add a paired passage-family bootstrap interval for the difference in test MAE between equation and baseline, in addition to equation accuracy/error intervals. Resample the same families for both methods, 5,000 draws with a fixed seed. A positive point improvement alone will not be described as a firmly established advantage if its interval includes zero. Export baseline predictions alongside candidate predictions for audit.

### Action-feature revision result
On the identical 64-row temporary pilot, the best continuous v2 equation improved MAE from 0.633253 to 0.4809930395914926, with 65.15% exact agreement. The integer-valued version of that equation reached MAE 0.348485 and the same exact agreement. These are pilot-selection results on two families; improvement must still survive the full development and untouched final evaluation. Retain v2 for the broader search. Full precision is in pilot-runs-v2/iterations.jsonl.

### Export defect caught by parity checks
One v1 random-forest candidate was rejected because an exported prediction differed from the fitted model by about 0.0012. Diagnosis: NumPy 2 weak scalar promotion could round a double-precision tree threshold to float32. Corrected comparison to preserve float64 thresholds after input float32 conversion, matching sklearn. Added a boundary regression check. The failed attempt stays in the audit log; it was never selected. Subsequent full searches use the corrected evaluator. Thus v1 had 87 attempted configurations, 86 accepted; v2 had 87 accepted before integer variants.

### Midpoint development snapshot
After all science and history development references completed, freeze midpoint-labels.jsonl: 48 passages and 207 reading steps from those two domains. Retain original train/validation assignments (36 training passages, 12 validation passages). This larger intermediate snapshot is used to inspect generalization and direct symbolic search while practical/everyday reference collection continues. It contains no final-test cases. Results will be superseded by a fresh fit on the complete development dataset, not silently reused.

### Midpoint outcome and second error-driven revision
All 90 continuous configurations (including three direct symbolic searches) and their 90 integer variants completed with no export errors. Best midpoint integer equation: rounded_ExtraTreesRegressor_leaf2, validation MAE 0.5517 and exact agreement 51.45%. Its training MAE is only 0.0204, so fitting the available examples closely is plainly insufficient. Best direct symbolic equation has MAE 0.606680. The step-length baseline has MAE 0.6643. The temporary pilot's stronger percentage did not carry unchanged into the broader development set.

Persistent, stable-reference errors include “Label both angles beside the diagram.” (4 versus predicted 2), “because both cubes occupy equal volumes.” (1 versus 3), and a stations/times ordering instruction (2 versus 4). Hypothesis: aggregate grammatical categories discard specific logical/reference distinctions and word familiarity. Test a v3 feature extension with common reference/equality word counts and local word-frequency measures, all computable from the prefix without Jev. Preserve v2 and compare on the identical midpoint snapshot. These proxies may fail; they do not solve semantic grouping by assumption.

### Reference/frequency revision result and full comparison decision
On the unchanged 207-row midpoint snapshot, v3's best integer equation achieved MAE 0.540043 and 55.68% exact agreement, compared with v2's 0.551677 and 51.45%. Its best continuous MAE was worse (0.616421 versus 0.606680). This is a modest, mixed improvement, not proof that the added variables explain memory. Retain all 271 measurements for the main search, but also refit the complete v1-only and v2-only candidate families on exactly the same full development split. This lets the broader evidence select among measurement hypotheses and preserves the possibility that an earlier version generalizes better. No final-test information has entered these decisions.

### Independent pre-final implementation review
Review confirmed integer wrapping, radial exports, float threshold correction and paired family bootstrapping. Corrected output labels to distinguish equation outputs from underlying continuous values; final predictions retain both when applicable. Printed equations now state protected arithmetic and tree input-conversion conventions. Added nonfinite/shape rejection to prevent invalid formulas being recorded as successes. Extracted the exact arithmetic evaluator into equation_runtime.py (NumPy only); the offline runner no longer imports fitted-model/training libraries. Fresh-process tests forbid those imports and block network calls.

### Full development collection completed
Collected three analyses for all 96 development passages: 437 eligible reading steps, no missing aggregates and no invocation failures. Froze development-labels.jsonl before the main fit. The fitting process reads only that development snapshot. Reference collection for the preassigned test partition runs separately into sealed caches; no test texts, feature matrices or target values will be used for selection. The final evaluator freezes the selected equation and baseline before reading test labels for evaluation. Analysis concurrency is increased from two to four for this last collection stage; model, prompts, profile, internal samples and scoring functions remain unchanged.

### Preserve the original error threshold
Before opening the final test, make the success check conservative for integer-output equations: also require the underlying continuous equation's MAE to meet the original <=0.1 unrounded-error target. Rounding can improve count prediction, but cannot manufacture success against the earlier unrounded criterion. Report both errors explicitly. Candidate comparisons still include both output types, with final selection based on development MAE and agreement.

### Final candidate selected before test inspection
{
  "name": "rounded_v1_boosted_absolute_error_depth5_n400",
  "selected_at_utc": "2026-09-22T18:11:15.123039+00:00",
  "selection_rule": "Minimum development-validation family-weighted MAE; ties resolved by higher exact agreement. No length penalty.",
  "validation": {
    "rows": 106,
    "families": 12,
    "mae": 0.5869047619047619,
    "rmse": 0.8626969524381269,
    "exact": 0.491765873015873,
    "within_one": 0.9213293650793651,
    "bias": 0.018620731120731128,
    "max_error": 2.0
  },
  "training": {
    "rows": 331,
    "families": 36,
    "mae": 0.17130254005254006,
    "rmse": 0.46453600188112115,
    "exact": 0.8484177859177859,
    "within_one": 0.9828049265549266,
    "bias": -0.04343534551867886,
    "max_error": 3.0
  },
  "equation_sha256": "f61a1c5b812eea86e4108dbc55a6cacecf39a69d254f76189993feadd2f85077",
  "development_data_hash": "43e823c8e9928c187fe23c801eff1b98df303dabb610ee03f73da68ec095436b",
  "feature_hash": "7928287c39bb1db956d7f5006c02515492973aa7660f675a7054090f134e450f",
  "candidate_count": 540,
  "test_labels_inspected_for_selection": false
}

The original feature set won by the error-first comparison used throughout development. Added action/frequency measurements helped some intermediate cases but did not produce the best full-development candidate. The near-runner-up had higher exact agreement but marginally higher MAE; retain the error-first selection rather than switch the rule after seeing the candidates. No test result influenced this choice.

### Final untouched-test outcome
The frozen candidate was evaluated once on 24 unseen passages / 12 families / 107 reading steps. It matched 31.1947% of rounded scores, with MAE 0.966378 count units. The continuous base MAE was 0.952195. The frozen word-count comparator had MAE 0.930934 and exact agreement 26.3564%. Paired error improvement was -0.035444, with 95% family-bootstrap interval [-0.144374, 0.076470]. Therefore there is no demonstrated error advantage over the simpler baseline, and both proposed success targets are missed. Equation accuracy interval: 24.07%–38.94%. This is a negative result for the tested approach, not a proof that all equations must fail.

Do not select a different formula using these test results, refit against these cases, or silently reuse them as a fresh test. Subsequent inspection is diagnosis only. Any next fitting experiment must use a new final-test collection.

### Completion checks and accounting
All 120 passages have three full analyses, yielding 544 complete step references. Of those, 520 are provisional in Passage and 447 have limited coverage flags; 155 steps vary across repeats. All 24 final-test passages reproduce the stored reference reading boundaries in the local predictor. A full offline run with network access blocked exactly reproduces the frozen equation outputs for the first alphabetically selected final passage; no example was selected for being a good fit.

Provider-reported usage cost: $9.87259808; charged-or-reserved total $9.96088187. Four HTTP 529 responses did not report usage and retain conservative reservations. Retries completed all references. This is not a reconciled invoice. No further paid calls are planned for this completed pilot.
