# Equation search: finished

Updated: 2026-09-25T02:28:39.532226+00:00

- Completed attempts: 181
- Best search candidate: 43.5% exact; 0.780 average error
- Numeric equation export: verified; trial 147.
- Existing equation on the same development data: 45.6% exact; 0.710 average error.
- Reason: progress_stalled
- Search uses ordinary local computation. No agent or model API calls run inside this loop.

**These are repeatedly reused development scores, not fresh-test accuracy.**
Even reaching 95% here only produces a candidate for a new test. The earlier 47.7% fresh-test result is a different measurement and should not be compared directly with this score.

The search keeps related passages together in five folds, so a fitted equation does not train on its own evaluation family. Repeatedly choosing equations using these folds can still overfit them.

Use Stop.command to pause. Use Start.command to resume. Each launch has a 12-hour ceiling; the total trial limit is 1000. The computer must remain powered on. The runner prevents idle sleep while it is active.
