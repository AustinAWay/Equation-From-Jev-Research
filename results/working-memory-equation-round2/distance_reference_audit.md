# Why the farther-away rule received a lower app score

**The app’s 12-prior-candidate limit drops original rule pieces in both far variants.** This is a concrete potential measurement artifact in the two near/far counterexamples. It prevents interpreting the lower scores as evidence that moving a rule farther away reduces human working-memory demand. It does **not** prove the cap alone caused the score decrease.

This read-only audit inspected all 12 saved analyses for `fresh_20_a/b` and `fresh_22_a/b`: three runs of each variant. Rebuilding the frozen app’s requests locally produced exactly the same memory-question candidate IDs as the saved decisions in every run. No API calls, relabeling, fitting, source changes, or cap-removal experiment were performed.

| Family | Near scores, runs 1–3 | Far scores, runs 1–3 | Prior candidates available / retained | Original rule occurrences retained, near → far |
|---|---|---|---|---|
| `fresh_20` | 6, 5, 6 | 3, 3, 3 | 16 / 12 | 4 → 1 |
| `fresh_22` | 6, 6, 5 | 3, 3, 3 | 14 / 12 | 7 → 5 |

The median decrease is three units in each family; every same-repeat comparison is negative. The near scores themselves vary, so “stable direction” is more accurate than “identical repeated scores.” Every focus score equals its primary group count; accepted additional relational units do not explain the difference.

For **fresh_20**, the near pool retains `c7 Members`, `c8 a silver badge`, `c9 may enter`, and `c10 nine`. The far pool retains only `c3 may enter` from that rule; it omits `c1 Members`, `c2 a silver badge`, and `c4 nine`. The later observation’s separate occurrence of “a silver badge” is still retained, so the app has not lost every mention of the badge. The original nine-o’clock threshold has no occurrence in the far case’s explicit grouping pool. Some irrelevant room/clock candidates occupy places instead. In the first near run, the threshold is a separate group; the far run also combines the drummer/badge and present-time candidates more tightly, so the total three-unit difference is not simply three omitted words.

For **fresh_22**, the near pool retains all seven rule occurrences: `c6 this probe`, `c7 a blue lamp`, `c8 means`, `c9 moist air`, `c10 a yellow lamp`, `c11 means`, and `c12 dry air`. The far pool drops `c2 a blue lamp` and `c3 means` from the blue-lamp rule. It retains `c1 this probe`, `c4 moist air`, `c5 a yellow lamp`, `c6 means`, and `c7 dry air`. The later “The blue lamp” observation remains available. Other grouping decisions differ: in the first far run, the interpretation, probe, observed blue lamp and lit state form one primary group, while “moist air” and “dry air” remain separate groups.

**The complete rule text remains visible in the request prefix in all cases.** The issue is narrower than truncating the text: the app nominates only 12 earlier occurrences for individual dependency/memory decisions. Primary groups can use only nominated earlier occurrences with memory decisions, and the relational candidate pool follows the same assessed set. Thus extra distance changes both placement and which rule pieces are explicitly available for counting. The comparison does not isolate distance with an otherwise fixed candidate universe.

The selection code prioritizes same-sentence conditional context, lexical overlap with the current clause, and recency. Here the relevant rule is in an earlier sentence, so the special same-sentence condition priority does not protect it. The saved app warnings already disclose that distant or differently worded dependencies can be missed despite the full prefix remaining available.

**Assessment:** These are valid counterexamples to the tentative prediction that the frozen app’s score would not decrease in the far condition. Their interpretation as cognitive evidence is substantially weakened by a demonstrated change in candidate coverage, by different remaining grouping decisions, and by provisional estimates. A later, separately declared ablation could keep all relevant rule candidates available in both orders and collect new reference judgments. That would test whether candidate coverage explains the reversal; it must not replace these frozen benchmark answers after the fact.

Source: frozen commit `cee3edb9922115d759778434878f6c56b483b390`; `backend/prompts.py:365–412`, `backend/memory.py:10–15`, and `backend/semantic_connections.py:44–53`. [The full audit](distance_reference_audit.json) preserves each run’s retained pool, dropped rule pieces, primary groups, role/confidence records, warnings and exact counts.
