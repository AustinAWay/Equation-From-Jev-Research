# The direct text equation

This is an explicit weighted sum of 32 measured text properties. Every input is counted from the current reading step or preceding visible text. The equation contains no tree ensemble and no Jev calls. Eleven input measurements use the existing local grammar parser. The intercept and coefficients were fitted on development data, not chosen to force a score of two or three.

Compute the following sum, round to the nearest whole number (halves round up), and replace negative answers with zero. Coefficients below are displayed to 10 decimal places; equation.json stores full precision.

```text
raw = -0.6628797162
    +0.0184034934 × letters
    +0.7538662445 × sentences
    +0.0389682062 × letters_per_word
    -0.0120904147 × three_syllable_words
    +0.1289403865 × unique_words
    +0.1228283039 × repeated_words
    +0.1401015164 × commas
    -0.0616611218 × semicolons
    +0.7320485622 × colons
    -0.1575964606 × pronoun_markers
    -0.3074740560 × condition_markers
    +0.0070588517 × connectors
    -0.1785639697 × negations
    +0.4679124671 × number_tokens
    +0.0113022800 × previous_words
    -0.0094761083 × previous_unique_words
    -0.1112504721 × words_seen_before
    -0.1329944538 × new_word_types
    +0.0540734433 × words_seen_recently
    +0.0028300753 × mean_repeat_gap
    -0.0110646227 × max_repeat_gap
    +0.0784355597 × step_noun_chunks
    +0.2157149806 × step_clause_heads
    -0.2601517530 × step_subordinate_clauses
    +0.0721235131 × step_max_syntax_depth
    +0.1087343934 × step_mean_dependency_distance
    +0.0347772369 × step_long_dependencies
    +0.1334992560 × step_pos_pron
    +0.3305647957 × struct_unfinished_peak
    +0.0117122197 × struct_new_entities
    -0.0321307908 × struct_intervening_information_sum
    -0.0691069022 × struct_cross_step_connections

score = max(0, floor(raw + 0.5))
```

These weights describe a fitted prediction, not causal effects on memory. Counts overlap; a negative coefficient does not establish that a feature makes reading easier. Vowels, total syllables, sentence length and other measurements were offered to the search; not every offered measurement was retained.

| Input | What is measured |
| --- | --- |
| `letters` | Alphabetic characters in the current step. |
| `sentences` | Nonempty text spans separated by sentence-ending punctuation; minimum one. |
| `letters_per_word` | Letter count divided by word count. |
| `three_syllable_words` | Words estimated to have at least three syllables. |
| `unique_words` | Different lowercase words in the current step. |
| `repeated_words` | Current words minus different current words. |
| `commas` | Comma count. |
| `semicolons` | Semicolon count. |
| `colons` | Colon count. |
| `pronoun_markers` | Occurrences of he/she/it/they/him/her/them/his/their/its/this/that/these/those. |
| `condition_markers` | Occurrences of if/unless/when/whenever/provided. |
| `connectors` | Occurrences of and/or/but/because/although/while/whereas/therefore/however. |
| `negations` | Occurrences of not/no/never/neither/nor/without. |
| `number_tokens` | Words containing a digit. |
| `previous_words` | Words before this reading step. |
| `previous_unique_words` | Different words before this reading step. |
| `words_seen_before` | Current word occurrences that appeared earlier. |
| `new_word_types` | Different current words absent from earlier text. |
| `words_seen_recently` | Current word occurrences present in the last 40 earlier words. |
| `mean_repeat_gap` | Mean number of earlier words back to the last occurrence of each repeated current word; zero if none. |
| `max_repeat_gap` | Largest such earlier-word distance; zero if none. |
| `step_noun_chunks` | Noun phrases counted by the local grammar parser. |
| `step_clause_heads` | Main or subordinate clause heads and coordinated verbs counted by the parser. |
| `step_subordinate_clauses` | Subordinate-clause heads counted by the parser. |
| `step_max_syntax_depth` | Maximum number of grammar links above a current word. |
| `step_mean_dependency_distance` | Mean word distance across grammatical links attached to current tokens. |
| `step_long_dependencies` | Grammatical links spanning at least five token positions. |
| `step_pos_pron` | Words tagged as pronouns by the parser. |
| `struct_unfinished_peak` | Largest number of selected grammatical links crossing a word boundary in the current step. |
| `struct_new_entities` | New noun/proper-noun lemmas first introduced in the current step. |
| `struct_intervening_information_sum` | Sum of intervening new nouns and finite verbs inside selected links completed in the step. |
| `struct_cross_step_connections` | Selected grammatical links crossing the boundary from earlier to current text. |
