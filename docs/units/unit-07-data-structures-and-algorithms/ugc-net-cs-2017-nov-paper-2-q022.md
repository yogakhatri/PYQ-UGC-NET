# Question 22

*UGC NET CS · 2017 Nov Paper 2 · Data Structures · Binary Search Tree Construction and Height*

The following numbers are inserted into an empty binary search tree in the given order : 10, 1, 3, 5, 15, 12, 16. What is the height of the binary search tree ?

- **1.** 3
- **2.** 4
- **3.** 5
- **4.** 6

> [!TIP]
> **Correct answer: 1. 3**

## Solution

Insert 10 as root. Then 1 is its left child; 3 is the right child of 1; and 5 is the right child of 3. On the right of 10, 15 has children 12 and 16. The longest root-to-leaf path is 10→1→3→5, which contains 3 edges. Under the standard algorithmic definition—height equals the number of edges on the longest downward path—the height is 3, so option 1 is correct.

## Key Points

- Always check the convention: edge-based tree height gives leaf=0; level-counting gives leaf=1.
- Here the intended answer is 3 edges.

## Why the other options are incorrect

Values 5 and 6 do not match either common height convention. If a source counts levels or nodes instead of edges, it would call this height 4 (option 2). The exam clearly intends the edge-count convention, with a leaf at height 0.
