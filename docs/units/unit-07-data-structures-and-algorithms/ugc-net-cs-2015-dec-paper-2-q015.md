# Question 15

*UGC NET CS · 2015 Dec Paper 2 · Performance Analysis · Recursive versus Iterative Implementations*

In general, in a recursive and non-recursive implementation of a problem (program) :

- **1.** Both time and space complexities are better in recursive than in non-recursive program.
- **2.** Both time and space complexities are better in non-recursive than in recursive program.
- **3.** Time complexity is better in recursive version but space complexity is better in non-recursive version of the program.
- **4.** Space complexity is better in recursive version but time complexity is better in non-recursive version of the program.

> [!TIP]
> **Correct answer: 2. Both time and space complexities are better in non-recursive than in recursive program.**

## Solution

The exam's intended general comparison is that an iterative/non-recursive implementation avoids function-call overhead and the implicit recursion stack, so it typically uses less time and auxiliary space than a straightforward recursive implementation. On that textbook interpretation, option 2 is the best answer.

## Key Points

- Iteration usually removes recursive call-stack overhead, but always compare concrete algorithms rather than treating this as a universal law.

## Why the other options are incorrect

Options 1, 3, and 4 claim a general resource advantage for recursion, although ordinary recursion adds call and stack costs. Strictly speaking, this is a heuristic rather than a universal asymptotic theorem: equivalent recursive and iterative algorithms often have the same big-O time, and tail-call optimization or a necessary explicit stack can change the comparison.
