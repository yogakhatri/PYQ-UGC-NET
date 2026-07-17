# Question 77

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Data Structures · Minimum weighted external path length*

S.N:87027 Given six weights 4,15,25,5,8, 16 construct a 2-T tree. What is the minimum weighted path length?

- **1.** 231
- **2.** 172
- **3.** 73
- **4.** 77

> [!TIP]
> **Correct answer: 2. 172**

## Solution

Huffman's 2-tree algorithm repeatedly combines the two smallest weights: 4+5=9, 8+9=17, 15+16=31, 17+25=42, 31+42=73. The minimum weighted path length equals the sum of merge weights: 9+17+31+42+73=172.

## Key Points

- For a Huffman tree, WPL equals the sum of all pairwise merge totals.

## Why the other options are incorrect

73 is only the root weight (sum of leaves), not the weighted external path length; 77 and 231 do not follow the optimal merges.
