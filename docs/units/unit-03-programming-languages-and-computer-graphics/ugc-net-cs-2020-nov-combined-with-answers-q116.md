# Question 116

*UGC NET CS · 2020 Nov With Answers · Computer Graphics · Homogeneous 2D Transformation Matrices*

Match the homogeneous 2D transformation matrices with their transformations: (A) [[2,0,0],[0,2,0],[0,0,1]], (B) [[1,0,2],[0,1,2],[0,0,1]], (C) [[0.5,−0.866,0],[0.866,0.5,0],[0,0,1]], (D) [[1,2,0],[0,1,0],[0,0,1]]. List II: (I) x-shear by factor 2, (II) scale by (2,2), (III) rotate by 60°, (IV) translate by (2,2).

- **1.** A-IV, B-II, C-III, D-I
- **2.** A-IV, B-III, C-II, D-I
- **3.** A-III, B-II, C-IV, D-I
- **4.** A-II, B-IV, C-III, D-I

> [!TIP]
> **Correct answer: 4. A-II, B-IV, C-III, D-I**

## Solution

Matrix A multiplies both x and y by 2, so A→II (uniform scale). Matrix B has translation entries 2 in the last column, so B→IV. Matrix C has cos60°=0.5 and sin60°≈0.866 in the standard rotation pattern, so C→III. Matrix D maps x' = x+2y and y'=y, an x-shear of factor 2, so D→I. Therefore A-II, B-IV, C-III, D-I, option 4.

## Key Points

- Read a homogeneous 3×3 matrix by pattern: diagonal scale, last-column translation, sine/cosine rotation, off-diagonal shear.

## Why the other options are incorrect

Translation is recognized by the last column, scaling by diagonal entries, rotation by the sine/cosine block, and shear by an off-diagonal factor. The other options interchange these distinctive patterns.
