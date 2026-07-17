# Question 150

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Performance Analysis and Recurrences · Time and Space Complexity*

SI: 100100 Read the passage carefully and answer the question that follows For a knapsack problem, P and W are profits and weights for a set of 7 items as given below: P=(9,5,2,7,6,16,9} W={2,5,6,11,1,9,3} Which of the following statements is correct for a knapsack?

- **1.** 0/1 knapsack can be applied for all kinds of problems but fractional knapsack can be applied only if the problem meets certain conditions.
- **2.** There is no difference between the two. They give the same solution for any problem.
- **3.** We use greedy algorithm for 0/1 knapsack and dynamic programming for fractional knapsack.
- **4.** In 0/1 knapsack problem, items cannot be divided into smaller portions and in fractional knapsack we can divide the item into required proportions of weight.

> [!TIP]
> **Correct answer: 4. In 0/1 knapsack problem, items cannot be divided into smaller portions and in fractional knapsack we can divide the item into required proportions of weight.**

## Solution

In 0/1 knapsack each item is indivisible: it is either selected completely (1) or excluded (0). Fractional knapsack permits taking any required fraction of an item. Option 4 states this defining distinction.

## Key Points

- 0/1 decisions are indivisible; fractional decisions allow partial items.

## Why the other options are incorrect

The two models do not always yield the same optimum. Their usual algorithms are reversed in option 3: 0/1 commonly uses dynamic programming, whereas fractional uses greedy selection. Option 1 is vague and does not identify the mathematical difference.
