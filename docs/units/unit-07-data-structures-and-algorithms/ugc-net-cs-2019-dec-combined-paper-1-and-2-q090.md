# Question 90

*UGC NET CS · 2019 Dec Paper 1 And 2 · Graph Algorithms · Edge Relaxation*

In a weighted directed graph, d[x] is the current shortest-distance estimate from source S to x. If d[v]=29, d[u]=15, and edge weight w(u,v)=12, what is the updated value of d[v] after relaxing (u,v)?

- **1.** 29
- **2.** 27
- **3.** 25
- **4.** 17

> [!TIP]
> **Correct answer: 2. 27**

## Solution

Relaxing edge (u,v) compares the old estimate d[v] with the path reaching u and then taking the edge: d[u]+w(u,v)=15+12=27. The update is d[v]=min(29,27)=27. Hence option 2.

## Key Points

- Edge relaxation formula: d[v]←min(d[v], d[u]+w(u,v)).

## Why the other options are incorrect

Twenty-nine is the unrevised estimate and should be replaced because 27 is smaller. Twenty-five and seventeen do not equal either the existing value or the candidate path value. Relaxation never invents a value other than the minimum of those two quantities.
