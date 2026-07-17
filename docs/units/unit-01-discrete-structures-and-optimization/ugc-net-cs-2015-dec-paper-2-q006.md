# Question 6

*UGC NET CS · 2015 Dec Paper 2 · Mathematical Logic · Validity of Arguments*

Which of the following arguments are not valid? (a) If Gora gets the job and works hard, then he will be promoted. If Gora gets promoted, then he will be happy. He will not be happy; therefore, either he will not get the job or he will not work hard. (b) Either Puneet is not guilty or Pankaj is telling the truth. Pankaj is not telling the truth; therefore, Puneet is not guilty. (c) If n is a real number such that n > 1, then n² > 1. Suppose that n² > 1; then n > 1.

- **1.** (a) and (c)
- **2.** (b) and (c)
- **3.** (a), (b) and (c)
- **4.** (a) and (b)

> [!TIP]
> **Correct answer: No listed option — only argument (c) is invalid**

## Solution

Let J mean ‘gets the job’, W ‘works hard’, P ‘is promoted’, and H ‘is happy’. In (a), ¬H and P→H give ¬P; then (J∧W)→P and ¬P give ¬(J∧W), equivalent to ¬J∨¬W. So (a) is valid. In (b), ¬G∨T together with ¬T yields ¬G by disjunctive syllogism, so it is valid. Argument (c) affirms the consequent: n>1 implies n²>1, but n²>1 does not imply n>1; n=−2 is a counterexample. Thus only (c) is invalid, a code the paper does not provide.

## Key Points

- Test argument validity by formal inference rules; disprove a claimed converse with one counterexample.

## Why the other options are incorrect

Every offered code includes (a), (b), or both among the invalid arguments, but both are valid. An implication cannot generally be reversed merely because its conclusion is true.
