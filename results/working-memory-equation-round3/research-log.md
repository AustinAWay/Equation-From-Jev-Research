# Continuing research

User authorization removes the old financial cap while retaining approaches 1–3 and Popper-based testing. New work is isolated from all prior frozen outputs. The original capped scoring procedure remains the primary target; candidate-cap and repeated-median experiments are separately versioned diagnostics.

All previous168 passages /84families /752steps are now development material. Five shared family folds were fixed before fitting the new lexical/directed-feature equations. Larger corpus authoring, component modeling and reference diagnostics run independently.

## Direct lexical equation, first attempt

Before fitting, fixed45kernel configurations with continuous and rounded outputs:90candidates. New measurements preserve separate current/prior words, bigrams, grammatical roles and ordered entity/predicate/argument combinations, computed locally without pretrained language representations. Vocabulary and inverse-document frequencies fit within family folds. The chosen equation still used numeric inputs alone:MAE0.800044, exact38.12% across84development families. Best lexical mixture MAE0.8964669589669588. This does not corroborate the claim that this lexical encoding improves prediction at this data size. All90candidate predictions, configuration and fold coefficients remain saved. Exported final arithmetic matched the fitted equation. The failed feature addition will be retested on the larger prespecified development dataset without presenting that retest as an untouched final test.

## Directed memory ledger, initial development test

Before fitting, saved a repair hypothesis of at least0.05 MAE improvement over matched original inputs. Fifty configurations tested both original and repaired measurements under identical algorithms and family folds. The selected repaired equation achieved MAE0.799019/exact40.10%, compared with matched original inputs MAE0.869695 (gain0.070676), independently selected original MAE0.839313 (gain0.040294), and matched empty history MAE0.823556 (gain0.024537). This provisionally supports the particular input repair on development folds, but does not independently establish the claimed magnitude or 95% fidelity. Five focused checks passed: directed events, negation, unchanged original behavior, teacher-field independence, and future-text independence. Every fold and final equation passed numerical export parity.

## Score-distribution revision

Prospectively test whether exact-score objectives and keeping all three training scores improve exact matches. Sixteen softmax configurations, three output choices each, use numeric or numeric-plus-explicit-lexical inputs. Individual-repeat fitting uses the analytically derived median-of-three transformation, checked by enumerating triples. The initial fit source is preserved by its exact recorded SHA256 in direct/distribution168/source_at_fit_start.py. While fitting was in progress, a binary-class-only sparse-matrix length bug was fixed in the working source; this corpus has more than two classes in every fit, and the immutable run retains the original source. This engineering repair is separate from outcome-driven model revision.

## Collection throughput amendment — 2026-09-22T19:39:11.797425+00:00

Raise the operational combined concurrency ceiling from4 to8 full analyses by starting immutable developmentbatch02 at concurrency4, alongside two existing collectors at2each. Preserve the repeatability study and batch01 at their declared concurrency2; preserve original reader/model/prompts/scoring and every request reservation. This uses the authorized resources to reduce collection time. Monitor explicit rate-limit and upstream service errors; back off added collection if errors rise materially. This scheduling amendment changes neither targets nor the repeatability protocol.

## Old counterexamples retested

All five prior exact-input collision pairs are distinguished by the revised52 ledger measurements. Across all540 current development steps with three identical reference repeats, no conflicting exact52-feature vector was found. This removes the demonstrated old-input obstruction on these observed rows; it neither establishes information completeness nor successful extrapolation to new text. Full vectors and identifiers are preserved in ledger/collision-audit/results.json.

## Shared combination, initial test

On identical84-family out-of-fold predictions, the single shared equation round(0.2*direct +0.6*component +0.2*ledger) achieved MAE0.718167 and43.24% exact agreement. The exact-first choice round(0.4*direct +0.5*component +0.1*ledger) achieved43.42% and MAE0.721298. Against the strongest component model MAE0.73198, this falls short of the prospectively declared0.05 MAE improvement. It is development selection only; no domain routing is present.

## Score-distribution outcome on initial data

All48 direct distribution/output candidates completed with no convergence failures and export parity. Best exact-first configuration used numeric features, C0.1, all three individual repeats, the median-of-three transformation, and a median output:42.11% exact, MAE0.802819. This improved exact agreement over the initial direct kernel38.12% by3.99percentage points, below the declaredfive-point gain, with essentially unchanged absolute error. More complex lexical inputs did not win. This is a useful but insufficient repair on development folds, not success on the original target.

