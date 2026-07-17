# Question 83

*UGC NET CS · 2018 July Paper 2 · Optimization · Unbounded Linear Programs*

Consider the LPP: maximize z=100x1+2x2+5x3, subject to 14x1+x2−6x3+3x4=7, 32x1+x2−12x3≤10, 3x1−x2−x3≤0, and x1,x2,x3,x4≥0. It has:

- **1.** Solution : x1= 100, x2= 0, x3= 0
- **2.** Unbounded solution
- **3.** No solution
- **4.** Solution : x 1= 50, x2= 70, x3= 60

> [!TIP]
> **Correct answer: 2. Unbounded solution**

## Solution

First show feasibility: x=(0,7,0,0) satisfies the equality and both inequalities. Now use the nonnegative direction d=(0,6,1,0). It preserves the equality because 6−6=0; its changes in the two inequality left sides are 6−12=−6≤0 and −6−1=−7≤0. Therefore x+td is feasible for every t≥0. The objective grows by 2·6+5·1=17 per unit t, so it tends to infinity. The LPP is unbounded, option 2.

## Key Points

- To prove an LP unbounded, find one feasible point and a feasible ray whose objective improvement is positive.

## Why the other options are incorrect

Option 3 is disproved by the explicit feasible point. Options 1 and 4 present finite vectors, but an improving feasible ray means no finite maximizer can be optimal. Also, option 1 violates the equality if interpreted with x4=0.
