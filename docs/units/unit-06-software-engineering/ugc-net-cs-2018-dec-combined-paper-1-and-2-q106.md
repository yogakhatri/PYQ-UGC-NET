# Question 106

*UGC NET CS · 2018 Dec Paper 1 And 2 · Software Testing · Statement and Branch Coverage*

Consider the method: int f(int m, int n, boolean x, boolean y) { int res = 0; if (m < 0) { res = n - m; } else if (x || y) { res = -1; if (n == m) { res = 1; } } else { res = n; } return res; } If P is the minimum number of tests for full statement coverage and Q is the minimum number for full branch coverage, find (P, Q).

- **1.** (3,4)
- **2.** (4, 3)
- **3.** (2, 3)
- **4.** (3, 2)

> [!TIP]
> **Correct answer: 1. (3,4)**

## Solution

For full statement coverage, three mutually exclusive paths are necessary: one test with m<0 executes res=n-m; one with m≥0, x||y true, and n==m executes both res=-1 and res=1; and one with m≥0 and x||y false executes res=n. Hence P=3. For full branch coverage, both outcomes of three nested decisions must occur. Four paths are necessary: m<0; m≥0 with x||y false; m≥0 with x||y true and n==m; and m≥0 with x||y true and n!=m. Hence Q=4. Therefore (P,Q)=(3,4), option 1.

## Key Points

- Statement coverage counts executable statements; branch coverage requires both outcomes of each reachable decision and can require additional mutually exclusive paths.

## Why the other options are incorrect

Two tests cannot cover the three mutually exclusive assignment regions required for statement coverage. Three tests cannot cover the outer true branch, the middle false branch, and both true/false outcomes of the innermost decision; the latter two outcomes require separate tests after taking the same middle true branch.
