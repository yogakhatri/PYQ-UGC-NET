# Question 23

*UGC NET CS · 2017 Nov Paper 2 · Graph Algorithms · Minimum Spanning Trees*

Let G be an undirected connected graph with distinct edge weight. Let Emax be the edge with maximum weight and Emin the edge with minimum weight. Which of the following statements is false ?

- **1.** Every minimum spanning tree of G must contain Emin.
- **2.** If Emax is in minimum spanning tree, then its removal must disconnect G.
- **3.** No minimum spanning tree contains Emax.
- **4.** G has a unique minimum spanning tree.

> [!TIP]
> **Correct answer: 3. No minimum spanning tree contains Emax.**

## Solution

Statement 3 is false. If the globally maximum edge Emax is a bridge, every spanning tree—and hence the MST—must contain it. The other statements hold with distinct weights: Emin is the unique lightest edge across a suitable cut and must be selected; if Emax appears in an MST it cannot lie on a cycle, so it must be a bridge whose removal disconnects G; and distinct edge weights guarantee a unique MST. Therefore option 3 is the requested false statement.

## Key Points

- Cycle property excludes a uniquely heaviest cycle edge, but a bridge lies on no cycle and is unavoidable regardless of its weight.

## Why the other options are incorrect

Options 1, 2, and 4 are valid consequences of cut/cycle properties under distinct weights. A two-component graph joined by one very heavy bridge is a simple counterexample to the claim that no MST can contain Emax.
