# Question 16

*UGC NET CS · 2014 Dec Paper 3 · 2-D Geometrical Transforms and Viewing · Rotation about an Arbitrary Pivot*

Consider a triangle represented by A(0, 0), B(1, 1), C(5, 2). The triangle is rotated counterclockwise by 45° about P(−1, −1). The coordinates of the new triangle obtained after rotation are:

- **A.** A′ = (−1, √2−1), B′ = (−1, 2√2−1), C′ = (3√2/2−1, 9√2/2−1)
- **B.** A′ = (√2−1, −1), B′ = (2√2−1, −1), C′ = (3√2/2−1, 9√2/2−1)
- **C.** A′ = (−1, √2−1), B′ = (2√2−1, −1), C′ = (3√2/2−1, 9√2/2−1)
- **D.** A′ = (−1, √2−1), B′ = (2√2−1, −1), C′ = (9√2/2−1, 3√2/2−1)

> [!TIP]
> **Correct answer: A. A′ = (−1, √2−1), B′ = (−1, 2√2−1), C′ = (3√2/2−1, 9√2/2−1)**

## Solution

A rotation about P(−1,−1) is done in three steps: translate P to the origin, rotate, and translate back. For 45°, (x,y) becomes ((x−y)/√2,(x+y)/√2). After translating by (+1,+1), A becomes (1,1), which rotates to (0,√2) and translates back to A′=(−1,√2−1). Similarly, B: (2,2)→(0,2√2)→(−1,2√2−1). For C, (6,3)→(3/√2,9/√2)→(3√2/2−1,9√2/2−1). These are exactly option A.

## Key Points

- To rotate about an arbitrary pivot P, use T(P)·R(θ)·T(−P), or equivalently translate to the origin, rotate, and translate back.

## Why the other options are incorrect

B incorrectly swaps the coordinates of A′ and B′. C has the right A′ but the wrong B′. D also exchanges the two components of C′. Each error can be caught by noting that A and B lie on the line y=x through the translated origin, so a +45° rotation must put both on the positive y-axis before translating back.
