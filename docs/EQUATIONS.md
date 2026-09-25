# What the equations actually contain

A short expression can describe a large fitted model. It is not evidence that a simple law of cognition was discovered.

## Cubic spline equation: the 43.4% comparison result

For text measurement vector x, the saved spline transformation produces 228 standardized curve components u_i(x). For each of ten observed score classes c:

```text
A(c) = b(c) + sum_i w(c,i) * u_i(x)
predicted score = class c with largest A(c)
```

This requires **2,290 fitted class weights and intercepts**, plus the spline knots, degrees and scaling values. It has 38 original measurements. The complete values are in [spline.json](../models/spline.json), and [spline_runtime.py](../src/jev_equations/spline_runtime.py) implements the saved arithmetic. Model class probabilities are numerical classifier outputs, not validated confidence about a person's memory.

## Gaussian equation: selected before the comparison

Standardize each of 38 measurements using the saved development mean and scale. Compute 128 radial basis terms:

```text
z_j = (x_j - mean_j) / scale_j
r_k = exp(-sum_j (z_j - center_kj)^2 / (2 * 38 * length_scale^2))
v = concatenate(z, r)
u_i = (v_i - basis_mean_i) / basis_scale_i
A(c) = intercept_c + sum_i coefficient_ci * u_i
predicted score = class c with largest A(c)
```

There are **6,942 saved numerical parameters** under the study's count, including centers, normalization, weights and intercepts. [gaussian.json](../models/gaussian.json) is the exact export; [the full numerical equation](../models/gaussian-full-equation.txt) lists its constants. The selected artifact has SHA-256 `bbf6494601187a251af4f659b0a7cf80df9b77b8bb1cdf22b59c4b94ace4c5bc`.

## Other equations and controls

- [polynomial.json](../models/polynomial.json): degree-one logistic specification won the linear/quadratic search. The name records the search family; the selected artifact is linear in standardized inputs.
- [linear.json](../models/linear.json): earlier 32-term weighted sum, followed by `max(0, floor(raw + 0.5))`.
- [word-count.json](../models/word-count.json): flexible spline using only the current step's word count. It is the relevant length control for the nonlinear comparison.
- [component-count-mode.json](../models/component-count-mode.json): the larger model selected in round 4. It predicts smaller item decisions, forms a distribution for their total using an independence approximation, chooses its mode and adds rounded extra relationship units. Use the original offline checker in the release for this different pipeline.

All classifiers can output only score classes present in their fitting data. Unknown text types and larger true app scores are not covered by a guarantee. Parser and feature versions are part of the equations' operational definition.
