# Question 9

*UGC NET CS · 2021 Nov With Answers · 3-D Object Representation, Geometric Transformations and Viewing · Cubic Bézier Evaluation and Convex-Hull Property*

Suppose a Bezier curve P(t) is defined by the four control points P0=(-2,0), P1=(-2,4), P2=(2,4), and P3=(2,0). Which statements are correct? A. Bezier curve P(t) has degree 3. B. P(1/2)=(0,3). C. Bezier curve P(t) may extend outside the convex hull of its control points.

- **1.** A and B only
- **2.** A and C only
- **3.** B and C only
- **4.** A, B, and C

> [!TIP]
> **Correct answer: 1. A and B only**

## Solution

Four control points define a cubic Bézier curve, so A is true. At t=1/2 the Bernstein weights are 1/8, 3/8, 3/8, and 1/8. Hence P(1/2)=[P0+3P1+3P2+P3]/8=(0,24/8)=(0,3), making B true. Bézier weights are nonnegative and sum to one for 0≤t≤1, so every curve point is a convex combination of the control points and cannot leave their convex hull. C is false. Therefore A and B only, option 1.

## Key Points

- A Bézier curve with n+1 control points has degree n and stays inside their convex hull.

## Why the other options are incorrect

Options 2–4 accept the false claim C or omit the verified midpoint. The convex-hull property is one of the main geometric guarantees of Bézier curves.
