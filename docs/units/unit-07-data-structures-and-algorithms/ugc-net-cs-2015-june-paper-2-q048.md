# Question 48

*UGC NET CS · 2015 June Paper 2 · Sorting Algorithms · Linear-Time Radix Sort for Polynomial Key Ranges*

Which of the following algorithms sorts n integers in the range 0 to (n^2 - 1), in ascending order, in O(n) time?

- **1.** Selection sort
- **2.** Bubble sort
- **3.** Radix sort
- **4.** Insertion sort

> [!TIP]
> **Correct answer: 3. Radix sort**

## Solution

Represent each key from `0` through `n^2 - 1` as a two-digit number in base `n`: `x = high × n + low`, with both digits in `0..n-1`. A stable counting-sort pass on the low digit and then on the high digit costs `O(n + n) = O(n)` per pass. There are exactly two passes, so radix sort completes in `O(n)` time.

## Key Points

- Keys below `n^2` have only two base-`n` digits, so two stable linear counting passes give linear-time radix sort.

## Why the other options are incorrect

Selection sort and bubble sort take `Θ(n^2)` in the general and worst cases. Insertion sort also has `Θ(n^2)` worst-case time. None uses the bounded integer range to achieve the requested linear bound.
