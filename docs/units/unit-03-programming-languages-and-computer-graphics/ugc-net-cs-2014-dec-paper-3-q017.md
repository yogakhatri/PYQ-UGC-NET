# Question 17

*UGC NET CS · 2014 Dec Paper 3 · 2-D Geometrical Transforms and Viewing · Cyrus–Beck Line-Clipping Parameter*

In the Cyrus–Beck line-clipping algorithm, which relation computes the parameter t? Here P₁ and P₂ are the line endpoints, fᵢ is a point on boundary i, and nᵢ is its inward normal.

- **A.** ((P₁−fᵢ)·nᵢ) / ((P₂−P₁)·nᵢ)
- **B.** ((fᵢ−P₁)·nᵢ) / ((P₂−P₁)·nᵢ)
- **C.** ((P₂−fᵢ)·nᵢ) / ((P₁−P₂)·nᵢ)
- **D.** ((fᵢ−P₂)·nᵢ) / ((P₁−P₂)·nᵢ)

> [!TIP]
> **Correct answer: B. ((fᵢ−P₁)·nᵢ) / ((P₂−P₁)·nᵢ)**

## Solution

Parameterize the line as P(t)=P₁+t(P₂−P₁). At its intersection with boundary i, the displacement from the boundary point fᵢ is perpendicular to the boundary and hence satisfies (P(t)−fᵢ)·nᵢ=0. Substitution gives (P₁−fᵢ)·nᵢ+t(P₂−P₁)·nᵢ=0. Solving yields t=((fᵢ−P₁)·nᵢ)/((P₂−P₁)·nᵢ), which is option B.

## Key Points

- Cyrus–Beck finds a boundary intersection by inserting P(t) into the boundary's normal equation and solving one linear equation for t.

## Why the other options are incorrect

A has the numerator's sign reversed while retaining the same denominator. C and D reverse the line direction in the denominator; their numerators do not make the corresponding sign change needed to reproduce the derived expression. The formula is undefined when the denominator is zero, which means the line is parallel to that boundary and must be handled separately.
