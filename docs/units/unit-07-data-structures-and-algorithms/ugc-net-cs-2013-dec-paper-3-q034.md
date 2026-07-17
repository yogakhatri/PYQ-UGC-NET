# Question 34

*UGC NET CS · 2013 Dec Paper 3 · Algorithm Design and Analysis · Simultaneous Maximum and Minimum*

How many comparisons are necessary in the worst case to find both the maximum and minimum of n numbers?

- **A.** 2n - 2
- **B.** n + floor(lg n) - 2
- **C.** floor(3n/2) - 2
- **D.** 2 lg n - 2

> [!TIP]
> **Correct answer: For even n, option C: 3n/2-2 comparisons. For odd n, the exact bound is 3(n-1)/2, so the printed question has no single formula valid for every n.**

## Solution

Use the pairwise method. First compare the two elements in each pair; compare the larger one only with the current maximum and the smaller one only with the current minimum. For even n, initialization uses one comparison and the remaining (n-2)/2 pairs use three each: 1+3(n-2)/2=3n/2-2. For odd n, initialize both extrema with the unpaired element and process (n-1)/2 pairs, giving 3(n-1)/2 comparisons. Thus option C is the familiar intended answer under the usual even-n assumption, but its floor formula is one comparison too small when n is odd.

## Key Points

- Compare elements in pairs: one comparison separates a minimum candidate from a maximum candidate, saving about n/2 comparisons.

## Why the other options are incorrect

A, 2n-2, is the cost of finding minimum and maximum in two independent scans and is not optimal. B and D are not attainable comparison bounds for arbitrary unsorted inputs. C is exact for even n only, despite being the intended choice.
