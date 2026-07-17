# Question 36

*UGC NET CS · 2016 July Paper 3 · Computational Geometry · Triangulation of a Convex Polygon*

A triangulation of a polygon is a set of T chords that divide the polygon into disjoint triangles. Every triangulation of n-vertex convex polygon has _____ chords and divides the polygon into _____ triangles.

- **1.** n – 2, n – 1
- **2.** n – 3, n – 2
- **3.** n – 1, n
- **4.** n – 2, n – 2

> [!TIP]
> **Correct answer: 2. n – 3, n – 2**

## Solution

A convex n-gon can be triangulated by drawing n−3 noncrossing diagonals (called chords here). The result contains n−2 triangles. This follows by induction: adding one vertex to a triangulated polygon adds one diagonal and one triangle. Therefore the pair is (n−3,n−2), option 2.

## Key Points

- Every triangulation of a convex n-gon has n−3 internal diagonals and n−2 triangles.

## Why the other options are incorrect

The other pairs are off by one or count boundary edges as chords. For a triangle n=3, the correct formulas give zero added chords and one triangle, an immediate consistency check.
