# Question 102

*UGC NET CS · 2019 Dec Paper 1 And 2 · Unsolvable Problems and Computational Complexity · Halting and Post Correspondence Problems*

For the Post Correspondence Problem, let A = (001, 0011, 11, 101) and B = (01, 111, 111, 010). Also let C = (00, 001, 1000) and D = (0, 11, 011). Which pair(s) have a PCP solution?

- **1.** Only pair (A, B)
- **2.** Only pair (C, D)
- **3.** Both (A, B) and (C, D)
- **4.** Neither (A, B) nor (C, D)

> [!TIP]
> **Correct answer: 1. Only pair (A, B)**

## Solution

For (A,B), choose tile indices 3,4,1. The top concatenation is 11·101·001=11101001, and the bottom concatenation is 111·010·01=11101001, so this pair has a PCP solution. For (C,D), a solution must start with tile 1 because tiles 2 and 3 begin with mismatching top/bottom bits. Tile 1 leaves an unmatched 0 on the top; another tile 1 only increases that excess, while tile 2 or 3 creates a permanent prefix mismatch. Hence (C,D) has no solution, and option 1 is correct.

## Key Points

- For a small PCP instance, search only sequences whose current top and bottom strings remain prefix-compatible; a permanent mismatch can never be repaired.

## Why the other options are incorrect

Options 2 and 4 overlook the explicit solution (3,4,1) for (A,B). Option 3 incorrectly asserts a solution for (C,D); PCP concatenations must agree at every prefix, and after the forced first tile no later tile can remove the top's unmatched zero prefix.
