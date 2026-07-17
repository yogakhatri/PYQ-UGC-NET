# Question 59

*UGC NET CS · 2018 Dec Paper 1 And 2 · Optimization · Linear Programming with Negative Objective Coefficients*

Use the dual simplex method to maximize z=-2x1-3x2 subject to x1+x2>=2, 2x1+x2<=10, x1+x2<=8, and x1,x2>=0.

- **1.** x1=2, x2=0, z=-4
- **2.** x1=2, x2=6, z=-22
- **3.** x1=0, x2=2, z=-6
- **4.** x1=6, x2=2, z=-18

> [!TIP]
> **Correct answer: 1. x1=2, x2=0, z=-4**

## Solution

Maximizing z=−2x₁−3x₂ is the same as minimizing 2x₁+3x₂. The constraint x₁+x₂≥2 requires at least two units in total; because x₁ costs 2 per unit and x₂ costs 3, the least-cost candidate is (2,0). It also satisfies the remaining printed constraints and non-negativity. Its objective is z=−2(2)−3(0)=−4, so option 1 is optimal.

## Key Points

- When maximizing a negative linear objective, equivalently minimize its positive counterpart over the feasible region.

## Why the other options are incorrect

Any feasible substitution of x₂ for x₁ increases the positive cost 2x₁+3x₂ and makes z more negative. Points failing x₁+x₂≥2 are infeasible; feasible points with additional nonnegative variables cannot improve beyond −4 under the given inequalities.
