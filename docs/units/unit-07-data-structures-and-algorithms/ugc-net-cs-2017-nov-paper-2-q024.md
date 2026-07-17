# Question 24

*UGC NET CS · 2017 Nov Paper 2 · Performance Analysis and Recurrences · String-Comparison Cost in Merge Sort*

A list of n strings, each of length n, is sorted into lexicographic order using merge - sort algorithm. The worst case running time of this computation is :

- **1.** O(n log n)
- **2.** O(n² log n)
- **3.** O(n² + log n)
- **4.** O(n³)

> [!TIP]
> **Correct answer: 2. O(n² log n)**

## Solution

Merge sort performs O(n log n) key comparisons when sorting n items. Here each item is a string of length n, and a worst-case lexicographic comparison may examine all n characters—for example, when strings share a long prefix. Multiplying the number of comparisons by the cost per comparison gives O(n log n)×O(n)=O(n² log n). Thus option 2 is correct.

## Key Points

- When keys are nonconstant-size objects, total sorting time = number of key comparisons × worst-case cost of one key comparison.

## Why the other options are incorrect

Option 1 treats every string comparison as constant time. Option 3 adds the costs instead of multiplying comparison count by comparison cost. Option 4 is a looser cubic upper bound, not the requested tight worst-case order supplied by merge sort analysis.
