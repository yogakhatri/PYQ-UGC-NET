# Question 149

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Design Techniques · Divide and Conquer*

il. No.9 BID:8709 Read the passage carefully and answer the question that follows For a knapsack problem, P and W are profits and weights for a set of 7 items as given below: P=(9,5,2,7,6,16,9} W= (2,5,6,11,1,9,3} The most efficient solution for the fractional knapsack problem with maximum capacity 15 can be obtained by using____

- **1.** Divide and Conquer
- **2.** Dynamic Programming
- **3.** Greedy Algorithm
- **4.** Backtracking

> [!TIP]
> **Correct answer: 3. Greedy Algorithm**

## Solution

Fractional knapsack has the greedy-choice property: choosing the greatest available profit per unit weight can never be improved by first taking a lower-ratio portion. Sorting by that ratio and filling capacity greedily therefore produces an optimum.

## Key Points

- Divisibility makes the locally best profit/weight choice globally optimal.

## Why the other options are incorrect

Dynamic programming is standard for 0/1 knapsack, while divide-and-conquer and backtracking are unnecessary for the divisible-item version.
