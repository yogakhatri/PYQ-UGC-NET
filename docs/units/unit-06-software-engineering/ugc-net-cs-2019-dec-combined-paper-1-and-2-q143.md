# Question 143

*UGC NET CS · 2019 Dec Paper 1 And 2 · Software Testing · Flow Graphs and Basis-Path Testing*

How many regions are there in flowgraph F?

- **1.** 2
- **2.** 3
- **3.** 4
- **4.** 5

> [!TIP]
> **Correct answer: 3. 4**

## Solution

A planar connected flowgraph has as many regions as its cyclomatic complexity when the unbounded outside area is included. From the graph, E=11 and N=9, so V(G)=E−N+2=4. Equivalently, the graph has three predicate nodes and hence P+1=4 regions. Visually these correspond to the bounded areas created by the branches and loop together with the exterior region. Therefore there are 4 regions, option 3.

## Key Points

- Include the outside region: for a connected planar flowgraph, number of regions = cyclomatic complexity.

## Why the other options are incorrect

Counts of two or three usually omit the exterior region or one branch-created region. Five treats a merge as if it opened another region. Region counting and cyclomatic complexity must agree for this connected planar flowgraph.

## Question Figure

![Question figure](../../assets/questions/ugc-net-2019-dec-flowgraph-q141-q145.png)