## First reference-repeatability result

All288 fresh analyses completed, covering147steps withnine scores each. Under benchmark-matched family→pooled-step weighting, median-of-three targets disagreed13.44% of the time, with95% family-bootstrap interval8.88%–19.16%. The corresponding upper-bound quantity on expected exact agreement is93.28%; its upper confidence endpoint95.56% does not exclude the original95% target. This first study therefore leaves that feasibility test unresolved. Pairwise score distance and the approximately0.07 lower-bound quantity are much smaller than the present approximately0.7 equation errors; reference variability cannot be used to explain away the whole modeling failure. A second16-family replication was selected and frozen before these numerical outcomes were inspected, and began19:55:32UTC. Allstage1scoring/source/config hashes passed audit.

## Throughput audit

A read-only audit found that the frozen backend shares four evaluation slots per event loop, each requesting two samples; increasing full-analysis concurrency within one saturated process is unlikely to help. The longer seconddevelopmentbatch needs more calls per passage. Keep existingcollectors unchanged. For the future finaltest, prospectively use two nonoverlapping whole-family IDshards with separateprocesses/ledgers and unchanged scoring. Merge only verifiedcomplete responses, retain original costs/timestamps, and require sealed predictions before either collectorstarts. No duplicate IDs or sharedmutable ledgers. This is an operational change, not a reference-target change.

## Development completion guard — 2026-09-22T20:03:53.828822+00:00

Longer passages require more individual Jev requests per full analysis. Batch02 may reach the original50,000-request operational guard before all360 planned analyses finish. A completion coordinator waits for each running collector to checkpoint and release its lock, then performs up tothree cache-aware passes for missing analyses only. On resumed passes the request guard is100,000, with the existing$50 cost guard and unchanged profile/model/prompt/samples/concurrency. Prior paid calls, unknown reservations, errors and valid cached outputs are retained. No parallel writer shares an output ledger. The coordinator releases the408-passage fit file only after matching every complete label repeat to its raw scored output and verifying identical reference source/profile acrossallfour data roots.

## Raw-text segmentation guard — 2026-09-22T20:30:26.053539+00:00

Before final-corpus text or labels were opened, strengthen the final prediction sealer to require the portable raw-text runner to extract exactly the same step identifiers and UTF-16 offsets as the frozen reference runtime for all80 final passages. Different local spaCy library versions make an explicit parity check worthwhile. This is a fail-closed implementation check, with no change to the model, target, or outcome criteria. It runs after model freezing and before paid final requests. The evaluator's three arithmetic/guard tests still pass.

## Replicated reference variability

The independent second16-family study completed all288 analyses, with11.03% benchmark-weighted median-target disagreement (95% family-bootstrap interval5.39%–17.26%). The prespecified pooled32-family result is12.234% (8.434%–16.381%). Under the original indicator bound, the upper confidence endpoint is95.783%; under the separately recorded conditional-IID collision bound it is95.690%. Neither excludes95% expected exact agreement. The latter deduction was post hoc for first-stage data and prospective before inspecting second-stage/pooled outcomes; pooling does not make its first-stage use prospective. All576 repeated analyses/294steps have complete nine-run scores. The estimated MAE lower-bound quantity is0.06528, much smaller than present model errors. Reference noise does not explain all the predictive failure. Full derivations, audits, assumptions and reservations remain preserved.

## Secondary final controls

Before any expanded fitting results or final reference answers, add frozen initial168 counterparts of the four fixed configurations to the final prediction seal. Compare them with their408 fits as exploratory paired contrasts; the additional data also change text length/content/domain mix, so this does not isolate quantity alone. Retain matched ledger controls, lexical components, genuine-choice secondary, and blends against a constituent chosen on development data. The six adjusted primary contrasts remain unchanged. secondary-comparisons-protocol.md and its locked runner define ten unadjusted descriptive comparisons; their hashes will be included in the sealed bundle registry.

## Targeted completion after connection failure — 2026-09-23T00:34:58.409363+00:00

The bounded coordinator ended with359/360 batch02 analyses after three resume passes; r3d_111_b repeat1 remains absent after timeout/connection failures. All original collectors have exited. Resume only that passage using the unchanged original collector/profile/repeats/samples/concurrency and existing ledger, with the same$50/100000-request runaway guards. Cached valid analyses are retained. This operational recovery does not select scores or modify any model or target. Existing fit waiters remain gated on a complete release.

