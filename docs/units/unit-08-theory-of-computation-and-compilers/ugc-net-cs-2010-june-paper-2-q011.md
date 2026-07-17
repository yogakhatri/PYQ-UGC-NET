# Question 11

*UGC NET CS · 2010 June Paper 2 · Code Generation and Optimization · Control-Flow and Data-Flow Analysis*

The statement print f (“ % d”, 10 ? 0 ? 5 : 1 : 12); will print

- **A.** 10
- **B.** 0
- **C.** 12
- **D.** 1

> [!TIP]
> **Correct answer: D. 1**

## Solution

The conditional operator associates right-to-left, so the expression is 10 ? (0 ? 5 : 1) : 12. Since 10 is nonzero, evaluate the inner conditional; since 0 is false, it yields 1. Therefore printf prints 1.

## Key Points

- Parse nested ?: operators right-to-left, then follow only the selected branches.

## Why the other options are incorrect

10 is the condition, not the returned true expression. The outer false branch 12 is not selected, and the inner true branch 5 is not selected.
