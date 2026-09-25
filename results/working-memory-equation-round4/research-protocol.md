# Round 4: learn the score more faithfully

Written before round-4 fitting or new reference collection. User requested further attempts after round 3. Prior outputs and archives remain immutable. This is continued exploratory equation discovery within approaches 1–3; no passage-specialist routing or new pretrained semantic helper is permitted. Equation length is unrestricted.

## Question and repair claims

Can richer measurements of the available text and explicit candidate structure, together with a fitting objective aimed at the final whole-number count, improve an offline equation's agreement with the fixed app procedure?

The previous component calculation adds expected small decisions and rounds once. That does not generally equal the most probable final count. It also compresses available relationships into limited measurements. These are proposed explanations of errors, not established causes. We will compare final-count classification and regression using the same measurements, and compare richer structural measurements with the original measurements. An independently diagnosed component revision may use intermediate labels; its exact proposal must be recorded before its fitting starts.

The available-prefix rule remains: current-step and earlier text may supply semantic measurements; later text cannot supply semantic evidence. The reference's existing full-passage extraction can supply its exact candidate spans and locally visible grammar. The same equation applies to all passage types. No domain IDs, family IDs, author labels, split names, reference decisions, or reference scores enter prediction inputs. Reference decisions and scores are training targets only.

## Data boundaries

All 488 earlier passages (244 paired families, expected 2,891 reading steps) are development material now, including round 3's former final test. We will never describe success on those rows as fresh confirmation. Preserve original source provenance and relabel the combined inventory explicitly as development.

Add 200 independently written development passages in 100 paired families, balanced across ten educational domains and three lengths. The corpus author first specifies and writes a separate 100-passage/50-family final set, seals it, then writes development in two immutable 100-passage batches. Final text is withheld from fitting agents until models are frozen; its scores are never requested until all final predictions are saved. Both sets are AI-authored; shared authoring and designed sampling limit generalization. Paired variants stay together. Review exact duplicates and substantial word overlap against prior texts and between sets; overlap checks do not establish complete independence.

New development and final use the unchanged fixed grade-six profile, parser/reference model, prompts, three analyses per passage, and original capped candidate procedure. Keep all complete scores, including provisional ones. Missing scores stop release/evaluation rather than being silently dropped. Retry missing analyses only and retain valid cached results and all cost/error logs.

## Development comparisons and selection

Use five deterministic whole-family folds, seed 20260930, shared across candidate comparisons. Keep variants and closely related scenario rewrites in one family. Fit vocabulary/scaling/model parameters inside each fold. Existing immutable feature-only caches may be reused; target-derived predictions from an equation trained on an evaluation family's labels may not be used as supposedly out-of-fold inputs.

The direct branch will examine original numerical inputs, richer candidate/grammar inputs, and explicit lexical measurements, with fixed candidate lists recorded before each search. Compare equations fitted to median final scores, classifiers of those scores, and permitted count decompositions. Classification may report its mode or median; regression rounds half upward after clamping at zero. Exact exported arithmetic and its raw value must be defined per model. Candidate selection, failed fits, configurations and predictions are retained. Development scores are exploratory after this adaptive search.

Choose one primary new equation by highest equal-family exact agreement on complete out-of-fold predictions, with lower displayed-score absolute error then a fixed lexical name as tie-breakers. Also preserve a separate lower-error candidate if different, and any useful matched measurement/objective controls. Before final labels, record all selected models, complete input dependencies, metrics, export checks, and their hashes in a locked registry. Any adaptive revision after the final test requires new test passages.

## Fresh test and possible falsifiers

Original desired fidelity is unchanged: at least 95% exact whole-number agreement and mean absolute raw-output error at most 0.10 units. This experiment also tests a narrower incremental claim: the primary new equation improves whole-number agreement over the unchanged round-3 lexical component equation by at least five percentage points, without increasing mean displayed-score absolute error. The comparator is selected before this new test; its previous 43% result is historical, not the score to subtract from a new population.

Use the median of three reference scores at each step. Average each metric over steps within a scenario family, then give each family equal weight. The paired whole-family bootstrap uses 20,000 resamples and seed 20261001. For the two incremental claims use two-sided 97.5% percentile intervals (Bonferroni nominal 95% jointly). An exact-gain interval wholly below +0.05 contradicts that gain magnitude; wholly above +0.05 provisionally supports it; crossing leaves it unresolved. For error change (new minus comparator), an interval wholly at or below zero supports no increase, wholly above zero contradicts it, otherwise unresolved. Both claims must survive for the combined improvement claim. Report all point metrics and descriptive 95% intervals; success does not establish a universal equation.

Matched controls are secondary exploratory comparisons with clearly labeled unadjusted intervals. Also show the unchanged round-3 main component equation and word-count baseline on these same passages. Do not select a new validated winner from final results. Claims concern agreement with the fixed app, not human working-memory validity.

## Reasoning and checks

Follow Popper by making repairs risk failure, preserving counterexamples, testing measurement and implementation alternatives, and stating which particular claim survives or fails. Family folds, bootstrap uncertainty and saved prediction freezes are modern safeguards, not inventions attributed to Popper. Probability statements are not logically refuted by any single error; the specified performance claims require the stated sampling and measurement assumptions.

Check faithful offline export, no target/ID leakage, complete scores, source and profile identity, prediction-before-reference chronology, and calculation reproducibility. Document narrow operational repairs separately; preserve original evidence and forbid outcome-driven changes to frozen scientific rules. Operational spending/request guards protect against runaway processes, not a user budget cap. Final documentation must explain the equation and actual improvement in plain language.
