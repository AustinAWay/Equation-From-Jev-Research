# Testing the equation on 100 new passages

The equation is unchanged. Each new passage receives three Jev analyses, and the middle score is used for comparison at each reading step.

- **Current progress:** `status.md` (updated by the collection program).
- **Final answer:** `report.md` (created automatically after all 300 analyses finish).
- **Detailed result:** `results.json` and `all-comparisons.jsonl`.

The final report compares the new exact-match percentage with **45.6% on development material** and **47.7% on the earlier fresh test**. It also reports uncertainty, near misses and disagreements between Jev's repeated runs.

Predictions are saved before Jev is called. This test does not train the equation or feed the separate autonomous search. It measures agreement with the Jev-based app, not measured human working memory.

The program runs locally without an AI agent managing each analysis. Internet access is needed for collection; this folder receives the final report automatically.
