# Question 55

*UGC NET CS · 2019 June Paper 1 And 2 · Graph Theory · Hamiltonian Paths and Circuits*

For which values of m and n does the complete bipartite graph K(m,n) have a Hamilton circuit?

- **1.** m != n, m,n >= 2
- **2.** m != n, m,n >= 3
- **3.** m = n, m,n >= 2
- **4.** m = n, m,n >= 3

> [!TIP]
> **Correct answer: 3. m = n, m,n >= 2**

## Solution

A cycle in a bipartite graph alternates between its two partite sets. A Hamilton circuit visits every vertex exactly once before returning, so it must use the same number of vertices from both parts; hence m=n. A cycle needs at least four vertices, so each part must contain at least two vertices. Thus K(m,n) has a Hamilton circuit exactly when m=n and m,n≥2.

## Key Points

- A Hamilton cycle in K(m,n) must alternate between the two parts, forcing m=n≥2.

## Why the other options are incorrect

- **Options 1 and 2:** unequal part sizes make an alternating Hamilton cycle impossible.
- **Option 4:** the lower bound 3 is too strict because K(2,2) itself is a four-cycle.
