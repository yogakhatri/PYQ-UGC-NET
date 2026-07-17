# Question 29

*UGC NET CS · 2018 July Paper 2 · Trees and Binary Trees · Full m-ary Tree Leaf Formula*

A full 5-ary tree has exactly five children at every internal node. How many leaf nodes does such a tree have when it has 8 internal nodes?

- **1.** 30
- **2.** 33
- **3.** 45
- **4.** 125

> [!TIP]
> **Correct answer: 2. 33**

## Solution

Let I be internal nodes, L leaves, and m=5 children per internal node. The tree has mI=5×8=40 edges because each internal node contributes five child edges. It also has I+L−1 edges, so 40=8+L−1 and L=33. Equivalently, L=(m−1)I+1=4×8+1=33. Therefore option 2 is correct.

## Key Points

- A full m-ary tree with I internal nodes has L=(m−1)I+1 leaves and mI+1 total nodes.

## Why the other options are incorrect

30, 45, and 125 do not satisfy the edge-count identity. Multiplying 5×8 counts child edges, not leaves; some child endpoints are internal nodes, so those eight must be accounted for.
