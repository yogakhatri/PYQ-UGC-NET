# Question 4

*UGC NET CS · 2012 June Paper 2 · Graph Theory · Planar Graph Colouring*

The number of colours required to properly colour the vertices of every planar graph is

- **A.** 2
- **B.** 3
- **C.** 4
- **D.** 5

> [!TIP]
> **Correct answer: C. 4**

## Solution

The Four Colour Theorem states that every planar graph can have its vertices coloured with at most four colours so that adjacent vertices receive different colours. Four is also sometimes necessary; for example, the planar complete graph K4 has four mutually adjacent vertices and needs four distinct colours. Therefore the universal guaranteed number is 4.

## Key Points

- Every planar graph is 4-colourable, and K4 shows that the bound cannot be lowered to 3.

## Why the other options are incorrect

Two colours work only for bipartite planar graphs. Three are insufficient for planar graphs such as K4. Five colours do suffice by the Five Colour Theorem, but they are not required because the sharper four-colour bound holds.
