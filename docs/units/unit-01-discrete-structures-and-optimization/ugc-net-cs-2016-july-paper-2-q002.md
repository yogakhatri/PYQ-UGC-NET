# Question 2

*UGC NET CS · 2016 July Paper 2 · Graph Theory · Counting Spanning Trees*

How many different spanning trees do the complete graph K₄ and the complete bipartite graph K₂,₂ have, respectively?

- **1.** 14, 14
- **2.** 16, 14
- **3.** 16, 4
- **4.** 14, 4

> [!TIP]
> **Correct answer: 3. 16, 4**

## Solution

Cayley's formula gives n^{n−2} spanning trees for Kₙ, so K₄ has 4²=16. A complete bipartite graph K_{m,n} has m^{n−1}n^{m−1} spanning trees. For K₂,₂ this is 2¹·2¹=4. The requested pair is therefore (16,4), option 3.

## Key Points

- τ(Kₙ)=n^{n−2}; τ(K_{m,n})=m^{n−1}n^{m−1}.

## Why the other options are incorrect

The values 14 do not satisfy either standard counting formula. K₂,₂ is a 4-cycle, and deleting any one of its four edges gives a different spanning tree, confirming the second count directly.
