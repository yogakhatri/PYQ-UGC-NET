# Question 62

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · 3-D Object Representation, Geometric Transformations and Viewing · Bezier and B-Spline Curves and Surfaces*

In _curve the last and the first vertices of the polygon lie on the curve and all other vertices define the derivatives, order and shape of the curve.

- **1.** B-Spline Curve
- **2.** Boxline curve
- **3.** Bezier curve
- **4.** Gaussian curve

> [!TIP]
> **Correct answer: 3. Bezier curve**

## Solution

A Bézier curve interpolates its first and last control points. Intermediate control points generally do not lie on the curve; they determine endpoint derivatives and overall order/shape.

## Key Points

- Bézier endpoints lie on the curve; inner control points pull its shape.

## Why the other options are incorrect

Ordinary B-splines generally do not interpolate both endpoint control vertices without special knot choices; the other names do not describe this control-polygon property.
