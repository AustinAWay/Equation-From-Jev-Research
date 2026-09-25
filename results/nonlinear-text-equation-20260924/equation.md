# The new equation, fully specified

This equation was learned directly from final Jev-app scores. It receives 38 numerical measurements taken from the current reading step and earlier text. It has 128 Gaussian terms and ten output sums, one for each score category seen in training. It uses 6,942 saved numerical parameters. It makes no Jev call when used.

In plain language: count the text features, compare that collection of counts with 128 learned reference patterns, and combine those comparisons to choose a score. Both the comparisons and the final weights are numerical and inspectable.

The arithmetic is:

```text
z[j] = (x[j] - mean[j]) / scale[j]
g[r] = exp(-sum_j((z[j] - center[r,j])²) / (2 × 38 × 2²))
v = [z[1], …, z[38], g[1], …, g[128]]
A[k] = intercept[k] + sum_q(weight[k,q] × (v[q] - basis_mean[q]) / basis_scale[q])
score = category with the largest A[k]
```

Ties select the smaller score. The ten observed training categories are 1, 2, 3, 4, 5, 6, 7, 8, 9 and 11. This categorical equation cannot predict an unseen category such as 10. Its reported probabilities come from exponentiating and normalizing the A values; they are probabilities assigned to Jev labels, not human memory measurements.

There is no preset “add two.” The saved intercepts and every other fitted weight were learned from the training examples. An intercept is part of ordinary equation fitting; it does not excuse failing the constant-score or word-count controls.

Every coefficient, normalization value and center is saved in selected-equation.json. full-equation.txt spells the equation out using explicit numbered inputs and complete numerical arrays. The input list is:

1. `words`
2. `letters`
3. `vowels`
4. `syllables`
5. `sentences`
6. `words_per_sentence`
7. `syllables_per_word`
8. `letters_per_word`
9. `long_words`
10. `three_syllable_words`
11. `unique_words`
12. `repeated_words`
13. `commas`
14. `semicolons`
15. `colons`
16. `pronoun_markers`
17. `condition_markers`
18. `connectors`
19. `negations`
20. `number_tokens`
21. `previous_words`
22. `previous_unique_words`
23. `words_seen_before`
24. `new_word_types`
25. `words_seen_recently`
26. `mean_repeat_gap`
27. `max_repeat_gap`
28. `step_noun_chunks`
29. `step_clause_heads`
30. `step_subordinate_clauses`
31. `step_max_syntax_depth`
32. `step_mean_dependency_distance`
33. `step_long_dependencies`
34. `step_pos_pron`
35. `struct_unfinished_peak`
36. `struct_new_entities`
37. `struct_intervening_information_sum`
38. `struct_cross_step_connections`

The surface definitions are in ../direct-text-equation-20260924/feature-definitions.json. Grammar counts use the existing fixed local parser. Only available earlier/current text enters extraction. Some input counts overlap, and fitted weight signs should not be interpreted as causes of human cognitive load.

The local calculator is work/nonlinear-text-equation-20260924/score_text.py. It accepts text and optional UTF-16 start/end offsets for the current reading step, and returns the predicted score, all measured inputs and all category probabilities. It requires the existing local parser and Python dependencies; it does not contact Jev.
