# Question 30

*UGC NET CS · 2021 Nov With Answers · Linear Programming · Corner-Point Optimization*

Maximize Z=6x+5y subject to 2x-3y≤5, x+3y≤11, 4x+y≤15, x≥0, and y≥0. What is the optimal objective value?

- **1.** 15
- **2.** 25
- **3.** 31.72
- **4.** 41.44

> [!TIP]
> **Correct answer: 3. 31.72**

## Solution

A linear objective reaches its optimum at a feasible corner. The important corners include (0,0), (5/2,0), (0,11/3), the intersection of 2x−3y=5 with 4x+y=15, namely (25/7,5/7), and the intersection of x+3y=11 with 4x+y=15. Solving the last pair gives x=34/11 and y=29/11; it also satisfies 2x−3y≤5. There Z=6(34/11)+5(29/11)=349/11≈31.72, larger than the objective at every other feasible corner. Thus option 3.

## Key Points

- Enumerate feasible boundary intersections, evaluate Z at each, and select the largest value.

## Why the other options are incorrect

15 is the value at (5/2,0), and 25 occurs at (25/7,5/7). The value 41.44 is not attained by a feasible corner. Intersections must be checked against all constraints before comparing their objectives.
