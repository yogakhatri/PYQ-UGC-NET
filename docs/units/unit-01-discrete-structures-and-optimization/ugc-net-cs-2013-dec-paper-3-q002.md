# Question 2

*UGC NET CS · 2013 Dec Paper 3 · Optimization · Karush-Kuhn-Tucker Conditions*

Given the problem to maximize f( x), X = (x1, x2,......xn) subject to m number of inequality constraints. g i(x) ≤ bi, i = 1, 2......m including the non-negativity constraints x ≥ 0. Which of the following conditions is a Kuhn-Tucker necessary condition for a local maxima at –x ?

- **A.** ∂L(–X, –λ , –S) ∂xj = 0, j = 1, 2….m
- **B.** –λi [gi (–X) – bi]= 0, i = 1, 2 ….m
- **C.** g i (–X) ≤ bi, i = 1, 2 ….m
- **D.** All of these

> [!TIP]
> **Correct answer: D. All of these**

## Solution

The Karush-Kuhn-Tucker necessary conditions include stationarity of the Lagrangian with respect to every decision variable, primal feasibility gi(x̄)≤bi, dual feasibility for the multipliers/slacks under the chosen sign convention, and complementary slackness λ̄i[gi(x̄)-bi]=0. The three displayed statements are members of this set.

## Key Points

- KKT checklist: stationarity, primal feasibility, dual feasibility and complementary slackness.

## Why the other options are incorrect

A, B and C each state only one necessary part: stationarity, complementary slackness or primal feasibility. Selecting one alone omits the others, so the complete answer is all of these.
