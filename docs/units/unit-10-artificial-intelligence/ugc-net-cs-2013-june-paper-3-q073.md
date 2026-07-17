# Question 73

*UGC NET CS · 2013 June Paper 3 · Fuzzy Sets · Convex Fuzzy Sets*

A fuzzy set A on R is ________ iff A( λx1 + (1 – λ )x2) ≥ min [A( x1), A(x2)] for all x1, x2 ∈ R and all λ ∈ [0, 1], where min denotes the minimum operator.

- **A.** Support
- **B.** α-cut
- **C.** Convex
- **D.** Concave

> [!TIP]
> **Correct answer: C. Convex**

## Solution

A fuzzy set A is convex when the membership at every point between x1 and x2 is at least the smaller endpoint membership: μ_A(λx1+(1−λ)x2)≥min(μ_A(x1),μ_A(x2)) for 0≤λ≤1. Geometrically, membership cannot dip below the lower endpoint level along a line segment. Equivalently, every α-cut of a convex fuzzy set is a convex ordinary set.

## Key Points

- Convex fuzzy set: membership along a segment is never below the minimum membership of its endpoints.

## Why the other options are incorrect

Support is the set of points with positive membership. An α-cut is a crisp level set derived from a fuzzy set. 'Concave' is not the name assigned to this standard minimum-based inequality.
