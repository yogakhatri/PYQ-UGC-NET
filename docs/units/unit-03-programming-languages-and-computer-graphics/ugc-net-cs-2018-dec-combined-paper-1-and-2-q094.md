# Question 94

*UGC NET CS · 2018 Dec Paper 1 And 2 · 3-D Object Representation, Geometric Transformations and Viewing · Perspective and Parallel Projections*

In 3D Graphics, which of the following statements about perspective and parallel projection is/are true? P: In a perspective projection, the farthest an object is from the centre of projection, the smaller it appears. Q: Parallel projection is equivalent to a perspective projection where the viewer is standing infinitely far away. R: Perspective projections do not preserve straight lines. Choose the correct answer from the code given below :

- **1.** P and Q only
- **2.** P and R only
- **3.** Q and R only
- **4.** P, Q and R

> [!TIP]
> **Correct answer: 1. P and Q only**

## Solution

P is true because perspective projection scales image size inversely with depth: farther objects appear smaller. Q is true because moving the centre of projection infinitely far away makes all projectors parallel, yielding parallel projection as a limiting case. R is false: projective transformations preserve straight lines as straight lines (although lengths, angles, and parallelism may not be preserved). Therefore P and Q only, option 1.

## Key Points

- Perspective changes apparent scale with depth and may destroy parallelism, yet projective geometry preserves collinearity.

## Why the other options are incorrect

Options 2–4 include R or omit one of P and Q. Perspective makes parallel lines appear to converge, but it does not bend an individual straight line into a curve.
