# Question 69

*UGC NET CS · 2015 June Paper 3 · Optimization · Linear-Programming Duality Theorems*

Given the following statements with respect to linear programming problem : S1 : The dual of the dual linear programming problem is again the primal problem S2 : If either the primal or the dual problem has an unbounded objective function value, the other problem has no feasible solution. S3 : If either the primal or dual problem has a finite optimal solution, the other one also possesses the same, and the optimal value of the objective functions of the two problems are equal. Which of the following is true ?

- **1.** S1 and S2
- **2.** S1 and S3
- **3.** S2 and S3
- **4.** S1, S2 and S3

> [!TIP]
> **Correct answer: 4. S1, S2 and S3**

## Solution

S1 is the involution property of LP duality: dualizing twice returns the primal in corresponding standard form. S2 follows from weak duality: if one side were feasible while the other had an improving unbounded objective, their objective inequality would be violated, so the opposite problem must be infeasible. S3 is strong duality: when either side has a finite optimum, the other also has an optimum with the same objective value. All three are true.

## Key Points

- LP duality: dual-of-dual, unbounded-versus-infeasible alternative, and equal finite optima.

## Why the other options are incorrect

Options 1–3 omit one of these standard duality results. Under the usual primal–dual pair and feasibility conventions assumed in LP theory, no statement needs to be excluded.
