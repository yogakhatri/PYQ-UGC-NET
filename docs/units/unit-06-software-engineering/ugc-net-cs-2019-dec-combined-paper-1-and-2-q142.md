# Question 142

*UGC NET CS · 2019 Dec Paper 1 And 2 · Software Testing · Flow Graphs and Basis-Path Testing*

What is the cyclomatic complexity of flowgraph F?

- **1.** 2
- **2.** 3
- **3.** 4
- **4.** 5

> [!TIP]
> **Correct answer: 3. 4**

## Solution

The flowgraph has three predicate nodes—1, (2,3), and 6—because each has two outgoing branches. For a connected structured flowgraph, cyclomatic complexity can be calculated as V(G)=P+1, where P is the number of predicate nodes. Thus V(G)=3+1=4. The edge-node formula confirms it: with E=11 edges and N=9 nodes, V(G)=E−N+2=11−9+2=4. Therefore option 3.

## Key Points

- For one connected flowgraph, V=E−N+2=P+1; predicate status depends on outgoing branches.

## Why the other options are incorrect

Two or three undercount the independent decisions, while five adds a nonexistent predicate. A merge node such as 9 or 10 can have several incoming edges but is not a predicate unless it has more than one outgoing edge.

## Question Figure

![Question figure](../../assets/questions/ugc-net-2019-dec-flowgraph-q141-q145.png)
