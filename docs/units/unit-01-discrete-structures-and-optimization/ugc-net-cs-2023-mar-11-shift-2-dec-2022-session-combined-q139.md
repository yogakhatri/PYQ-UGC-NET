# Question 139

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Optimization · Linear-programming relaxation for vertex cover*

OBID:187089 Statement 1: Given a graph G=(V,E) in which each vertex v € V has an associated positive weight w(v), we can use linear programming to find the lower bound on the weight of the minimum-weight vertex cover. Statement 2: The lower bound can be found by maximizing the following Ever W(1)x (1) subject to х(u) + x(v) ≥ 1 for each (u,v) E V x(1) ≤ 1 for each v E V *(1) ≥ 0 for each 1 E V In the light of the above statements, choose the most appropriate answer from the options given below:

- **1.** Both statement I and Statement II are correct
- **2.** Both statement I and Statement Il are incorrect
- **3.** Statement I is correct but Statement II is incorrect
- **4.** Statement I is incorrect and Statement II is correct

> [!TIP]
> **Correct answer: 3. Statement I is correct but Statement II is incorrect**

## Solution

The LP relaxation of weighted vertex cover gives a lower bound on the integer optimum, so Statement I is correct. But it minimizes Σw(v)x(v) subject to x(u)+x(v)≥1 and 0≤x(v)≤1. Statement II says maximize, which is wrong.

## Key Points

- A minimization problem's relaxation provides a lower bound by minimizing over a larger feasible set.

## Why the other options are incorrect

Any choice accepting Statement II uses the wrong optimization direction; option 2 also rejects the valid relaxation principle.
