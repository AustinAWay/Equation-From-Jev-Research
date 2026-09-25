# Fresh test of the frozen equation

**The equation matched Jev's app score exactly 47.3% of the time on 100 new passages.** It was within one point 91.4% of the time; average error was 0.63 points.

| Test | Exact agreement |
| --- | ---: |
| Earlier development estimate | 45.6% |
| Earlier fresh test, 100 passages | 47.7% |
| This fresh test, 100 new passages | **47.3%** |

The change from 45.6% is **+1.7 percentage points**. The new result's descriptive 95% uncertainty range is **42.9% to 51.6%**. The new result is compatible with the earlier 45.6% development estimate when judged by this new sample's uncertainty interval. This is not proof that the underlying rates are identical.

We used three complete Jev-based analyses per passage (300 total), taking the middle score at each of 910 reading steps. The equation and all predictions were frozen before the first request. No training or equation changes were made for this test. Both passages in a pair belong to one family; families receive equal weight. The simple unweighted count was 423 exact matches out of 910 steps (46.5%).

Jev's three runs disagreed at 267 steps. 880 steps had a provisional flag; 910 had a coverage warning or lacked a definite all-clear flag. All steps remained in the result.

| Claim | Possible contradiction | Test result | Scope and status |
| --- | --- | --- | --- |
| Earlier approximate agreement survives new examples | A substantially worse new result, with uncertainty supporting the drop | 47.3% exact; range 42.9–51.6% | compatible with the earlier development point under this test's assumptions; no proof of equality |
| This equation is a nearly exact replacement for the app | Error rate well above 5% | 52.7% disagreement | The 95% exact-agreement target is contradicted on this sample |

These newly authored passages test agreement with the app, not accuracy about human working memory. They are not a random sample of all reading material. Differences can reflect the text mix and reference variability. The next stronger test would use an independently sourced, preselected real-world corpus; a clear drop there would weaken the generalization further.

The corpus, unchanged predictions, full comparisons, protocol and numerical results are saved alongside this report. Raw responses and per-request accounting remain in the local experiment folder. The separate autonomous training search did not receive these results.

Collection speed was increased at the user's request: four concurrent analyses and eight concurrent evaluation batches replaced two analyses and four batches. Completed analyses, the equation, saved predictions, samples, repeats and scoring rules were preserved. Both transport settings are recorded in the raw results.
