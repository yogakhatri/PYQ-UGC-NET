# Question 21

*UGC NET CS · 2018 July Paper 2 · Performance Analysis and Recurrences · Geometrically Shrinking Recurrences*

The solution of the recurrence T(m)=T(3m/4)+1 is:

- **1.** θ (lg m)
- **2.** θ (m)
- **3.** θ (mlg m)
- **4.** θ (lglg m)

> [!TIP]
> **Correct answer: 1. θ (lg m)**

## Solution

After k recursive calls, the argument is m(3/4)^k. Recursion stops when this becomes constant: m(3/4)^k≈1. Solving gives k≈log_{4/3}m. Each level contributes only the constant `+1`, so T(m)=Θ(k)=Θ(log m). Therefore option 1 is correct.

## Key Points

- Repeated multiplication by any fixed factor between 0 and 1 reaches constant size in Θ(log m) steps.

## Why the other options are incorrect

Linear and m log m would require work proportional to m across the recursion, which is absent. log log m arises from much faster shrinkage such as repeatedly taking a square root, not multiplying by a fixed fraction.
