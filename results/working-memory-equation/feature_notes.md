# Local prefix features

`features.py` implements `extract_features(passage, start, end) -> dict[str, float]`.
Offsets use JavaScript UTF-16 units. The end is exclusive. Offsets that cut a
surrogate pair, fall outside the source, or are invalid types are rejected.

Version: `local-prefix-features-v1`. Runtime verified with Python 3.9.6, spaCy
3.8.11, and the installed `en_core_web_sm` package. Freeze the parser/model
versions alongside a fitted equation: parser changes can change features.

## Data boundary

The source is truncated before parsing. Only characters through `end` enter
spaCy. The later suffix cannot affect feature values, parser decisions, or
Unicode validation. No teacher calls, outputs, groupings, probabilities,
capacity settings, row identifiers, topic labels, dataset partitions or learner
outcomes are inputs. No corpus or generated targets were inspected while
developing this extractor.

The API assumes the study has already fixed the reader context. It does not
infer the learner's subject knowledge, comprehension or working-memory capacity.

## Inventory: 231 measures

71 measures are computed at each of three scopes:

- `step_`: the requested text range `[start,end)`.
- `prefix_`: all available text `[0,end)`.
- `sentence_`: the final parsed sentence in that prefix, up to the reading point.

The following are the 71 suffixes shared by those scope prefixes:

```
characters words syllables mean_word_length max_word_length mean_syllables
polysyllabic_words long_words short_words sentences words_per_sentence
content_words unique_content_lemmas content_density repeated_lemma_ratio
unique_nominal_lemmas repeated_nominal_mentions unique_proper_lemmas stopword_ratio
noun_chunks mean_noun_chunk_tokens max_noun_chunk_tokens max_nominal_modifiers
named_entities unique_named_entities person_entities quantity_entities numeric_tokens
candidate_concepts candidate_relations candidate_total
clause_heads subordinate_clauses relative_clauses coordinated_predicates
coordinated_nominals mean_syntax_depth max_syntax_depth max_subordinate_depth
mean_dependency_distance max_dependency_distance long_dependencies
internal_dependency_distance_sum conditional_markers causal_markers negation_markers
comparison_markers temporal_markers demonstrative_markers definition_cues
passive_subjects modal_verbs commas semicolons colons parenthesis_pairs question_marks
flesch_kincaid_grade flesch_reading_ease
pos_noun pos_propn pos_pron pos_verb pos_aux pos_adj pos_adv pos_adp
pos_cconj pos_sconj pos_num pos_det
```

18 additional measures connect the reading step with available earlier text:

```
prior_words prior_sentences prior_definition_cues prior_unique_nominal_lemmas
step_content_mentions_seen_before step_content_mentions_new step_seen_content_ratio
step_mean_mention_recency_tokens step_max_mention_recency_tokens
step_mean_previous_mentions cross_step_dependency_edges
cross_step_dependency_distance_sum cross_step_dependency_distance_max
step_mean_nearest_nominal_distance step_max_nearest_nominal_distance
step_mean_available_nominal_antecedents step_words_before_in_sentence
reading_point_sentence_index
```

## Interpretation

- Words are Unicode alphanumeric word spans, allowing interior apostrophes.
  Syllables use a declared English vowel-group heuristic, not a pronunciation
  dictionary. Flesch outputs therefore are approximate baselines.
- Content words are non-stopword nouns, proper nouns, verbs, adjectives or
  adverbs. Repetition uses lowercase lemmas. Nominal uniqueness uses noun and
  proper-noun lemmas; it does not resolve real-world identity.
- `long_words` means at least seven characters; `short_words` at most three;
  `polysyllabic_words` means at least three estimated syllables.
- Syntax depth counts ancestors in the prefix parse. Dependency distance counts
  spaCy token positions, including punctuation. `long_dependencies` means a
  distance of at least five token positions. Non-internal distances may reach
  earlier text outside the step, but never later than the reading point.
- Cross-step edges connect a parsed dependent and head on opposite sides of
  `start`. They are observable grammatical edges, not measured maintained memory
  bindings or a claim about an unresolved future dependency.
