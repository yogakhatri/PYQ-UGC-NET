# Question 79

*UGC NET CS · 2019 June Paper 1 And 2 · 3-D Object Representation, Geometric Transformations and Viewing · Orthographic projection*

In the context of 3D computer graphics, which statements are true? P: Orthographic transformations keep parallel lines parallel. Q: Orthographic transformations are affine transformations.

- **1.** Both P and Q
- **2.** Neither P nor Q
- **3.** Only P
- **4.** Only Q

> [!TIP]
> **Correct answer: 1. Both P and Q**

## Solution

An orthographic projection maps points along parallel projectors onto a view plane. It preserves parallelism: parallel model-space lines remain parallel in the image unless they collapse to the same line. The mapping consists of linear transformation plus translation, so it is affine. Both statements are therefore true.

## Key Points

- Orthographic projection is affine and preserves parallel lines; perspective projection generally does not.

## Why the other options are incorrect

Options 2–4 reject at least one standard property of orthographic projection. Perspective projection, not orthographic projection, is the case in which parallel lines may converge to vanishing points.
