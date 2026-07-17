# Question 14

*UGC NET CS · 2017 Jan Paper 3 · Computer Graphics · GKS Segments and Segment Transformations*

A segment is any object described by GKS commands and data that start with CREATE SEGMENT and Terminates with CLOSE SEGMENT command. What functions can be performed on these segments ?

- **1.** Translation and Rotation
- **2.** Panning and Zooming
- **3.** Scaling and Shearing
- **4.** Translation, Rotation, Panning and Zooming

> [!TIP]
> **Correct answer: 4. Translation, Rotation, Panning and Zooming**

## Solution

A GKS segment groups primitives so they can be transformed as one object. A segment transformation changes position by translation, orientation by rotation, and size by scaling. In viewing terms, translation supports panning and scaling supports zooming. Thus the most complete listed description is translation, rotation, panning and zooming, option 4.

## Key Points

- GKS segment transformation changes a stored object's position, orientation, and size—translation/pan, rotation, and scaling/zoom.

## Why the other options are incorrect

Options 1 and 2 name only subsets of the supported effects. Option 3 includes scaling but pairs it with shearing; the standard GKS segment transformation is defined in terms of translation, scaling, and rotation rather than arbitrary shear. Option 4 covers those standard effects using both geometric and viewing terminology.

## References

- [NIST FIPS 120-1 — Graphical Kernel System functional description](https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub120-1.pdf)
