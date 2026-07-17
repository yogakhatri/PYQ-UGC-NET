# Question 118

*UGC NET CS · 2019 June Paper 1 And 2 · Design Techniques · Dynamic Programming and Greedy Method*

Consider two steps: S1: characterize the structure of an optimal solution; S2: compute the value of an optimal solution in bottom-up fashion. Which step is common to both dynamic programming and greedy algorithms?

- **1.** Only S1
- **2.** Only S2
- **3.** Both S1 and S2
- **4.** Neither S1 nor S2

> [!TIP]
> **Correct answer: 1. Only S1**

## Solution

Both design methods begin by identifying the structure of an optimal solution, usually through optimal substructure, so S1 is common. Bottom-up computation of a table of subproblem values is characteristic of dynamic programming. A greedy method instead makes a locally optimal choice and continues with the remaining subproblem; it need not fill a bottom-up table. Therefore only S1 is common.

## Key Points

- Both exploit optimal structure; bottom-up tabulation belongs specifically to dynamic programming.

## Why the other options are incorrect

Options 2 and 3 incorrectly treat bottom-up tabulation as a necessary greedy step. Option 4 ignores that both methods require a proof or characterization of optimal-solution structure.
