# Question 36

*UGC NET CS · 2015 June Paper 3 · Data Structures · Node-Height Bound in Binary Heaps*

The number of nodes of height h in any n-element binary heap is bounded by:

- **1.** h
- **2.** 2^h
- **3.** ceil(n / 2^h)
- **4.** ceil(n / 2^(h+1))

> [!TIP]
> **Correct answer: 4. ceil(n / 2^(h+1))**

## Solution

In the array representation of a binary heap, roughly half the nodes are leaves (height 0), one quarter can have height 1, one eighth can have height 2, and so on. The standard bound is that an n-element heap has at most `ceil(n / 2^(h+1))` nodes of height h. Therefore option 4 is the intended theorem.

## Key Points

- Heap nodes thin geometrically with height: at most n/2^(h+1) nodes have height h.

## Why the other options are incorrect

The quantities h and `2^h` do not depend correctly on n. `ceil(n/2^h)` is one factor of two too large. Strictly, the source should say `at most`; the displayed expression is a bound and need not equal the exact count for every n and h.
