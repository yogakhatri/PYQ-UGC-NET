# Question 29

*UGC NET CS · 2013 June Paper 3 · 2-D Geometrical Transforms and Viewing · Homogeneous Points at Infinity*

In homogenous coordinate system (x, y, z) the points with z = 0 are called

- **A.** Cartesian points
- **B.** Parallel points
- **C.** Origin point
- **D.** Point at infinity

> [!TIP]
> **Correct answer: D. Point at infinity**

## Solution

A finite 2-D Cartesian point (X,Y) is represented homogeneously as (x,y,z) with X=x/z and Y=y/z for z≠0. When z=0, those divisions do not produce finite Cartesian coordinates; the homogeneous triple represents a direction, or a point at infinity, in the projective plane.

## Key Points

- Homogeneous last coordinate nonzero=finite point; zero=point/direction at infinity.

## Why the other options are incorrect

Cartesian points require a nonzero scale coordinate, commonly normalized to z=1. 'Parallel point' is not the standard projective term. The origin is represented by (0,0,z) with z≠0, such as (0,0,1), not by every point with z=0.
