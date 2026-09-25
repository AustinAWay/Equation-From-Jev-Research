# What counts as the saved equation

The user allowed arbitrarily long equations. These exports are numerical functions with fitted coefficients and piecewise rules; they are not claimed to be short readability-style polynomials. The inputs are explicit measurements from the existing local parser, word statistics and memory-tracking rules. The saved JSON parameters and frozen measurement/runtime code together define the calculation.

The plain-language explanation is separate. This appendix states the arithmetic precisely enough to identify the fitted objects.

## Approach 1: direct equation

Let `x_j` be numerical text measurement `j`, and let `z_j = (x_j − μ_j)/σ_j`. Means, scales, stored standardized centers, coefficients and the intercept are fixed after fitting. The primary numeric kernel equation is

`D(x) = max(0, b + Σ_i a_i exp(−0.001 Σ_j (z_j − z_ij)²))`.

The displayed score is `floor(D(x) + 0.5)`. Every `a_i`, `b`, `μ_j`, `σ_j` and `z_ij` is in the corresponding JSON model. Stored centers are numerical input measurements, not a table of Jev answers retrieved at inference. The coefficients were learned from those answers during fitting.

The lexical development alternative additionally measures explicit words, word pairs and directed grammar. It uses the recorded vocabulary, inverse-document weights and declared kernel mixture. It is a tested secondary input revision; it is not a new pretrained semantic model.

### Probability variation within approach 1

The saved multinomial logistic equation first estimates individual-score probabilities:

`p_k(x) = exp(b_k + w_k · z) / Σ_h exp(b_h + w_h · z)`.

Use numerically stable evaluation of this expression. For the ordered score classes, let `F_k = Σ_(h≤k) p_h`. If three draws are conditionally independent with these same probabilities, their median has cumulative distribution

`G_k = 3F_k² − 2F_k³`.

Its score probabilities are `q_k = G_k − G_(k−1)`, with preceding cumulative value zero. The primary output is the smallest class whose cumulative probability reaches0.5. The separately reported unrounded output is `Σ_k k q_k`. The transformation is exact under its assumptions; estimated `p_k` values can still be wrong. Unit tests compare this identity with enumeration of every triple.

## Approach 2: smaller decisions, then count

For each idea `c` in the locally extracted candidate pool (current candidates plus at most12 prior candidates), a fixed forest produces three estimated probabilities: separate/root, grouped, background. A second fixed forest predicts additional relationship units. The primary expected-count equation is

`C = Σ_c P_c(root) + E(extra units)`.

The display is `max(0, floor(C + 0.5))`. The root-probability forest has160 trees and the extra-unit forest has120 trees. Their features, split thresholds, leaf values and aggregation rules are all saved. Role outputs are clipped to[0,1] and divided by their sum; if that sum is at most1e−12, the fallback is one-third for each role. Extra counts are made nonnegative. This computes an expected sum and then rounds. It is not the exact median-of-three distribution of the final assembled score.

The genuine-grouping secondary uses a fitted conditional choice equation and the original assembly logic with a fixed deterministic integration approximation. It is preserved separately; it is not silently substituted for the expected-count primary.

## Approach 3: explicit running memory record

Fixed rules track entity references, directed relations, negation, retrieved conditions and recent history. Let `l` be the52 measurements of that state. The selected activity window accepts event age at most4: the current event and four preceding events. Identity and condition records can persist longer. The primary scoring equation is

`L(l) = max(0, b + 0.04 Σ_(t=1..200) T_t(l))`.

The displayed score is `floor(L(l) + 0.5)`. Each tree has maximum depth3. The precise initial value, thresholds, leaves, measured state and float32 input casting rule are saved. This is a learned score of the running record, not a claim that simply counting its entries measures human memory.

## Trees as explicit mathematical expressions

A decision tree is a piecewise numerical function. If `v_ℓ` is a leaf value, it can be written as

`T(z) = Σ_leaves ℓ v_ℓ × Π_rules on path to ℓ I(rule is satisfied)`.

`I` is1 when its comparison is true and0 otherwise. A left branch tests `z_j ≤ threshold`; a right branch tests `z_j > threshold`. Thus the saved branch tables are a compact representation of a long equation. Tree ensembles add or average these functions using the recorded weights. Numerical casting and clipping in the runtime are part of the exact computational definition, not omitted conveniences.

## One fixed combination of approaches 1–3

The combined equation is `max(0, w_D D + w_C C + w_L L)`, optionally rounded once with `floor(value + 0.5)`. Weights are nonnegative and sum to1. They are selected from development predictions in tenths and fixed for every passage. `models.json` preserves both the smaller-error choice and the exact-match choice. No passage-type routing is used.

Every export is checked numerically against its fitted implementation. The portable bundle is also checked away from the source workspace with network access denied. These tests establish that the saved arithmetic executes faithfully. They do not establish its predictive accuracy, which is measured separately on sealed new passages.
