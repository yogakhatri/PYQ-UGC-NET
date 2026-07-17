# Question 61

*UGC NET CS · 2016 July Paper 3 · Optimization · Linear Programming - Mathematical Model*

The region of feasible solution of a linear programming problem has a _____ property in geometry, provided the feasible solution of the problem exists.

- **1.** concavity
- **2.** convexity
- **3.** quadratic
- **4.** polyhedron

> [!TIP]
> **Correct answer: 2. convexity**

## Solution

A linear-programming feasible region is the intersection of all half-spaces and hyperplanes defined by its linear constraints. Each such set is convex, and an intersection of convex sets remains convex. Algebraically, if feasible points x and y satisfy Ax ≤ b, then for any 0 ≤ λ ≤ 1, A[λx + (1−λ)y] = λAx + (1−λ)Ay ≤ b. Thus every point on the line segment joining x and y is also feasible. The required geometric property is convexity, option 2.

## Key Points

- Linear inequalities define half-spaces; their intersection is convex.

## Why the other options are incorrect

Concavity normally describes functions, not this feasible set. 'Quadratic' is unrelated to linear constraints. A finite linear feasible region is indeed a convex polyhedron, but the question asks for a geometric property and the options phrase that property as convexity; 'polyhedron' names the shape class rather than the defining property.
