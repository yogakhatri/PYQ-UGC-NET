# Question 57

*UGC NET CS · 2019 Dec Paper 1 And 2 · Graph Theory · Degree Sum and Edge Count in Trees*

A tree has 2n vertices of degree 1, 3n vertices of degree 2. n vertices of degree 3. Determine the number of vertices and edges in tree.

- **1.** 12 vertices, 11 edges
- **2.** 11 vertices, 12 edges
- **3.** 10 vertices, 11 edges
- **4.** 9 vertices, 10 edges

> [!TIP]
> **Correct answer: 1. 12 vertices, 11 edges**

## Solution

The total number of vertices is V=2n+3n+n=6n. By the handshaking lemma, the degree sum is 2n·1+3n·2+n·3=11n=2E. A tree satisfies E=V−1=6n−1. Substituting gives 11n=2(6n−1)=12n−2, so n=2. Hence V=12 and E=11, option 1.

## Key Points

- Combine Σdeg(v)=2E with the tree identity E=V−1.

## Why the other options are incorrect

A tree always has exactly one fewer edge than vertices, immediately ruling out (11,12), (10,11), and (9,10), all of which list more edges than vertices. The degree calculation independently fixes the only possible pair as (12,11).
