# Question 73

*UGC NET CS · 2018 Dec Paper 1 And 2 · Dynamic Programming · Longest Common Subsequence*

Let X=<0,1,2,1,3,0,1> and Y=<1,3,2,0,1,0>. What is the length of a longest common subsequence of X and Y?

- **1.** 2
- **2.** 3
- **3.** 4
- **4.** 5

> [!TIP]
> **Correct answer: 3. 4**

## Solution

Use the LCS recurrence: if the current elements match, add 1 to the diagonal DP value; otherwise take the larger value from deleting one current element. Filling the 7×6 table gives final value LCS(7,6)=4. A concrete common subsequence of that length is <1,2,0,1>: in X it occurs at positions 2,3,6,7, and in Y at positions 1,3,4,5. Therefore option 3 is correct.

## Key Points

- LCS preserves order but not adjacency; dynamic programming proves optimality, while an explicit subsequence proves attainability.

## Why the other options are incorrect

Lengths 2 and 3 are too small because the explicit length-4 subsequence exists. Length 5 is ruled out by the completed dynamic-programming table; a subsequence must preserve relative order, so merely finding five shared values is insufficient.
