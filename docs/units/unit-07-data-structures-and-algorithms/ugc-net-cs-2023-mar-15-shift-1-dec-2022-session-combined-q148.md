# Question 148

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Design Techniques · Fractional-knapsack running time*

S1.0:87098 Read the passage carefully and answer the question that follows For a knapsack problem, P and W are profits and weights for a set of 7 items as given below: P= (9,5,2,7,6,16,9} W=(2,5,6,11,1,9,3} If new item (P=5, W= 2) is added to the list, total items is 8 and capacity is 25, then the best-case time of fractional knapsack for this case is

- **1.** 0(8)
- **2.** 0(64)
- **3.** O(24)
- **4.** 0(56)

> [!TIP]
> **Correct answer: 3. O(24)**

## Solution

The standard fractional-knapsack procedure orders n items by profit/weight ratio, which takes Θ(n log n), and then scans them in Θ(n). For n=8, n log₂n=8×3=24, so the listed form is O(24). The added item's numerical profit and weight do not change this asymptotic step count.

## Key Points

- Fractional knapsack is dominated by sorting ratios: O(n log n).

## Why the other options are incorrect

O(8) counts only the final scan and ignores ordering; O(64) is quadratic; O(56) corresponds to n(n−1) comparisons rather than the standard sorting bound.
