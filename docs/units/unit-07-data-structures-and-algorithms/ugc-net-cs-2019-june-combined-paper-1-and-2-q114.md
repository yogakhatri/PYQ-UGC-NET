# Question 114

*UGC NET CS · 2019 June Paper 1 And 2 · Advanced Algorithms · Radix Sort for Bounded Integers*

Which is the best running time to sort n integers in the range 0 to n^2-1?

- **1.** O(log n)
- **2.** O(n)
- **3.** O(n log n)
- **4.** O(n^2)

> [!TIP]
> **Correct answer: 2. O(n)**

## Solution

Write each number in base n. Because every key lies between 0 and n^2-1, it has at most two base-n digits. A stable counting sort can process one digit in O(n+n)=O(n) time because there are n records and n possible digit values. Two radix-sort passes therefore take O(2n)=O(n), which is optimal because reading n inputs already costs Omega(n).

## Key Points

- A bounded integer range can beat comparison sorting: two base-n digits plus stable counting sort give linear time.

## Why the other options are incorrect

- **O(log n):** impossible for sorting n explicit inputs because they must all be inspected.
- **O(n log n):** is the comparison-sorting lower bound, but integer radix sorting uses the restricted key range.
- **O(n^2):** is achievable but not the best bound.
