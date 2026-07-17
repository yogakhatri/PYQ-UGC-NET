# Question 82

*UGC NET CS · 2018 July Paper 2 · Optimization · Properties of Convex Minimization*

Which statement is false about a convex minimization problem?

- **1.** If a local minimum exists, then it is a global minimum
- **2.** The set of all global minima is convex set
- **3.** The set of all global minima is concave set
- **4.** For each strictly convex function, if the function has a minimum, then the minimum is unique

> [!TIP]
> **Correct answer: 3. The set of all global minima is concave set**

## Solution

For convex minimization, every local minimum is global. If x and y are global minimizers, convexity makes every point on the segment between them a minimizer, so the minimizer set is convex. A strictly convex function can have at most one minimizer. Thus statements 1, 2, and 4 are true. `The set of all global minima is a concave set` is not the applicable property and is the false statement, option 3.

## Key Points

- Convex objective: local=global and the argmin set is convex; strictly convex objective: at most one minimizer.

## Why the other options are incorrect

The term `concave set` is not the standard counterpart here; convexity is a property of the feasible/minimizer set, while concavity usually describes a function. Strict convexity rules out two distinct minimizers because their midpoint would have a strictly smaller value.
