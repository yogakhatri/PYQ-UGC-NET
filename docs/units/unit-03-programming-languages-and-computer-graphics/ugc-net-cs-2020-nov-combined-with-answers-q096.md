# Question 96

*UGC NET CS · 2020 Nov With Answers · Computer Graphics · Perspective Projection*

In the context of 3D computer graphics, which statements are correct? (A) Under perspective projection, parallel lines in the object do not remain parallel in the image, except those parallel to the view plane. (B) Applying perspective projection to a vertex involves division by its z-coordinate (equivalently, perspective division in homogeneous coordinates). (C) Perspective transformation is a linear transformation in Cartesian coordinates.

- **1.** (A) and (B) only
- **2.** (A) and (C) only
- **3.** (B) and (C) only
- **4.** (A), (B) and (C)

> [!TIP]
> **Correct answer: 1. (A) and (B) only**

## Solution

Perspective projection maps a 3D point approximately as x'=d·x/z and y'=d·y/z. Lines parallel to the view plane share the relevant depth behaviour and remain parallel, while other parallel lines generally converge toward a vanishing point; thus A is true. The formulas explicitly require division by depth (or, in a homogeneous pipeline, division by w after the projection matrix), so B is true. Because division by a coordinate does not preserve addition or scalar multiplication in ordinary Cartesian coordinates, the complete perspective mapping is not linear there; C is false. Hence option 1.

## Key Points

- Perspective projection uses depth division: it creates vanishing points and makes the final Cartesian transformation nonlinear.

## Why the other options are incorrect

Every alternative containing C confuses the homogeneous matrix step with the full Cartesian mapping. A projection matrix acts linearly on homogeneous vectors, but the subsequent perspective divide makes the Euclidean transformation nonlinear.
