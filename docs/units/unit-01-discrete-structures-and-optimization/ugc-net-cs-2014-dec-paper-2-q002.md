# Question 2

*UGC NET CS · 2014 Dec Paper 2 · Graph Theory · Degree Sum in Trees*

A certain tree has two vertices of degree 4, one vertex of degree 3 and one vertex of degree 2. If the other vertices have degree 1, how many vertices are there in the graph ?

- **A.** 5
- **B.** n – 3
- **C.** 20
- **D.** 11

> [!TIP]
> **Correct answer: D. 11**

## Solution

Let x be the number of degree-1 vertices. Then the tree has n=x+4 vertices. Its degree sum is 2·4+3+2+x=13+x. A tree with n vertices has n−1 edges, so the handshaking lemma gives degree sum 2(n−1)=2(x+3)=2x+6. Equating the sums yields 13+x=2x+6, hence x=7 and n=7+4=11.

## Key Points

- For a tree, combine the handshaking lemma with |E|=|V|−1.

## Why the other options are incorrect

5 and 20 do not satisfy both the specified degrees and the tree identity sum deg=2(n−1). 'n−3' is not a numerical vertex count and does not result from solving the equation.
