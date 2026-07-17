# Question 64

*UGC NET CS · 2014 Dec Paper 3 · Image Processing · Discrete Laplacian Spatial Masks*

Given S₁=[[0,1,0],[1,−4,0],[0,1,0]] and S₂=[[1,1,1],[1,−8,1],[1,1,1]], which mask can implement the image Laplacian by convolution?

- **A.** Only S₁
- **B.** Only S₂
- **C.** Both S₁ and S₂
- **D.** None of these

> [!TIP]
> **Correct answer: B. Only S₂**

## Solution

A discrete Laplacian mask must annihilate a constant image, so its coefficients must sum to zero. S₂ has eight neighbor coefficients of +1 and center −8, giving sum 0; it is the standard 8-neighbor Laplacian. In the printed S₁, the coefficient to the right of the center is 0 rather than 1, so the sum is −1 and the four-neighbor stencil is incomplete. Only S₂ is valid as printed.

## Key Points

- Quick mask check: a derivative operator must give zero on a constant image, so its coefficients must sum to zero.

## Why the other options are incorrect

A and C treat S₁ as the familiar four-neighbor mask, but the actual printed matrix is missing one +1. The correct four-neighbor mask would be [[0,1,0],[1,−4,1],[0,1,0]]. Because S₂ is valid, none of these is false.
