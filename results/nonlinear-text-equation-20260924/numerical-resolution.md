# Numerical resolution before comparison evaluation

The initial Gaussian fitting run used an unnecessarily strict optimizer tolerance of 1e-6 with 1,200 maximum iterations. The first nine development candidates repeatedly reached the iteration limit. The process was stopped; its development metrics and warnings remain under kernel-polynomial/numerical-initial. No comparison labels had been evaluated.

Rerun the identical 24 Gaussian/polynomial specifications uniformly with tolerance 1e-4 (the spline run's tolerance) and at most 3,000 iterations. Reject any candidate with an unconverged development fold. Do not change features, regularization grid, development folds or selection criteria. A selected full-data refit must converge. Independently reproduce both predictions and probabilities from the exported arithmetic, including finite-value checks. This is a numerical fitting correction, not another model search selected on comparison answers.

For the stated complexity tie-break, count saved numerical coefficients, intercepts, normalization means/scales, and learned kernel centers or spline knots. The initial Gaussian code counted only output weights, which omitted center coordinates; the rerun corrects that. The shared evaluator binds each frozen comparison prediction file by SHA256 and checks its row identifiers before loading reference answers.
