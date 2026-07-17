# Question 108

*UGC NET CS · 2019 Dec Paper 1 And 2 · Reasoning under Uncertainty · Dempster-Shafer Belief and Plausibility*

According to Dempster–Shafer theory for uncertainty management, which relation is always valid? Here Bel(A) denotes the belief in event A.

- **1.** Bel(A) + Bel(¬A) ≤ 1
- **2.** Bel(A) + Bel(¬A) ≥ 1
- **3.** Bel(A) + Bel(¬A) = 1
- **4.** Bel(A) + Bel(¬A) = 0

> [!TIP]
> **Correct answer: 1. Bel(A) + Bel(¬A) ≤ 1**

## Solution

Dempster–Shafer belief and plausibility satisfy Pl(A)=1−Bel(¬A) and Bel(A)≤Pl(A). Substituting gives Bel(A)≤1−Bel(¬A), hence Bel(A)+Bel(¬A)≤1. The gap can represent belief mass committed to a larger set that supports neither A nor ¬A specifically—epistemic ignorance. Therefore option 1 is always valid.

## Key Points

- Belief is a lower support bound and plausibility an upper bound; Pl(A)=1−Bel(¬A) immediately yields the inequality.

## Why the other options are incorrect

The sum need not be at least or exactly 1 because uncommitted evidence may remain. It is not always 0 either; evidence can directly support A or its complement. Equality with 1 is a special probability-like case, not the general Dempster–Shafer rule.
