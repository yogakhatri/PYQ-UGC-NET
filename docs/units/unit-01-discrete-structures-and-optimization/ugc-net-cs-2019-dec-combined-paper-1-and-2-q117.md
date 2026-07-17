# Question 117

*UGC NET CS · 2019 Dec Paper 1 And 2 · Optimization · Linear-Programming Duality Theorems*

Consider the following statements with respect to duality in LPP: (a) The final simplex table giving optimal solution of the primal also contains optimal solution of its dual in itself. (b) If either the primal or the dual problem has a finite optimal solution. then the other problem also has a finite optimal solution. (c) If either problem has an unbounded optimum solution, then the other problem has no feasible solution at all. Which of the statements is (are) correct?

- **1.** only (a) and (b)
- **2.** only (a) and (c)
- **3.** only (b) and (c)
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 4. (a), (b) and (c)**

## Solution

Statement (a) is true: in the standard simplex formulation, the final optimal tableau's objective-row information yields the dual prices and hence a dual optimum. Statement (b) is strong duality—if one side has a finite optimum, the other is feasible with the same finite optimal value. Statement (c) follows from weak duality: if the opposite problem had any feasible solution, its objective would bound the first problem, contradicting unboundedness. All three statements are correct, so option 4.

## Key Points

- LP duality links statuses: finite optimum ↔ finite optimum with equal value; unbounded on one side ⇒ infeasible on the other.

## Why the other options are incorrect

Options 1–3 each omit one valid duality fact. A frequent mistake is to think primal unboundedness makes the dual unbounded too; the correct implication is that the dual is infeasible, and conversely with primal and dual exchanged.
