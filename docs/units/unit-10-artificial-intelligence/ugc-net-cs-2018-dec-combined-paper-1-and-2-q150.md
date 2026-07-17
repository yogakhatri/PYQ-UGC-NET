# Question 150

*UGC NET CS · 2018 Dec Paper 1 And 2 · Reasoning under Uncertainty · Conditional Probability from a Full Joint Distribution*

Using the given full joint distribution for Toothache, Cavity and Catch, what is the conditional probability distribution over Cavity given evidence of Toothache?

- **1.** <0.2, 0.8>
- **2.** <0.4, 0.8>
- **3.** <0.6, 0.8>
- **4.** <0.6, 0.4>

> [!TIP]
> **Correct answer: 4. <0.6, 0.4>**

## Solution

First sum out the unobserved variable Catch. For Cavity and Toothache, the mass is 0.108+0.012=0.120. For ¬Cavity and Toothache, it is 0.016+0.064=0.080. The evidence probability is P(Toothache)=0.120+0.080=0.200. Normalizing gives P(Cavity|Toothache)=0.120/0.200=0.6 and P(¬Cavity|Toothache)=0.080/0.200=0.4. The requested distribution is ⟨0.6,0.4⟩, option 4.

## Key Points

- Conditional inference from a full joint table: restrict to the evidence, sum out hidden variables, then normalize the remaining entries.

## Why the other options are incorrect

Options 1 and 2 do not match the normalized cavity probability. Option 3 sums to 1.4, and option 2 sums to 1.2, so neither can be a probability distribution. The key is to sum over both Catch values first and then divide both cavity cases by the total Toothache mass.
