# Question 25

*UGC NET CS · 2013 June Paper 3 · Optimization · Vogel's Approximation Method*

The total transportation cost in an initial basic feasible solution to the following transportation problem using Vogel’s Approximation method is W1 W2 W3 W4 W5 Supply F1 4 2 3 2 6 8 F2 5 4 5 2 1 12 F3 6 5 4 7 3 14 Demand 4 4 6 8 8

- **A.** 76
- **B.** 80
- **C.** 90
- **D.** 96

> [!TIP]
> **Correct answer: B. 80**

## Solution

Total supply is 8+12+14=34 while total demand is 30, so first add a dummy destination of demand 4 and zero costs. Vogel's penalties first allocate F3→Dummy=4. A consistent continuation allocates F2→W5=8, F2→W4=4, F1→W4=4, F1→W2=4, F3→W1=4 and F3→W3=6. The real transportation cost is 8(1)+4(2)+4(2)+4(2)+4(6)+6(4)=8+8+8+8+24+24=80; the dummy allocation costs zero.

## Key Points

- Before VAM, balance supply and demand with a zero-cost dummy; then repeatedly use the largest row/column penalty.

## Why the other options are incorrect

76, 90 and 96 do not equal the cost of the VAM allocation after balancing the problem. Omitting the dummy destination leaves supply and demand unequal and prevents a valid basic feasible solution.
