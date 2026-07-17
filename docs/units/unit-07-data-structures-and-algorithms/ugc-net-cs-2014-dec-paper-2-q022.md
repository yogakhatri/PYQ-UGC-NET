# Question 22

*UGC NET CS · 2014 Dec Paper 2 · Sorting Algorithms · Insertion Sort for Nearly Sorted Data*

A list L consists of a sorted prefix followed by a few random elements. Which sorting method is most suitable?

- **A.** Bubble sort
- **B.** Selection sort
- **C.** Quick sort
- **D.** Insertion sort

> [!TIP]
> **Correct answer: D. Insertion sort**

## Solution

Insertion sort is adaptive: an element moves left only across elements larger than it. A sorted prefix requires almost no work, and each of the few random tail elements can be inserted into that prefix. Its time is O(n+k), where k is the number of inversions, so a nearly sorted list can be processed close to linearly.

## Key Points

- Insertion sort's work is proportional to inversions, making it ideal for nearly sorted input.

## Why the other options are incorrect

Selection sort always performs Θ(n²) comparisons regardless of existing order. Ordinary quicksort does not directly exploit the long sorted prefix and can choose poor pivots. Bubble sort can be adaptive with an early-exit flag, but insertion sort is the standard and more direct choice for a sorted run plus a few out-of-place elements.
