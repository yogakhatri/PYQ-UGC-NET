# Question 126

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Graph Theory · Edges and connected components*

stoption 10-403 S1. 0: 87076 Let 'G' be a simple, undirected graph with n (n> 10) vertices and 'k' connected components. What is the minimum possible number of edges of 'G'?

- **1.** k(n-1)
- **2.** n(k-1)
- **3.** n+k-2
- **4.** n-k

> [!TIP]
> **Correct answer: 4. n-k**

## Solution

Each connected component with v_i vertices needs at least v_i−1 edges. Summing across k components gives Σ(v_i−1)=n−k. A forest attains this bound.

## Key Points

- A forest with n vertices and k components has exactly n−k edges.

## Why the other options are incorrect

The other formulas exceed or do not match the spanning-forest lower bound.
