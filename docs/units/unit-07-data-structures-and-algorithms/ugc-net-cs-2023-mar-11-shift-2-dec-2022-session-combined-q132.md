# Question 132

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Graph Algorithms · Minimum-spanning-tree edge order*

Given the graph below which one of the following edges cannot be added in that order to find a minimum spanning tree algorithm. A. a-b B. d-t C. b-f D. d-c E. d-e Choose the correct answer from the options given below:

- **1.** A, B,C, D.E
- **2.** A. B. D.C, E
- **3.** B, A, C, E, D
- **4.** B,A, D, C, E

> [!TIP]
> **Correct answer: 3. B, A, C, E, D**

## Solution

Kruskal processes edges by nondecreasing weight. Here A(a-b) and B(d-f) have weight 1; C(b-f) and D(d-c) have weight 2; E(d-e) has weight 3. Sequence B,A,C,E,D puts weight-3 E before weight-2 D and therefore cannot be the sorted addition order.

## Key Points

- Kruskal permits arbitrary tie order but never processes a heavier edge before an available lighter edge.

## Why the other options are incorrect

The other sequences keep both weight-1 edges before the weight-2 pair and E last; ties may appear in either order.
