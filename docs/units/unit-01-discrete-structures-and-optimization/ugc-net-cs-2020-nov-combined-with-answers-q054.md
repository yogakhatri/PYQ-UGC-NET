# Question 54

*UGC NET CS · 2020 Nov With Answers · Linear Programming · Graphical Optimization*

Consider the linear program: maximize z=2x1+3x2, subject to 2x1+x2≤4, x1+2x2≤5, and x1,x2≥0. What is its optimum value?

- **1.** 23
- **2.** 9.5
- **3.** 13
- **4.** 8

> [!TIP]
> **Correct answer: 4. 8**

## Solution

A linear objective reaches its optimum at a feasible corner. The axis corners are (0,0), (2,0), and (0,2.5). The two constraint lines intersect where 2x1+x2=4 and x1+2x2=5. Solving gives x1=1 and x2=2. Evaluate z=2x1+3x2: the four values are 0, 4, 7.5, and 2+6=8. The maximum is 8 at (1,2), hence option 4.

## Key Points

- For a two-variable LP, enumerate feasible vertices and evaluate the objective at each.

## Why the other options are incorrect

Values 23 and 13 do not result from any feasible corner. The value 9.5 would exceed the objective at every vertex and is therefore impossible. Checking the intersection alone is not enough in general, but here its value also exceeds both axis corners.
