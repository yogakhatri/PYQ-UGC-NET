# Question 13

*UGC NET CS · 2013 June Paper 3 · Trees and Heaps · Number of Heap Nodes at a Given Height*

In any n-element heap, the number of nodes of height h is

- **A.** at most ceil(n/2^h)
- **B.** greater than ceil(n/2^h)
- **C.** greater than ceil(n/2^(h+1))
- **D.** at most ceil(n/2^(h+1))

> [!TIP]
> **Correct answer: D. at most ceil(n/2^(h+1))**

## Solution

An n-element binary heap is an almost-complete binary tree. A node of height h roots a subtree that, except near the final incomplete level, accounts for about 2^(h+1) positions. Counting the possible roots yields the standard bound: the number of nodes of height h is at most ceil(n/2^(h+1)). For h=0 this says the number of leaves is at most ceil(n/2), which matches heap structure.

## Key Points

- Heap height-count lemma: at most ceil(n/2^(h+1)) nodes have height h.

## Why the other options are incorrect

A's denominator 2^h is too small and gives a weaker, nonstandard level bound; at h=0 it merely says at most n. B and C claim lower bounds ('greater than') that fail for many heaps and heights. D states the standard upper bound.
