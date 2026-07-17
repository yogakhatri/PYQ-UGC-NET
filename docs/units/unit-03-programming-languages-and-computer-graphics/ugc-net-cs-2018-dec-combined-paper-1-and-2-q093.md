# Question 93

*UGC NET CS · 2018 Dec Paper 1 And 2 · Raster Graphics · Midpoint-Bresenham Line Algorithm*

Consider the midpoint (or Bresenham) algorithm for rasterizing lines: (1) input (x1,y1) and (x2,y2); (2) y=y1; (3) d=f(x1+1,y1+1/2), where f is the implicit form of a line; (4) for x=x1 to x2; (5) do; (6) plot(x,y); (7) if d<0; (8) then; (9) y=y+1; (10) d=d+(y1-y2)+(x2-x1); (11) else; (12) d=d+(y1-y2); (13) end; (14) end. Which statements are true? P: For a line with slope m>1, the outer loop in line (4) should be over y. Q: Lines (10) and (12) update d through incremental evaluation of f. R: The algorithm fails if d is ever 0.

- **1.** P only
- **2.** P and Q only
- **3.** Q and R only
- **4.** P, Q and R

> [!TIP]
> **Correct answer: 2. P and Q only**

## Solution

P is true: when |m|>1, y changes faster than x, so a line rasterizer should step through y and decide when x changes. Q is true: the formulas in lines (10) and (12) add precomputed differences to d instead of reevaluating the implicit line equation at every pixel; that is incremental evaluation. R is false: if d=0, the midpoint lies exactly on the ideal line and a fixed tie rule can select either candidate consistently. Hence P and Q only, option 2.

## Key Points

- Choose the dominant coordinate as the outer loop; update the midpoint decision variable incrementally and handle d=0 with a deterministic tie rule.

## Why the other options are incorrect

Option 1 omits true statement Q. Options 3 and 4 include false statement R. Equality of the decision parameter is a tie case, not algorithmic failure.
