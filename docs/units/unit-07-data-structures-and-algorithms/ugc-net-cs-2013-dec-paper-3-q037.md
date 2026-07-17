# Question 37

*UGC NET CS · 2013 Dec Paper 3 · Dynamic Programming · Longest Common Subsequence*

The longest common subsequence of the sequences X = <A, B, C, B, D, A, B> and Y = <B, D, C, A, B, A> has length

- **A.** 2
- **B.** 3
- **C.** 4
- **D.** 5

> [!TIP]
> **Correct answer: C. 4**

## Solution

A common subsequence of length 4 exists: B-C-B-A occurs in X at positions 2,3,4,6 and in Y at positions 1,3,5,6. Dynamic programming confirms no length-5 common subsequence exists. Using L[i,j]=L[i-1,j-1]+1 when the current symbols match and max(L[i-1,j],L[i,j-1]) otherwise, the final table entry is L[7,6]=4.

## Key Points

- To establish an LCS answer, exhibit a subsequence of that length and use the DP recurrence to rule out a longer one.

## Why the other options are incorrect

Lengths 2 and 3 are possible but not longest because the explicit subsequence BCBA has length 4. Length 5 is ruled out by the LCS dynamic-programming result.
