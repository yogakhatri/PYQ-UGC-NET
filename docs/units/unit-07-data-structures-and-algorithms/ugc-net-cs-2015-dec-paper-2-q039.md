# Question 39

*UGC NET CS · 2015 Dec Paper 2 · Sorting Algorithms · In-Place Sorting and Auxiliary Space*

An ideal sort is an in-place sort whose additional space requirement is:

- **1.** O(log2 n)
- **2.** O(n log2 n)
- **3.** O(1)
- **4.** O(n)

> [!TIP]
> **Correct answer: 3. O(1)**

## Solution

An in-place sorting algorithm rearranges elements within the input array using only a constant number of extra variables. Its ideal auxiliary-space requirement is therefore O(1), independent of n.

## Key Points

- In-place sorting aims for constant auxiliary storage, O(1).

## Why the other options are incorrect

O(log n) can arise from a recursion stack, but it is not the strict constant-space ideal in-place target asked here. O(n log n) and O(n) require storage growing with the input and are not in-place by this definition.
