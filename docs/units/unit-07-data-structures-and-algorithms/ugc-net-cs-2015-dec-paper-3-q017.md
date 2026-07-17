# Question 17

*UGC NET CS · 2015 Dec Paper 3 · Dynamic Programming · Longest Common Subsequence*

For X=⟨a,b,c,b,d,a,b⟩ and Y=⟨b,d,c,a,b,a⟩, which option is a longest common subsequence?

- **1.** b, c, a
- **2.** c, a, b
- **3.** b, c, a, a
- **4.** b, c, b, a

> [!TIP]
> **Correct answer: 4. b, c, b, a**

## Solution

The sequence ⟨b,c,b,a⟩ occurs in X at positions 2,3,4,6 and in Y at positions 1,3,5,6, so it is a common subsequence of length 4. A dynamic-programming LCS table for the two length-7 and length-6 sequences gives maximum length 4, so this common subsequence is longest.

## Key Points

- A subsequence preserves relative order but need not use consecutive positions; verify positions in both strings.

## Why the other options are incorrect

Options 1 and 2 have length only 3. Option 3 is not a subsequence of X: after choosing b,c,a there is no later a available for the fourth symbol.
