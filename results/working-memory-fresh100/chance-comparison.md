# Does the equation beat guessing?

Yes, on this fresh test it beat both random guesses and always choosing the most common score.

| Method | Exact agreement with Jev's app |
| --- | ---: |
| Random guesses, using score frequencies from development | 23.4% expected |
| Always answer 2, the most common development score | 34.4% |
| Frozen equation | 47.3% |

The equation gives about 13 more exact matches per 100 scoring steps than always answering 2. The family-bootstrap 95% interval for that advantage is 8.2 to 17.4 percentage points. Its average error is also lower: 0.63 points versus 0.93 for the constant answer.

This is a comparison of several possible numerical scores, so 50% is not the automatic chance level. There is no single universal random baseline: the random strategy above chooses scores with the same frequencies observed in development, independently of the passage. Its reported accuracy is the mathematically expected value, not one lucky or unlucky simulation. The stronger constant-answer baseline also uses only development data to select its answer.

This additional comparison was chosen after viewing the test results. It uses all the same 100 passages, 50 families and 910 reading steps, with the original equal-family weighting. No equation changes, new Jev calls, test exclusions or test-selected constant scores were used. Uncertainty resamples whole families 20,000 times with seed 20260924; it is descriptive for this authored sample.

The equation therefore contains useful predictive information beyond these guessing strategies. It still disagrees with the app on the exact score roughly half the time, and this comparison does not establish accuracy about human working memory. Numerical details are in chance-baselines.json.
