# Question 25

*UGC NET CS · 2013 Dec Paper 2 · Sorting and Searching · Worst-Case Merge Comparisons*

Given two sorted list of size ‘m’ and ‘n’ respectively. The number of comparison needed in the worst case by the merge sort algorithm will be

- **A.** m × n
- **B.** max (m, n)
- **C.** min (m, n)
- **D.** m + n – 1

> [!TIP]
> **Correct answer: D. m + n – 1**

## Solution

Merge compares the first unconsumed elements of the two sorted lists and removes the smaller. In the worst case, neither list becomes empty until only one of the total m+n elements remains. Selecting the first m+n-1 elements therefore needs m+n-1 comparisons; the last element is then copied without comparison.

## Key Points

- Worst-case comparisons when merging sorted lists of lengths m and n equal m+n-1.

## Why the other options are incorrect

m x n would compare every cross-list pair and is unnecessary. max(m,n) and min(m,n) underestimate interleaved worst cases. The linear bound is what makes merging efficient.
