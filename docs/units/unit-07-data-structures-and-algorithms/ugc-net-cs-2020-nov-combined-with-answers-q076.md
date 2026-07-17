# Question 76

*UGC NET CS · 2020 Nov With Answers · Graph Algorithms · Shortest Paths in Implicit Graphs*

Let G be a directed graph whose vertex set is the set of numbers from 1 to 100. There is an edge from a vertex i to a vertex j if and only if either j = i + 1 or j = 3i. The minimum number of edges in a path in G from vertex 1 to vertex 100 is _

- **1.** 23
- **2.** 99
- **3.** 4
- **4.** 7

> [!TIP]
> **Correct answer: 4. 7**

## Solution

A seven-edge path is 1→3→9→10→11→33→99→100: four ×3 moves and three +1 moves. It corresponds to building the base-3 representation 100=(10201)₃ from left to right. Reversing confirms the count: 100→99 by −1, →33 by ÷3, →11 by ÷3, →10 by −1, →9 by −1, →3 by ÷3, →1 by ÷3. Each reverse step undoes one allowed edge, giving 7 steps. Therefore option 4.

## Key Points

- For operations ×3 and +1, base-3 digits expose an efficient path; reverse with ÷3 and −1 to verify it.

## Why the other options are incorrect

Ninety-nine uses only +1 moves. Twenty-three and four do not match the optimal combination of multiplication and increments; four ×3 moves alone produce powers of three and cannot reach 100 without the three required increments encoded by its base-3 digits.
