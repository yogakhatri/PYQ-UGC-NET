# Question 31

*UGC NET CS · 2014 Dec Paper 3 · Lower-Bound Theory · Decision-Tree Lower Bound for Sorting*

Any decision tree that sorts n elements has height

- **A.** Ω(n)
- **B.** Ω(log n)
- **C.** Ω(n log n)
- **D.** Ω(n²)

> [!TIP]
> **Correct answer: C. Ω(n log n)**

## Solution

A comparison-sorting decision tree needs at least one leaf for each of the n! possible input orders. A binary tree of height h has at most 2ʰ leaves, so 2ʰ≥n! and h≥log₂(n!). By Stirling's approximation, log(n!)=Θ(n log n). Therefore every comparison-based sorting decision tree has height Ω(n log n).

## Key Points

- Count the n!
- possible orderings, bound a height-h binary tree by 2ʰ leaves, and take logarithms.

## Why the other options are incorrect

Ω(n) and Ω(log n) are weaker true lower bounds, but they do not state the tight asymptotic lower bound sought by the sorting decision-tree argument. Ω(n²) is too strong because algorithms such as merge sort and heapsort use O(n log n) comparisons.
