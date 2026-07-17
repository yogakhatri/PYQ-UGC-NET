# Question 126

*UGC NET CS · 2019 Dec Paper 1 And 2 · Design Techniques · Dynamic-Programming Correctness and Complexity*

Consider the following statements. (a) The running time of a dynamic-programming algorithm is always Θ(p), where p is the number of subproblems. (b) When a recurrence relation has a cyclic dependency, it is impossible to use that recurrence relation unmodified in a correct dynamic program. (c) Computing all values bottom-up is asymptotically faster than recursion with memoization for every dynamic-programming algorithm. (d) If a problem X can be reduced to a known NP-hard problem, then X must be NP-hard. Which statement(s) are true?

- **1.** Only (a) and (b)
- **2.** Only (b)
- **3.** Only (b) and (c)
- **4.** Only (b) and (d)

> [!TIP]
> **Correct answer: 2. Only (b)**

## Solution

Only statement (b) is universally true. A dynamic program relies on a well-founded dependency order: every subproblem must be computable from already solved smaller subproblems. If the recurrence contains a cycle, that unmodified recurrence gives no such order, so it cannot directly define a correct bottom-up or memoized computation. Statement (a) is false because p counts subproblems but says nothing about the work per subproblem; the total is the sum of those costs, not always Θ(p). Statement (c) is false because bottom-up and memoized versions often have the same asymptotic complexity, while memoization may even avoid unreachable states. Statement (d) reverses a reduction: X≤pH shows that H is at least as hard as X, not that X is NP-hard. Therefore option 2.

## Key Points

- Count both subproblems and work per subproblem, require an acyclic dependency order, and never reverse the direction of a hardness reduction.

## Why the other options are incorrect

Options 1 and 3 include false claims about dynamic-programming running time. Option 4 includes the incorrectly directed NP-hardness argument. To prove X NP-hard, a known NP-hard problem H must reduce to X, written H≤pX.
