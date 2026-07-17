# Question 10

*UGC NET CS · 2018 July Paper 2 · 2-D Geometrical Transforms and Viewing · Composition of Scaling and Translation Matrices*

Consider the homogeneous 2D transformation matrix M=[[2,0,2],[0,1,1],[0,0,1]]. Which statement about M is true? Assume column-vector coordinates.

- **1.** M represents first, a scaling of vector (2, 1) followed by translatio n of vector (1, 1)
- **2.** M represents first, a translation of vector (1, 1) followed by scalin g of vector (2, 1)
- **3.** M represents first, a scaling of vector (3, 1) followed by shearing of p arameters (−1, 1)
- **4.** M represents first, a shearing of parameters ( −1, 1) followed by scaling of vector (3, 1)

> [!TIP]
> **Correct answer: 2. M represents first, a translation of vector (1, 1) followed by scalin g of vector (2, 1)**

## Solution

Using column vectors, translation by (1,1) is T=[[1,0,1],[0,1,1],[0,0,1]] and scaling by (2,1) is S=[[2,0,0],[0,1,0],[0,0,1]]. If translation happens first and scaling second, the combined matrix is S·T=[[2,0,2],[0,1,1],[0,0,1]], exactly M. Therefore option 2 is correct.

## Key Points

- For column vectors, the rightmost transform acts first: applying T then S gives the product S·T.

## Why the other options are incorrect

Scaling first and translating second would give T·S=[[2,0,1],[0,1,1],[0,0,1]], so option 1 has the wrong order. Options 3 and 4 describe shear compositions whose off-diagonal linear terms do not match M.
