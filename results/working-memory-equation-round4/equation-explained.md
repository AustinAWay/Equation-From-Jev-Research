# The equation in plain English

The selected equation estimates which items contribute to the app's count, then combines them using a fixed counting rule. It matched the app exactly on 47.7% of the fresh-test reading steps, with each scenario family given equal weight.

First, a local grammar parser identifies possible items. The equation measures each item's grammatical role, earlier appearances and connections to the current step. It also measures how common the words are. Many saved numerical if/then rules turn these measurements into an item estimate between zero and one. An estimate of 0.8 means an assigned 80% chance of contributing a separate unit to the app's score. We have not established that those assigned probabilities are accurately calibrated, even for the app; they are not verified probabilities about a person's memory. Combining them is an approximation to our reference answer: the middle of three complete app scores.

For each possible total, calculate how likely it would be if the item decisions were independent. Choose the most likely total, then add the rounded extra-unit estimate. Ties choose the smaller total.

For example, three items each assigned a 51% chance of mattering would all pass an individual yes/no cutoff. But the calculated probabilities for the totals are 11.8% for zero, 36.7% for one, 38.2% for two and 13.3% for three. **Two is the most likely total.** This is a mathematical illustration of the counting rule, not evidence that real memory decisions are independent.

The actual counting equation is:

\[
Q(z)=z^{\lfloor e+0.5\rfloor}\prod_{i=1}^{K}((1-p_i)+p_i z),
\qquad \widehat{s}=\operatorname*{argmax}_{k\ge0}[z^k]Q(z).
\]

Here, the coefficient of the k-th power of z is the calculated chance of total k. The computer finds those coefficients through repeated addition and multiplication. The independence assumption may be wrong; the test measures whether the resulting predictions are useful. For this equation, the raw output equals the displayed whole-number score.

The item and extra-unit estimates themselves are:

\[
p_i=\operatorname{clip}_{[0,1]}\left(\frac1{160}\sum_{t=1}^{160}T_t(\phi_i)\right),
\qquad e=\max\left(0,\frac1{120}\sum_{t=1}^{120}U_t(\psi)\right).
\]

Each T or U is a saved set of numerical if/then rules. The symbols phi and psi mean the measured properties of an item and a reading step. **full-equation.txt** spells out every fitted threshold and numerical leaf value. **equation.json** contains the same learned parameters in a machine-readable form. The offline checker supplies the exact text measurements and specifies the local parser and word-table dependencies.

This is a long, learned piecewise mathematical predictor. It can run locally without Jev requests after training. Local computation and the existing parser are still required.

Having an equation and having an equation accurate enough to replace the app are separate achievements. This test measures agreement with the fixed app procedure. It does not validate either system as a measure of human working memory.