## Complete expanded release — 2026-09-23T00:37:25.915809+00:00

Targeted recovery completed the last absent analysis in22.023 seconds, reusing both valid cached repeats. The released development set contains408 passages/204 families/2325 steps and1224 full analyses. Every repeat target matched its stored raw score and every source/profile identity matched the frozen procedure. Direct and ledger fits began00:35:41UTC on2026-09-23; component fitting began after its independent manifest/cache audit. The final corpus remains sealed.

## Guarded continuation — 2026-09-23T00:57:25.361619+00:00

The continuation runner waits for explicit expanded-fit readiness and independent pre-final audit markers. It then selects the prespecified shared blends, freezes all model assets, verifies the portable package on development text only, extracts final steps, seals predictions, and starts the two frozen reference-collection shards. Evaluation follows only a verified complete merge. Each stage stops on nonzero exit and retains its separate log; this scheduling change does not alter candidate models, score targets, success criteria, or the untouched-final-data boundary.

## Inference efficiency repair, before final access — 2026-09-23T01:26:18.740956+00:00

The original full lexical export verification is still running and remains unchanged. Its recursive evaluator copies all 14,063 input columns at each tree node. A separately versioned inference-only wrapper is being evaluated for the lexical component equation: carry row indexes instead, preserving float32 inputs, float64 split comparisons, leaf values and tree summation order. Original model parameters, fitted outputs and source are retained. This is a computational repair, not a new feature, model or outcome-selected candidate. Require exact branch/boundary and representative saved-tree comparisons plus independent review before changing the portable registry. The continuation runner was safely restarted while still waiting, with an additional absent root integration-ready marker so that registry/source audit updates must complete before any final passage is opened. Original waiting log is preserved.

## Full export verification and reconciliation — 2026-09-23T01:51:28.436164+00:00

The same-configuration additional lexical fit completed full native-versus-fast verification on29,290 role rows and2,325 extra-count rows, with maximum absolute differences below1e-15. The original slow verification then completed independently before any handoff: the handoff guard refused before sending signals or copying files. The two complete model JSON files are byte-identical. Both full checks and representative original-versus-fast comparisons are preserved. The original canonical export and unchanged choice job remain in use; only lexical portable inference uses the reviewed row-index evaluator. Earlier notes describing the original export as pending are historical status reports, superseded by this completed comparison. Verification time allowances increased to3,600s for isolated package checks and600s for each CLI check, with all scientific checks unchanged.

## Recovery after connection gap — 2026-09-23T12:43:57.358578+00:00

The component coordinator completed the unchanged choice fit and final summaries at03:57:54UTC. The agent connection was interrupted and resumed at12:42UTC; the guarded continuation remained waiting for independent readiness/integration markers throughout. No final passages, predictions or reference requests had been accessed by that pipeline. All completed artifacts are retained. The choice variation produced development MAE0.80511886299 and38.6171% exact agreement; all five optimizers converged. Finish provenance wording and readiness audits, then proceed from these completed files without refitting.

## Independent arithmetic after library warnings — 2026-09-23T12:53:02.386713+00:00

NumPy matrix products emitted divide/overflow/invalid warnings despite finite saved outputs. Independent non-BLAS arithmetic checked all132 blend candidates and every selected development prediction: winners and rounded scores match, largest metric discrepancy8.9e-16. Explicit distance calculations and Python math.fsum checked5.97million kernel entries and all3,077 saved center inputs for the initial/expanded direct equations: all finite, zero rounded-score changes, maximum raw discrepancy2.53e-13 versus nearest rounding margin1.70e-4. The warnings are preserved and their library cause remains undiagnosed; these tested numerical outputs are corroborated independently. No fitted parameters, source, registry, final inputs, or selection rules changed.

## Portable dependency inclusion repair — 2026-09-23T13:12:42.146396+00:00

The isolated expanded-bundle check failed when the already selected choice equation imported `joins.py`, which imports `grammar.memory`. The source-only support list omitted that existing helper. A new relocated-import regression reproduced this exact failure before the change. Added only `round3/components/grammar/memory.py` to the packager's support files. The helper is byte-identical to the frozen app source (SHA256 `224ce28b2a482fee00a89cd77d1132543be1131002a7c0af6982213c0cb898f9`) and has no additional imports. No equations, numerical model files, registry choices, or scientific thresholds changed. All 14 registered model entries now import from a separate temporary source-only tree while access to the original workspace/app and networking is denied; no predictions or reference calls ran in that check. All eight existing packaging tests also pass.

