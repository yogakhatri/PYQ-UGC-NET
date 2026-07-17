# Question 146

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Design Techniques · Fractional-knapsack greedy solution*

510-96096 Read the passage carefully and answer the question that follows For a knapsack problem, P and W are profits and weights for a set of 7 items as given below: P= (9,5,2,7,6,16,9} W=(2,5,6,11,1,9,3} Find the optimal solution for fractional knapsack problem when its maximum capacity is 15.

- **1.** 43
- **2.** 40
- **3.** 45
- **4.** 44

> [!TIP]
> **Correct answer: 2. 40**

## Solution

Compute profit/weight ratios: item 5=6, item 1=4.5, item 7=3, item 6=16/9≈1.78, item 2=1, item 4≈0.64, item 3≈0.33. With capacity 15, take items 5,1,7,6 completely. Their weights are 1+2+3+9=15 and profits are 6+9+9+16=40. Therefore the optimum is 40.

## Key Points

- Fractional knapsack takes items in decreasing profit-to-weight ratio.

## Why the other options are incorrect

The greedy ratio order exactly fills the capacity at value 40; 43, 44, and 45 cannot be obtained by replacing any selected weight with lower-ratio material.
