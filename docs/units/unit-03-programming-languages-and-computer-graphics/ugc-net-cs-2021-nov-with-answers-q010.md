# Question 10

*UGC NET CS · 2021 Nov With Answers · Computer Graphics · Polygon Clipping and Perspective Nonlinearity*

Given below are two statements Statement I: The maximum number of sides that a triangle might have when clipped to a rectangular viewport is 6. Statement II: In 3D graphics, the perspective transformation is nonlinear in z. In light of the above statements, choose the correct answer from the options given below

- **1.** Both Statement I and Statement II are true.
- **2.** Both Statement I and Statement II are false
- **3.** Statement I is true but Statement II is false
- **4.** Statement I is false but Statement II is true

> [!TIP]
> **Correct answer: 4. Statement I is false but Statement II is true**

## Solution

Clipping a convex m-gon against a convex n-gon can produce an intersection with as many as m+n sides. A triangle and rectangle can attain 3+4=7 sides—for example, when one triangle vertex lies inside the viewport and the other edges cut the rectangle so that all four rectangle edges contribute. Therefore the claimed maximum of 6 is false. Perspective projection uses coordinates such as x'=d·x/z and y'=d·y/z after the homogeneous divide, so it is nonlinear in z; Statement II is true. The answer is option 4.

## Key Points

- Triangle∩rectangle can be a heptagon; perspective normalization introduces 1/z and is nonlinear in Euclidean depth.

## Why the other options are incorrect

Options 1 and 3 accept the incorrect six-side limit, while option 2 denies the reciprocal-depth dependence of perspective projection. A perspective matrix is linear in homogeneous coordinates, but conversion back to normalized Euclidean coordinates includes division by depth.
