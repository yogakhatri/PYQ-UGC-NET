# Question 56

*UGC NET CS · 2019 Dec Paper 1 And 2 · Graph Algorithms · Minimum Spanning Trees*

What is the weight of a minimum spanning tree of the given weighted graph G, as calculated by Kruskal's algorithm?

- **1.** 14
- **2.** 15
- **3.** 17
- **4.** 18

> [!TIP]
> **Correct answer: 2. 15**

## Solution

Kruskal processes edges from smallest weight upward: 2,3,4,5,6,7,8. Select TL=2 and PQ=3. Select LQ=4, which joins those two components without a cycle. LP=5 would now create the cycle L–Q–P–L, so skip it. LR=6 connects the remaining vertex R. Four selected edges now span all five vertices, with total 2+3+4+6=15. Therefore option 2.

## Key Points

- Kruskal accepts the lightest edge that joins two different components and rejects any edge that creates a cycle.

## Why the other options are incorrect

A spanning tree on five vertices must contain four edges. Weight 14 would require using 2+3+4+5, but the weight-5 edge closes a cycle and still leaves R disconnected. Totals 17 and 18 use a heavier connection to R even though the weight-6 edge is available.
