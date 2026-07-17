# Question 54

*UGC NET CS · 2019 June Paper 1 And 2 · Graph Theory · Planar Graph*

Suppose that a connected planar graph has six vertices, each of degree four. Into how many regions is the plane divided by a planar representation of this graph?

- **1.** 6
- **2.** 8
- **3.** 12
- **4.** 20

> [!TIP]
> **Correct answer: 2. 8**

## Solution

The handshaking lemma gives 2E as the sum of all vertex degrees. With six vertices of degree four, 2E=6×4=24, hence E=12. Euler's formula for a connected planar graph is V-E+F=2. Therefore F=2-V+E=2-6+12=8 regions, including the unbounded outer region.

## Key Points

- For a connected planar graph, first find E from the degree sum and then use V-E+F=2.

## Why the other options are incorrect

- **Option 1:** equals the vertex count, not the face count.
- **Option 3:** is the number of edges.
- **Option 4:** does not satisfy Euler's formula for V=6 and E=12.
