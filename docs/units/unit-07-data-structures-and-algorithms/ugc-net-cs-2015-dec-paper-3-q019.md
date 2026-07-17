# Question 19

*UGC NET CS · 2015 Dec Paper 3 · Performance Analysis and Recurrences · Recurrence Relations*

Solve the recurrence T(n)=Θ(1) for n≤80, and T(n)≤T(n/5)+T(7n/10+6)+O(n) for n>80.

- **1.** O(lg n)
- **2.** O(n)
- **3.** O(n lg n)
- **4.** None of the above

> [!TIP]
> **Correct answer: 2. O(n)**

## Solution

Ignoring the harmless +6 for intuition, the two recursive subproblems contain n/5+7n/10=0.9n total input, while the current call does O(n) work. At every deeper level the total linear work shrinks geometrically by about 0.9; the +6 is controlled by the n>80 cutoff and changes only constants. Therefore the level costs sum to O(n)(1+0.9+0.9²+…)=O(n).

## Key Points

- When recursive subproblem sizes sum to less than n and each node does linear work, the recursion-tree level costs form a convergent geometric series.

## Why the other options are incorrect

O(log n) ignores the linear work at the root alone. O(n log n) would arise when each level retained total size n, but here the child-size sum is strictly below n. Hence ‘none’ is unnecessary.