- A candidate is a local noun-phrase, nominal, predicate or value occurrence.
  The convention is inspired by Passage's extractor but implemented independently
  on the prefix. It neither calls nor reproduces Jev grouping. Counts need not
  match Passage's full-text parser, and no equality is assumed in the study.
- Definition cues count literal patterns such as "means", "is called", and
  "is the". A cue does not establish that a concept was adequately explained.
- Pronoun antecedent measures count earlier nouns/proper nouns and distance to
  the nearest. They do not resolve which noun a pronoun actually refers to.
- Mention recency compares a current content lemma with its last earlier
  occurrence. New and repeated mentions remain lexical proxies.
- Empty scopes produce finite values with zero-denominator ratios set to zero.
  `characters` uses Python Unicode codepoints; only API offsets use UTF-16 units.

## Reproducibility and tests

The parser is loaded lazily. Prefix parses are cached with a bounded 128-entry
cache. Each call returns a fresh dictionary. No network is required.

`python3 -m pytest tests/test_features.py -q` verifies suffix invariance, UTF-16
emoji offsets, malformed boundaries, finite/stable schemas including empty text,
distinct/repeated-name proxies, prior mentions, literal markers, and immunity to
caller mutation. The initial tests failed against the unimplemented extractor;
all 19 feature cases passed after implementation.

A full-suite check at that time passed those 19 cases and failed four
`tests/test_search.py` cases while the separate search implementation was still
being written. No search files were modified by this subtask. The installed
Python environment emits a urllib3/LibreSSL compatibility warning when importing
spaCy; the extractor itself does not use HTTPS.

These are engineering checks on feature extraction. They do not establish the
features' predictive usefulness or the validity of a fitted equation.

## Revision v2: registered development hypothesis before revised fitting

Registration timestamp: 2026-09-22T17:49:44.965613+00:00. The original extractor is preserved verbatim in
`feature_versions/features-v1.py`. The revised extractor will be version
`local-prefix-features-v2-actions` and add exactly 20 step-level measures, bringing
the inventory from 231 to 251. Existing measures retain their definitions.

The v1 section's statement that no labels had been inspected applies to the
original implementation only. This revision follows error inspection of exactly
`pilot-runs/models/polynomial_k8_d2_a0.1/validation_predictions.jsonl`. Those
temporary pilot validation families belong to the permanent **training** set.
Neither the permanent validation set nor final-test text or scores informed this
revision. This is a recorded development hypothesis, not a retrospective claim
that the revised measures were chosen without seeing any errors.

Observed development errors motivate a specific hypothesis: counts of nouns,
clauses, and dependency distances may insufficiently distinguish describing a
relationship from asking the reader to manipulate, compare, connect, or track
several relationships. Some descriptions were overestimated while some
instructions were underestimated. The direction is not universal: a previously
defined term also produced a lower reference score than the same instruction
without the earlier definition, so action categories cannot by themselves solve
all errors.

Prediction to test: giving the equation generic action and argument information
will reduce average error on the **same** pilot holdout with the same training
split and search procedure, especially for multi-argument instructions. Compare
v1 and v2 without selecting favorable examples. A worsening result rejects this
revision as an improvement under that comparison. A pilot improvement remains
development evidence and requires a fresh evaluation on the reserved permanent
validation set; the final test stays sealed until a candidate is frozen.

The 20 new keys, all beginning with `step_`, are:

```
imperative_roots imperative_predicates
action_compare_verbs action_order_verbs action_connect_verbs action_track_verbs
action_calculate_verbs action_select_verbs action_define_verbs action_manipulate_verbs
action_category_count action_lexical_verbs action_conditional_selections
action_direct_object_heads action_direct_object_items action_max_object_group
action_prepositional_arguments action_prepositional_object_items
action_spatial_arguments action_max_nominal_arguments
```

The lexicons describe common operations across domains, such as compare, sort,
connect, trace, calculate, choose, define, and move. They contain no subject-specific
science vocabulary and no label values. The counts do not assert that an action
requires a particular number of working-memory units. Category verbs can occur
in descriptions as well as instructions; the separate imperative measures let a
fitted equation learn an interaction rather than hard-coding a score.

