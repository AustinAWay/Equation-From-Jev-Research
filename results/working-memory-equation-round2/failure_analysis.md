# What the frozen predictions got wrong

This diagnosis uses **24 held-out passage families**, 48 passages, and 208 scored steps. Families are the evaluation units; related variants and repeated scores are not independent samples. No equation was changed or run again for this audit.

| Frozen procedure | Average error | Exact agreement | Error on stable references |
|---|---:|---:|---:|
| Previous equation | 0.846 | 39.0% | 0.787 |
| Direct formula | 0.855 | 40.0% | 0.795 |
| Intermediate decisions | 0.740 | 41.7% | 0.672 |
| Running ledger | 0.888 | 32.7% | 0.810 |
| Ledger without history | 0.888 | 31.6% | 0.833 |

**Prespecified improvement claims.**

- Direct formula versus previous equation: improvement -0.009; simultaneous interval [-0.103, 0.085]. The 0.10-unit claim is contradicted at the proposed magnitude.
- Intermediate decisions versus direct formula: improvement 0.115; simultaneous interval [0.013, 0.214]. The 0.10-unit claim is unresolved at the proposed magnitude.
- Ledger versus removing its history: improvement -0.000; simultaneous interval [-0.057, 0.053]. The 0.10-unit claim is contradicted at the proposed magnitude.

The intermediate-decision interval stays above zero: this is positive evidence of some predictive improvement on this benchmark. It does not yet establish the promised improvement of at least 0.10 units. None of these exact-match rates approaches 95%.

**Reference consistency.** All three repeats agreed on 151/208 steps. The stable-reference column shows whether substantial errors remain without observed score disagreement. Repetition is not proof of human-memory validity.

**Stable counterexamples.**

- Direct formula: “Report the surface, color, and weight without treating those words as the same property.” Reference 8; prediction 4. All three reference runs agreed.
- Intermediate decisions: “Identify the object” (after tracking which of two objects was carried upstairs). Reference 6; prediction 2. All three reference runs agreed.
- Running ledger: “Report the surface, color, and weight without treating those words as the same property.” Reference 8; prediction 4. All three reference runs agreed.

**Controlled contrasts.** Average error by challenge:

| Challenge | Approach 1 | Approach 2 | Ledger | Reference follows tentative focus direction |
|---|---:|---:|---:|---:|
| connected facts | 0.794 | 0.606 | 0.837 | 4/6 families |
| extra idea | 1.010 | 0.899 | 1.099 | 5/6 families |
| near far | 0.847 | 0.792 | 0.856 | 1/6 families |
| reference wording | 0.769 | 0.663 | 0.762 | 6/6 families |

Moving the relevant rule farther away reduced the Jev-based focus score in 5/6 pairs and left it unchanged in 1/6. In 2 pairs, every observed cross-repeat difference was negative. The tentative expectation about these reference counts failed; this does not show that actual human memory demand falls with distance. A separate [reference audit](distance_reference_audit.md) confirmed omitted original rule candidates in two far variants. Whether that omission caused the score changes still needs a controlled test.

Last-step and whole-passage peak directions are additional diagnostics, not newly declared primary tests. Incomplete pairs are excluded; observed repeat ranges accompany differences. A failed tentative direction challenges the expectation about Jev-derived counts, not the observation.

**What remains uncertain.** The ledger stores relation arguments without their order, so reversed roles can collapse into one identity. That loses information but does not alone show that the final count must change. An advantage for intermediate decisions would support that implemented procedure; it would not isolate a cognitive mechanism from its measurements and learned proxies.

These results judge particular frozen equations within this corpus and reader profile. They do not prove that equations are impossible or establish human working-memory measurement. Repairs require another independent test; these outcomes must not be reused as unseen evidence.

A separate old-data check found 5 groups with exactly identical complete ledger inputs but different three-run-stable targets. A deterministic equation using only those same inputs cannot match both targets. This identifies missing information in this representation; it does not rule out better text measurements.
Those collisions force at least 5 errors among 389 stable old rows, an unweighted maximum agreement of 98.715%. That bound does not disprove the 95% target. Richer inputs within approaches 1–3, followed by another withheld test, remain a possible repair.

**Strongest next test.** Keep the best intermediate-decision procedure as the fixed comparator. Add explicit measurements preserving who acts on whom and which earlier object a reference identifies, then compare the repaired version on newly authored, withheld pairs matched for wording and length. Include separate checks of the teacher's candidate selection in near/far pairs. Freeze both versions before collecting answers and retain the same 0.10 improvement criterion. This tests a specific repair within approaches 1–3; it does not require passage-type routing or another language model.
