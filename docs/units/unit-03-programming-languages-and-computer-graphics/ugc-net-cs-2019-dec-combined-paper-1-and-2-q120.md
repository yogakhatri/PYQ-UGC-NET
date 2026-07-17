# Question 120

*UGC NET CS · 2019 Dec Paper 1 And 2 · Computer Graphics · Scan-Line and Seed-Fill Algorithms*

Consider the following statements with respect to approaches to fill area on raster systems : P: To determine the overlap intervals for scan lines that cross the area. Q: To start from a given interior position and paint outward from this point until we encounter the specified boundary conditions. Select the correct answer from the options given below :

- **1.** P only
- **2.** Q only
- **3.** Both P and Q
- **4.** Neither P nor Q

> [!TIP]
> **Correct answer: 3. Both P and Q**

## Solution

P describes the scan-line polygon-fill approach: intersect a horizontal scan line with the boundary, pair the intersections, and fill each interior interval. Q describes a seed-fill approach such as boundary fill or flood fill: begin at an interior pixel and expand through neighbours until the boundary or a non-target colour stops the process. Both are valid raster area-filling approaches, so option 3.

## Key Points

- Raster filling has two classic views: fill inside scan-line intersection pairs, or grow a region outward from a seed.

## Why the other options are incorrect

Options 1 and 2 each recognize only one of the two standard families. Option 4 rejects both despite P describing interval filling and Q describing connected-region filling. They use different starting information but solve the same area-fill task.