The failed artifact is preserved at `package/bundle-final-before-support-fix`, with its original verification log at `continuation-package.log`. The coordinator will rebuild `package/bundle-final` from the unchanged frozen registry and rerun complete development-text parity verification before any final input or reference call. This targeted check establishes dependency availability only, not full prediction parity or accuracy. No final corpus or data was opened for this repair.

## Independent probability-output arithmetic — 2026-09-23T13:20:46.373804+00:00

The distribution warning was reproduced with unchanged full-fit inference on752 initial and2,325 expanded source-only development rows. All probabilities were finite and within[0,1], with row sums within2.22e-16 of one. Independent Python multiplication/math.fsum expectations differ from matrix products by at most8.88e-16; every scalar-CDF median and rounded mean matches. Networking was blocked with zero attempts. This corroborates these full-fit numerical outputs, not the absent saved out-of-fold probability vectors; the prior limited audit remains preserved. The library warning cause remains undiagnosed. No model, selection, source, protocol or final input changed.

## Additional development input diagnostic and contextual reading — 2026-09-23T13:51:34.108204+00:00

After freezing all equations, a separate development-only audit checked exact equality of the direct equation’s271 measurements. All saved center rows were verified against their source/cache order. Among2,325 rows,411 duplicate pairs include57 with conflicting median targets:51 share the same prefix and boundaries but differ later, while6 differ in available text. Independent rational arithmetic reproduces the finite-sample optimum of98.024% exact agreement and minimum0.02149 absolute error for unrestricted deterministic functions of those inputs. These conflicts prevent perfect replay of these recorded labels but neither exclude95%/0.10 goals nor explain most observed error. No equation was revised. A separately labeled contextual appendix reviews three primary sentence-comprehension papers and proposes a future matched test of unfinished requirements/new intervening information; that proposal was not run and changed no current model or final analysis.


## Final collection, independent audit and delivery — 2026-09-23T14:20:28.724836+00:00

All 16 prediction sets were sealed at 13:40:13.727886 UTC before any final reference calls. A launcher failure then exposed an interpreter-path issue: resolving the virtual-environment executable selected the base interpreter without its required parser. The narrowly reviewed operational amendment changed that path handling only, preserved the original source/lock and zero-call failure, and left every equation, prediction, reference setting and criterion unchanged. Recorded chronology is seal < amendment at 13:49:24.438189 < collection plan at 13:53:02.518498 < first request at 13:53:04.375963. The full repair and independent review remain in final_collection/interpreter-path-repair/ and reference-audit/final-operational-chronology.json.

The final 80 passages / 40 families / 566 steps have 240 complete analyses and no missing scores. Three upstream failures were recovered without replacing valid cached outputs. The independent audit replayed every stored analysis and all 16 equations' summary statistics, six adjusted primary comparisons and ten secondary comparisons; discrepancies were below 1e-11. Every equation missed the original 95% exact-agreement and 0.10 raw-error targets. The development-selected blend achieved 38.50% agreement; the highest main candidate was components at 40.47%, while the secondary lexical variation reached 42.98% descriptively. These observed ranks do not validate a new selection after inspecting the test.

The component equation reduced displayed-score error from 0.8020 to 0.7290 compared with the unchanged earlier component baseline. Its adjusted gain interval [0.00275, 0.14139] supports some improvement, but leaves the predeclared 0.10 magnitude unresolved. Matched larger-data comparisons favored the expanded fits; changed content/length/domain mix prevents attribution to quantity alone. Lexical inputs, ledger history and blends showed no clear advantage in their secondary comparisons; the grouping-choice variation was worse. Failed and uncertain revisions remain reported.

The final reference collection cost is estimated at $12.05 from reported usage or $12.78 retaining unknown-usage reservations. Across all rounds the corresponding totals are $75.41 and $79.77, excluding development-tool usage/local compute and not representing invoices. Independent report review found no numerical or scientific overclaim; requested clarifications were incorporated about secondary failures, all-16 fidelity failure, half-up rounding, raw versus displayed error, and the development-only scope of collision bounds. The report generator now binds its audit to the exact result-file hashes. Delivery archives will preserve both successful checks and the original failure evidence. This completed test challenges the specific equations' performance claims; it does not establish impossibility for all equations or validate human memory measurement.
