# Question 132

*UGC NET CS · 2020 Nov With Answers · 3-D Object Representation, Geometric Transformations and Viewing · Bézier Curves and Control Points*

Statement I: Bézier curves interpolate all of their control points. Statement II: A cubic Bézier curve has four control points. Choose the correct evaluation.

- **1.** Both Statement I and Statement II are true
- **2.** Both Statement I and Statement Il are false
- **3.** Statement I is correct but Statement Il is false
- **4.** Statement I is incorrect but Statement Il is true.

> [!TIP]
> **Correct answer: 4. Statement I is incorrect but Statement Il is true.**

## Solution

A Bézier curve is controlled by its control polygon but generally does not pass through every interior control point; it interpolates the first and last control points. Thus Statement I is false. A Bézier curve of degree n has n+1 control points, so a cubic (degree-3) curve has four control points. Statement II is true, and option 4 follows.

## Key Points

- Degree n means n+1 control points; an ordinary Bézier curve passes through its endpoints, not all control points.

## Why the other options are incorrect

Options 1 and 3 confuse approximation with interpolation. Option 2 also rejects the degree-plus-one rule that gives four control points for a cubic curve.
