# Question 32

*UGC NET CS · 2014 Dec Paper 3 · Performance Analysis and Recurrences · Matching Standard Algorithm Complexities*

Match List I with List II. a. Bucket sort; b. Matrix-chain multiplication; c. Huffman codes; d. All-pairs shortest paths. i. O(n³ log n); ii. O(n³); iii. O(n log n); iv. O(n). Choose the code in the order a, b, c, d.

- **A.** iv ii i iii
- **B.** ii iv i iii
- **C.** iv ii iii i
- **D.** iii ii iv i

> [!TIP]
> **Correct answer: C. iv ii iii i**

## Solution

Under the conventional implementations assumed by the list, bucket sort is O(n) on its average-case distribution assumptions, so a→iv. Matrix-chain dynamic programming fills O(n²) states and may try O(n) split points per state, so b→ii, O(n³). Building a Huffman tree with a priority queue is O(n log n), so c→iii. The remaining listed bound for all-pairs shortest paths is i, O(n³ log n), as obtained by running a heap-based single-source method on a dense graph. Thus the code is iv, ii, iii, i.

## Key Points

- Use the standard cues: bucket average linear, matrix-chain DP cubic, Huffman heap n log n; then interpret the APSP entry according to the listed implementation bound.

## Why the other options are incorrect

A assigns Huffman coding the O(n³ log n) bound. B gives bucket sort cubic time and matrix-chain multiplication linear time. D swaps the near-linear bucket/Huffman matches. A useful caveat is that Floyd–Warshall solves all-pairs shortest paths in O(n³), so O(n³ log n) is an implementation-specific listed bound, not the tightest universal APSP bound.
