# Question 3

*UGC NET CS · 2015 June Paper 2 · Counting, Mathematical Induction and Discrete Probability · Positive Integer Distributions*

In how many ways can 15 indistinguishable fish be placed into 5 distinct ponds so that every pond contains at least one fish?

- **1.** 1001
- **2.** 3876
- **3.** 775
- **4.** 200

> [!TIP]
> **Correct answer: 1. 1001**

## Solution

Let xᵢ be the fish count in pond i. The ponds are distinct and every pond must be nonempty, so x₁+⋯+x₅=15 with xᵢ≥1. Give one fish to each pond, leaving 10 indistinguishable fish to distribute freely. Stars and bars gives C(10+5−1,5−1)=C(14,4)=1001.

## Key Points

- Positive distributions: allocate one to each box, then count nonnegative distributions of the remainder.

## Why the other options are incorrect

The other values do not equal the positive-solution count. Treating the ponds as indistinguishable or the fish as distinguishable changes the model; the question explicitly has indistinguishable fish and five different ponds.
