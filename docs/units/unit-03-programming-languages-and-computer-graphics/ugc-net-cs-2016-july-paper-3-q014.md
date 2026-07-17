# Question 14

*UGC NET CS · 2016 July Paper 3 · 2-D Geometrical Transforms and Viewing · Rotation about an Arbitrary Pivot*

A point P(5, 1) is rotated by 90° about a pivot point (2, 2). What is the coordinate of new transformed point P′ ?

- **1.** (3, 5)
- **2.** (5, 3)
- **3.** (2, 4)
- **4.** (1, 5)

> [!TIP]
> **Correct answer: 1. (3, 5)**

## Solution

Translate P relative to the pivot: (5−2,1−2)=(3,−1). A positive 90° rotation is counter-clockwise and maps (x,y) to (−y,x), giving (1,3). Translate back by (2,2): (1+2,3+2)=(3,5). Thus option 1 is correct.

## Key Points

- Rotate about pivot C by P′=C+R(P−C); for +90°, R(x,y)=(−y,x).

## Why the other options are incorrect

The other coordinates result from rotating about the origin, using an incorrect sign, or failing to translate back. Rotation about a pivot must use T(pivot)·R(90°)·T(−pivot), not R alone.
