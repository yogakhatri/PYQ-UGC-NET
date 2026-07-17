# Question 17

*UGC NET CS · 2016 July Paper 3 · 2-D Geometrical Transforms and Viewing · Y-Direction Shear about a Reference Line*

Let us consider that the original point is (x, y) and new transformed point is (x′, y′). Further, Shx and Shy are shearing factors in x and y directions. If we perform the y-direction shear relative to x = xref then the transformed point is given by _______.

- **1.** x′=x+Shₓ(y−yref); y′=y
- **2.** x′=x; y′=y·Shₓ
- **3.** x′=x; y′=Shᵧ(x−xref)+y
- **4.** x′=Shᵧ·y; y′=y(x−xref)

> [!TIP]
> **Correct answer: 3. x′=x; y′=Shᵧ(x−xref)+y**

## Solution

A y-direction shear leaves x unchanged and changes y in proportion to horizontal distance. To keep the reference line x=xref fixed, use that distance x−xref: x′=x and y′=y+Shᵧ(x−xref). Therefore option 3 is correct.

## Key Points

- Y-shear about x=xref: x′=x, y′=y+Shᵧ(x−xref); points on the reference line remain unchanged.

## Why the other options are incorrect

Option 1 is an x-direction shear relative to a horizontal reference line. Option 2 scales y rather than shearing it. Option 4 changes x and multiplies coordinates incorrectly; it does not leave points on x=xref fixed.
