# Question 60

*UGC NET CS · 2016 July Paper 3 · Computer Graphics and Image Processing · Boundary Representation and Chain Codes*

Which of the following is used for the boundary representation of an image object ?

- **1.** Quad Tree
- **2.** Projections
- **3.** Run length coding
- **4.** Chain codes

> [!TIP]
> **Correct answer: 4. Chain codes**

## Solution

A chain code represents an object's boundary by choosing a starting boundary pixel and recording the direction of each step to the next boundary pixel. Four-connected chain codes use four possible directions and eight-connected codes use eight. Because the representation follows the contour itself, option 4 is correct.

## Key Points

- Boundary representation asks 'how does the contour move?'; a chain code answers with a sequence of direction numbers.

## Why the other options are incorrect

A quadtree recursively partitions an image region into quadrants, so it is primarily a region or spatial-decomposition representation. Projections summarize values along directions, and run-length coding stores lengths of consecutive equal pixels. Neither directly records the ordered boundary path.
