# Question 78

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Advanced Algorithms · Searching and Merging*

S1.0:87028 Suppose we store n keys in a hash table of size m=n using a hash function h randomly chosen from a universal class of _that there are any collisions. hash functions. Then the probability is

- **1.** greater than 1/5
- **2.** greater than 1/2
- **3.** less than 1/2
- **4.** less than 1/5

> [!TIP]
> **Correct answer: 3. less than 1/2**

## Solution

There are C(n,2) key pairs. Universality bounds each pair's collision probability by 1/m=1/n². By the union bound, Pr(any collision)≤C(n,2)/n²=(n−1)/(2n)<1/2.

## Key Points

- Union-bound all pair-collision events: C(n,2)/m.

## Why the other options are incorrect

The calculation gives a strict upper bound below one-half, not above it; it is not always below one-fifth.
