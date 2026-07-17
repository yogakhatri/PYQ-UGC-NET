# Question 52

*UGC NET CS · 2015 Dec Paper 3 · Optimization · Degenerate Basic Feasible Solutions*

A basic feasible solution of a linear programming problem is said to be __________ if at least one of the basic variable is zero.

- **1.** degenerate
- **2.** non-degenerate
- **3.** infeasible
- **4.** unbounded

> [!TIP]
> **Correct answer: 1. degenerate**

## Solution

In a basic feasible solution, the basic variables normally identify a vertex of the feasible polytope. If at least one basic variable has value zero, more constraints meet at that vertex than are needed to identify it, and the basic feasible solution is called degenerate.

## Key Points

- Degenerate BFS: one or more basic variables equal zero.

## Why the other options are incorrect

A non-degenerate BFS has every basic variable strictly positive. Feasibility concerns satisfaction of all constraints, so a zero basic variable does not make the solution infeasible. Unboundedness concerns the objective improving without limit and is unrelated to whether a basic variable is zero.
