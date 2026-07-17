# Question 38

*UGC NET CS · 2013 Dec Paper 3 · Sorting Algorithms · Bucket and Counting Sort Complexity*

Assuming there are n keys and each key is in the range [0, m – 1]. The run time of bucket sort is

- **A.** O(n)
- **B.** O(n lgn)
- **C.** O(n lgm)
- **D.** O(n + m)

> [!TIP]
> **Correct answer: D. O(n + m)**

## Solution

For integer keys in [0,m-1], create m buckets or counters, scan the n input keys to place/count them, and then scan the m bucket positions to emit them in order. These two phases cost Theta(n) and Theta(m), so the total running time is Theta(n+m).

## Key Points

- Direct-address sorting pays once for the n records and once for the m-value key universe: n+m.

## Why the other options are incorrect

Theta(n) ignores the need to initialize or scan m possible key positions unless m is assumed proportional to n. Theta(n log n) is a comparison-sort bound and is unnecessary when keys can index buckets directly. Theta(n log m) does not describe the counting/bucket procedure.
