# Question 8

*UGC NET CS · 2021 Nov With Answers · Computer Graphics · Deriving a 2-D Shear Matrix from Vertex Mappings*

What is the transformation matrix M that transforms the square in the xy-plane defined by (1,1)^T, (-1,1)^T, (-1,-1)^T and (1,-1)^T to a parallelogram whose corresponding vertices are (2,1)^T, (0,1)^T, (-2,-1)^T and (0,-1)^T?

- **1.** M = [[1,1,0],[0,1,0],[0,0,1]]
- **2.** M = [[1,0,0],[1,1,0],[0,0,1]]
- **3.** M = [[1,1,1],[0,1,0],[0,0,1]]
- **4.** M = [[1,1,0],[1,1,0],[0,0,1]]

> [!TIP]
> **Correct answer: 1. M = [[1,1,0],[0,1,0],[0,0,1]]**

## Solution

Compare each source and target: y is unchanged, while x increases by y. Thus x'=x+y and y'=y, an x-direction shear of factor 1. In homogeneous coordinates this is [[1,1,0],[0,1,0],[0,0,1]]. Checking (1,1) gives (2,1), and the same matrix maps the other three vertices to the stated targets. Therefore option 1.

## Key Points

- Derive coordinate equations from corresponding points first; then read their coefficients into the homogeneous transformation matrix.

## Why the other options are incorrect

Option 2 performs the opposite shear, y'=x+y. Option 3 adds a translation of 1 in x, which would move every target. Option 4 is singular and maps both output coordinates to x+y.
