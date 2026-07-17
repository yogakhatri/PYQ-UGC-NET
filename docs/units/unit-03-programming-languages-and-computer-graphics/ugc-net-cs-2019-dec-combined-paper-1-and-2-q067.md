# Question 67

*UGC NET CS · 2019 Dec Paper 1 And 2 · 2-D Geometrical Transforms and Viewing · Line and Polygon Clipping*

A rectangular clipping window is bounded by x=0, y=0, x=5 and y=3. If the line segment joining (-1,0) and (4,5) is clipped against this window, which two endpoints remain?

- **1.** (0,1) and (3,3)
- **2.** (0,1) and (2,3)
- **3.** (0,1) and (4,5)
- **4.** (0,1) and (3,5)

> [!TIP]
> **Correct answer: 2. (0,1) and (2,3)**

## Solution

The segment from (−1,0) to (4,5) has slope (5−0)/(4−(−1))=1, so its line equation is y=x+1. At the window's left boundary x=0, it enters at (0,1). Moving upward, it reaches the top boundary y=3 at x=2. Both coordinates then lie within the other window limits, so the visible segment is from (0,1) to (2,3), option 2.

## Key Points

- Find intersections of the segment's line equation with the first entering and exiting window boundaries.

## Why the other options are incorrect

(3,3) is not on y=x+1, while (4,5) lies above the window and is the original outside endpoint. (3,5) is both off the line and outside the y≤3 boundary. Clipping replaces outside endpoints with boundary intersections.
