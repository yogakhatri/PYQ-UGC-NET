# Question 32

*UGC NET CS · 2015 Dec Paper 3 · Computer Graphics · Straight-Line Equation and Point Generation*

The end points of a given line are (0, 0) and (6, 18). Compute each value of y as x steps from 0 to 3, by using equation of straight line :

- **1.** x=0,y=0; x=1,y=3; x=2,y=6; x=3,y=9
- **2.** x=0,y=1; x=1,y=3; x=2,y=4; x=3,y=9
- **3.** x=0,y=2; x=1,y=3; x=2,y=6; x=3,y=9
- **4.** x=0,y=0; x=1,y=3; x=2,y=4; x=3,y=6

> [!TIP]
> **Correct answer: 1. x=0,y=0; x=1,y=3; x=2,y=6; x=3,y=9**

## Solution

The slope through (0,0) and (6,18) is m=(18−0)/(6−0)=3. Using point-slope form through the origin gives y=3x. Substituting x=0,1,2,3 yields y=0,3,6,9, respectively.

## Key Points

- Find m=Δy/Δx, form y=mx+c, then evaluate the requested x values.

## Why the other options are incorrect

Options 2 and 3 violate the endpoint-derived line at x=0, while option 4 stops following slope 3 after x=1. A straight line must use the same slope at every step.