Imperatives are a parser-based proxy: a base-form root verb without an explicit
subject, or a subject-free coordinated base-form verb attached to that root.
Direct objects and their coordinated members count as separate local arguments.
Prepositional arguments are local prepositions whose nearest verbal ancestor is
one of the category predicates; their object items include coordinated members.
Spatial arguments are a declared general set of direction/location words in
those constructions. All tokens and parse decisions stop at the reading point.

For defining, ordinary definition verbs are supplemented by a form of "be" with
a nominal attribute (for example, "a triangle is a shape"). This is only a
syntactic cue and does not establish that a definition is complete or correct.
Conditional selection counts a selection predicate when its available sentence
contains an if/unless-style marker. The same-sentence context may precede the
current step but cannot include future text.

Implementation checks: the 15 newly added synthetic test cases initially failed
against v1 with missing feature keys (and the expected old feature count), while
the original 19 cases passed. After implementing v2, all 34 feature cases pass.
They test described versus imperative actions, all eight categories, nominal
definitions versus adjective descriptions, coordinated objects, spatial
arguments, conditions available before a step, and exclusion of earlier-step
actions. The existing suffix-invariance test now covers all 251 measures.

The original v1 file SHA-256 is
`f64ed256452de88d514097418aa444ea7b181044eb031a4bf06967309fa295dd`.
The feature tests use invented synthetic sentences, not teacher labels. No API
request or revised model fit was performed by the feature revision subtask.

## Revision v3: reference words and ordinary word frequency

Registered at 2026-09-22T17:58:03.551115+00:00, before the revised comparison.
V2 is preserved in `feature_versions/features-v2.py`, SHA-256
`4a24078175316f8320e53099cb892e45aa8e0793241db387507dfb7493adc140`.
V3 will be `local-prefix-features-v3-reference-frequency` with 271 measures:
the existing 251 unchanged plus the following 20 step-level measures.

Sixteen separate literal word counts, named `step_reference_word_<word>`:

```
both each every same equal different other another between either neither
together separately respectively former latter
```

Four frequency measures:

```
step_content_zipf_mean
step_content_zipf_min
step_rare_content_mentions
step_new_rare_content_lemmas
```

The researcher supplied three stable-error examples from the two-domain
development midpoint: underprediction for labeling both angles, overprediction
for a clause about equal volumes, and overprediction for drawing stations then
adding their times. These are development observations, not final-test evidence.
No final-test text or scores have been inspected for this revision.

Hypothesis: broad relationship counts can conceal distinctions between equal
things, both things, and separately tracked things. Separate common reference
words may help the equation learn these differences. General word familiarity
may also help distinguish ordinary references from unfamiliar terms without
introducing particular science nouns or their reference scores.

Predeclared comparison: use the same two-domain midpoint data and search as V2,
compare overall held-out development error and the previously observed errors,
and retain a complete record even if V3 gets worse. No success is presumed and
no favorable examples may replace the overall comparison. Since development
errors informed this choice, the comparison does not establish final-test
generalization.

Literal counts use lowercase surface words; for example, "equal" counts while
"equals" does not. Frequency uses the installed `wordfreq==3.1.1` English `best`
word list and its `zipf_frequency` for lowercase content-word lemmas. This is a
local lookup, not a model or API call. The same content-word definition as V1 is
used. Mean and minimum cover current content-word occurrences. A rare mention
has Zipf frequency below 3.0; a new rare lemma is a distinct current rare lemma
not previously encountered as a content lemma before this step. Empty content
sets yield zero. General population frequency is only a familiarity proxy: it
does not measure this learner's knowledge, and an unlisted token receives the
library's zero default. Freeze the library and its packaged word list for
reproducibility.

V3 engineering verification: all 40 feature test cases pass. Before implementation,
the six added tests and updated schema-count assertion failed on the missing V3
keys/count, with the other 33 cases passing. The tests distinguish literal "both"
from "equal", check scope boundaries and frequency behavior, and compare every
one of the 251 previous feature values against the preserved V2 implementation
on five synthetic examples. The preexisting all-feature suffix-invariance check
also covers the 20 additions. No revised equation was fitted by this subtask.
