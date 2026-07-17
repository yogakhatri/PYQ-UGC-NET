# Question 1

*UGC NET CS · 2013 Dec Paper 3 · Optimization · Primal-Dual Feasibility and Unboundedness*

If the primal Linear Programming problem has unbounded solution, then it’s dual problem will have

- **A.** feasible solution
- **B.** alternative solution
- **C.** no feasible solution at all
- **D.** no bounded solution at all

> [!TIP]
> **Correct answer: C. no feasible solution at all**

## Solution

Weak duality says every feasible dual objective bounds every feasible primal objective. If the primal objective can improve without bound while the dual had a feasible solution with a finite objective, that dual value would provide a bound—a contradiction. Therefore an unbounded primal implies an infeasible dual.

## Key Points

- Primal unbounded ⇒ dual infeasible.
- Dual unbounded ⇒ primal infeasible; an infeasible problem does not alone determine the other problem's status.

## Why the other options are incorrect

A feasible dual cannot coexist with an unbounded primal under the usual primal-dual pair. Alternative optima concern multiple finite optimal points. 'No bounded solution' is imprecise; the definite conclusion is that no dual feasible solution exists.
