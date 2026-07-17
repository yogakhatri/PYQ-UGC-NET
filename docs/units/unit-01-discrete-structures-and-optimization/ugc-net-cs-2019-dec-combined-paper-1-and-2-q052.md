# Question 52

*UGC NET CS · 2019 Dec Paper 1 And 2 · Optimization · Linear Programming - Mathematical Model*

Consider the linear programming problem: maximize z = x1 + x2 subject to x1 + 2x2 ≤ 2000, x1 + x2 ≤ 1500, x2 ≤ 600, and x1,x2 ≥ 0. Which listed point is an optimal solution?

- **1.** x1=750, x2=750, z=1500
- **2.** x1=500, x2=1000, z=1500
- **3.** x1=1000, x2=500, z=1500
- **4.** x1=900, x2=600, z=1500

> [!TIP]
> **Correct answer: 3. x1=1000, x2=500, z=1500**

## Solution

The constraint x1+x2≤1500 is also an upper bound on the objective z=x1+x2, so no feasible point can exceed z=1500. We only need find which listed point is feasible and reaches that bound. At (1000,500), x1+2x2=2000, x1+x2=1500, and x2=500≤600; all non-negativity constraints also hold. Thus it attains the upper bound and is optimal, option 3.

## Key Points

- When a constraint directly bounds the objective, test candidate feasibility and identify a point that attains that bound.

## Why the other options are incorrect

(750,750) violates x1+2x2≤2000 and x2≤600. (500,1000) violates both of those constraints. (900,600) satisfies x2≤600 and x1+x2=1500 but gives x1+2x2=2100, so it is infeasible. An objective value written beside a point does not make the point feasible.
