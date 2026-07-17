# Question 15

*UGC NET CS · 2016 July Paper 3 · 2-D Geometrical Transforms and Viewing · Cohen-Sutherland Trivial Acceptance and Rejection*

Let R be the rectangular window against which the lines are to be clipped using 2D Sutherland-Cohen line clipping algorithm. The rectangular window has lower left-hand corner at (– 5, 1) and upper right-hand corner at (3, 7). Consider the following three lines for clipping with the given end point co-ordinates : Line AB : A (– 6, 2) and B (–1, 8) Line CD : C (– 1, 5) and D (4, 8) Line EF : E (–2, 3) and F (1, 2) Which of the following line(s) is/are candidate for clipping ?

- **1.** AB
- **2.** CD
- **3.** EF
- **4.** AB and CD

> [!TIP]
> **Correct answer: 4. AB and CD**

## Solution

The window is x∈[−5,3], y∈[1,7]. For AB, A is LEFT and B is TOP; their outcode AND is zero, so the segment is a clipping candidate. For CD, C is inside and D is TOP+RIGHT, again giving AND zero and requiring clipping. Both endpoints of EF are inside, so EF is trivially accepted without clipping. Therefore AB and CD, option 4.

## Key Points

- Cohen-Sutherland: OR=0 trivially accept; AND≠0 trivially reject; otherwise clip against a boundary.

## Why the other options are incorrect

Selecting only AB or only CD misses the other segment that crosses a boundary. EF is not rejected, but it is not a clipping candidate because both outcodes are 0000 and no endpoint needs adjustment.
