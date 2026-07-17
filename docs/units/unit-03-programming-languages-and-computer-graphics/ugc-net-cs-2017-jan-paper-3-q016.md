# Question 16

*UGC NET CS · 2017 Jan Paper 3 · Computer Graphics · Bresenham Circle Scan Conversion*

Below are the few steps given for scan-converting a circle using Bresenham’s Algorithm. Which of the given steps is not correct ?

- **1.** Compute d = 3 – 2r (where r is radius)
- **2.** Stop if x > y
- **3.** If d < 0, then d = 4x + 6 and x = x + 1
- **4.** If d ≥ 0, then d = 4 ∗ (x – y) + 10, x = x + 1 and y = y + 1

> [!TIP]
> **Correct answer: 4. If d ≥ 0, then d = 4 ∗ (x – y) + 10, x = x + 1 and y = y + 1**

## Solution

Bresenham's circle algorithm begins at (0,r) with decision variable d=3−2r and generates one octant while x≤y. On every iteration x increases. When d≥0, the chosen pixel moves diagonally inward, so y must decrease: y=y−1, not y=y+1. The corresponding accumulated update is d←d+4(x−y)+10. Therefore step 4 contains the decisive wrong direction for y and is the incorrect step.

## Key Points

- While tracing the first octant of a circle from (0,r), x rises and y can only stay fixed or fall; it never rises.

## Why the other options are incorrect

The initialization d=3−2r is standard, and stopping after x>y avoids repeating the symmetric octants. For d<0 the next point moves horizontally with x increasing and the decision value updated by 4x+6 (added to the old d). Option 4 instead moves y outward.
