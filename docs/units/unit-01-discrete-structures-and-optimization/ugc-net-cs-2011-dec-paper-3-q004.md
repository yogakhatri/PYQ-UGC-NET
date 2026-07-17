# Question 4

*UGC NET CS · 2011 Dec Paper 3 · Optimization · Transportation Problem*

Sources S1, S2 and S3 have supplies 120, 80 and 80. Destinations D1, D2 and D3 demand 150, 80 and 50. Unit costs are S1=(8,5,6), S2=(15,10,12), S3=(3,9,10). Find a minimum-cost transportation schedule.


> [!TIP]
> **Correct answer: Optimal schedule: S1->D1=70, S1->D3=50, S2->D2=80, S3->D1=80; minimum cost=1900**

## Solution

Total supply and demand are both 280, so the problem is balanced. S3 has a very strong cost advantage for D1, so assign all 80 units from S3 to D1. D1 still needs 70. Comparing S1 with S2, using S1 instead of S2 saves 7 per unit at D1, 6 at D3 and 5 at D2. Use S1's 120 units where that saving is greatest: 70 to D1 and 50 to D3. S2 then sends its 80 units to D2.

The nonzero schedule is x11=70, x13=50, x22=80 and x31=80. All row supplies and column demands are satisfied. Cost=70(8)+50(6)+80(10)+80(3)=560+300+800+240=1900.

For an optimality check, use a degenerate zero basic cell x12 and potentials u1=0, v1=8, v2=5, v3=6, u2=5, u3=-5. Every nonbasic reduced cost c_ij-(u_i+v_j) is nonnegative (2, 1, 9 and 9 for x21, x23, x32 and x33), so no transportation loop can reduce the total.

## Key Points

- Build a feasible balanced schedule, allocate scarce low-cost routes by opportunity saving, then verify optimality with MODI reduced costs.

## Common mistakes to avoid

A least-cost allocation without checking row/column opportunity costs can waste S1 on D2 and force expensive S2 shipments to D1. Also, the source scan shows S3 supply as '8'; balance with total demand confirms the intended value is 80.
