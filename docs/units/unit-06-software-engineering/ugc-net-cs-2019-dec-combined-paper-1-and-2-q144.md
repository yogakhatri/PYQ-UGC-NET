# Question 144

*UGC NET CS · 2019 Dec Paper 1 And 2 · Software Testing · Flow Graphs and Basis-Path Testing*

How many nodes are there in the longest independent path?

- **1.** 6
- **2.** 7
- **3.** 8
- **4.** 9

> [!TIP]
> **Correct answer: 3. 8**

## Solution

A longest basic independent path may traverse the loop once before taking the exit. One such path is 1 → (2,3) → 6 → 7 → 9 → 10 → 1 → 11; replacing 7 by 8 gives another of the same length. Counting node occurrences along the path gives eight: the entry node 1 appears once before the loop body and once after the back edge returns. The alternative branch through (4,5) is shorter. Hence the longest independent path contains 8 node occurrences, option 3.

## Key Points

- Trace a complete entry-to-exit basic path; when a back edge returns to a node, count that second occurrence in the path length.

## Why the other options are incorrect

Six omits part of the longest branch or the loop return, seven commonly counts the repeated entry node only once, and nine requires adding a node that cannot occur on the same independent route without traversing mutually exclusive branches or repeating the loop.

## Question Figure

![Question figure](../../assets/questions/ugc-net-2019-dec-flowgraph-q141-q145.png)
