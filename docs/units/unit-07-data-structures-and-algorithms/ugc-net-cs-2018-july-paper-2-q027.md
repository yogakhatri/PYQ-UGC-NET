# Question 27

*UGC NET CS · 2018 July Paper 2 · Design Techniques · Matching Problems to Algorithm Paradigms*

Match the following with respect to algorithm paradigms : List - I List - II (a) The 8-Queen’s problem (i) Dynamic programming (b) Single-Source shortest paths (ii) Divide and conquer (c) STRASSEN’s Matrix multiplication (iii) Greedy approach (d) Optimal binary search trees (iv) Backtracking Code : (a) (b) (c) (d)

- **1.** (iv) (i) (iii) (ii)
- **2.** (iv) (iii) (i) (ii)
- **3.** (iii) (iv) (ii) (i)
- **4.** (iv) (iii) (ii) (i)

> [!TIP]
> **Correct answer: 4. (iv) (iii) (ii) (i)**

## Solution

The 8-Queens search places queens and backtracks when a partial placement conflicts, so a→iv. Standard single-source shortest paths with nonnegative weights uses greedy Dijkstra, so b→iii. Strassen recursively divides matrices into blocks, so c→ii. Optimal binary search trees use interval dynamic programming, so d→i. The sequence (iv),(iii),(ii),(i) is option 4.

## Key Points

- Canonical examples: N-Queens/backtracking, Dijkstra/greedy, Strassen/divide-and-conquer, optimal BST/dynamic programming.

## Why the other options are incorrect

The other mappings swap well-known paradigm examples. Strassen is not greedy or dynamic programming; optimal BST is not divide-and-conquer alone because it stores and reuses optimal interval subproblems.
