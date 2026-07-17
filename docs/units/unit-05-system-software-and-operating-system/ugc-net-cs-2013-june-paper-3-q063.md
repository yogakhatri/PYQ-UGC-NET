# Question 63

*UGC NET CS · 2013 June Paper 3 · Memory Management · Working Set and Locality*

The working-set model is used in memory management to implement the concept of

- **A.** Swapping
- **B.** Principle of locality
- **C.** Segmentation
- **D.** Thrashing

> [!TIP]
> **Correct answer: B. Principle of locality**

## Solution

The working set W(t,Δ) is the set of pages referenced during a recent window of execution. Programs tend to revisit a relatively small current locality, so keeping that working set resident implements the principle of locality. If the sum of active working sets exceeds physical memory, the OS can suspend processes instead of allowing continuous page replacement.

## Key Points

- The recent-reference window estimates a process's current locality and its needed resident pages.

## Why the other options are incorrect

Swapping and segmentation are different memory-management mechanisms. Thrashing is a harmful condition the working-set model helps prevent; it is not the underlying concept the model implements.
