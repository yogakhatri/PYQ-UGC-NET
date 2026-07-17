# Question 13

*UGC NET CS · 2016 July Paper 3 · Computer Graphics · Bresenham Circle Generation*

In Bresenham's circle algorithm, the current first-octant point is (xᵢ,yᵢ) with decision parameter pᵢ. For pᵢ≥0, which update gives (xᵢ₊₁,yᵢ₊₁) and pᵢ₊₁?

- **1.** xᵢ₊₁=xᵢ+1; yᵢ₊₁=yᵢ; pᵢ₊₁=pᵢ+4xᵢ+6
- **2.** xᵢ₊₁=xᵢ+1; yᵢ₊₁=yᵢ−1; pᵢ₊₁=pᵢ+4(xᵢ−yᵢ)+10
- **3.** xᵢ₊₁=xᵢ; yᵢ₊₁=yᵢ−1; pᵢ₊₁=pᵢ+4(xᵢ−yᵢ)+6
- **4.** xᵢ₊₁=xᵢ−1; yᵢ₊₁=yᵢ; pᵢ₊₁=pᵢ+4xᵢ+10

> [!TIP]
> **Correct answer: 2. xᵢ₊₁=xᵢ+1; yᵢ₊₁=yᵢ−1; pᵢ₊₁=pᵢ+4(xᵢ−yᵢ)+10**

## Solution

In the first octant, each step increments x. When pᵢ≥0, the midpoint test selects the south-east pixel, so y also decreases by 1: xᵢ₊₁=xᵢ+1 and yᵢ₊₁=yᵢ−1. The corresponding recurrence is pᵢ₊₁=pᵢ+4(xᵢ−yᵢ)+10. Therefore option 2 is correct.

## Key Points

- Bresenham circle: p<0 chooses E; p≥0 chooses SE with update p←p+4(x−y)+10.

## Why the other options are incorrect

Option 1 is the east-pixel update used when pᵢ<0. Options 3 and 4 do not follow the algorithm's first-octant rule that x advances by one at every step, and their decision updates do not match the selected move.
