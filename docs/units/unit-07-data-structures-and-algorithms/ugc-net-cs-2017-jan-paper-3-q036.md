# Question 36

*UGC NET CS · 2017 Jan Paper 3 · Design Techniques · Matching Problems to Algorithmic Paradigms*

Match the following with respect to algorithm paradigms : List – I List – II a. Merge sort i. Dynamic programming b. Huffman coding ii. Greedy approach c. Optimal polygon triangulation iii. Divide and conquer d. Subset sum problem iv. Back tracking Codes : a b c d

- **1.** iii i ii iv
- **2.** ii i iv iii
- **3.** ii i iii iv
- **4.** iii ii i iv

> [!TIP]
> **Correct answer: 4. iii ii i iv**

## Solution

Merge sort splits the input and recursively combines sorted halves, so a→iii (divide and conquer). Huffman coding repeatedly combines the two least frequent items, so b→ii (greedy). Optimal polygon triangulation combines optimal solutions of overlapping subpolygons, so c→i (dynamic programming). A standard exact subset-sum search chooses or rejects each item and backtracks, so d→iv. The code iii, ii, i, iv is option 4.

## Key Points

- Recognize paradigms by structure: split/combine, greedy safe choice, overlapping optimal subproblems, or reversible search choices.

## Why the other options are incorrect

The other codes assign at least one problem to the wrong design pattern. The distinctive clues are recursive splitting for merge sort, locally cheapest merging for Huffman, overlapping subproblems for triangulation, and include/exclude search for subset sum.
