# Question 70

*UGC NET CS · 2018 Dec Paper 1 And 2 · Graph Theory · Hamiltonian Sufficient Conditions*

Let G be a simple graph with n≥3 vertices. Consider these proposed sufficient conditions for G to be Hamiltonian: (i) deg(v)≥n/3 for every vertex v; (ii) deg(v)+deg(w)≥n whenever nonadjacent vertices v and w are chosen; (iii) |E(G)|≥(1/3)(n−1)(n−2)+2. Which conditions are sufficient?

- **1.** (i) and (iii) only
- **2.** (ii) only
- **3.** (ii) and (iii) only
- **4.** (iii) only

> [!TIP]
> **Correct answer: 2. (ii) only**

## Solution

Condition (ii) is exactly Ore’s theorem: a simple n-vertex graph (n≥3) is Hamiltonian if every nonadjacent pair v,w satisfies deg(v)+deg(w)≥n. Condition (i) is not sufficient: for n=6, the disconnected graph K₃∪K₃ has every degree equal to 2=n/3 but cannot have a spanning cycle. Condition (iii) is also not sufficient: K₃,₄ has n=7 and 12 edges, meeting (1/3)(6)(5)+2=12, yet every bipartite cycle uses equal numbers from both parts, so K₃,₄ has no Hamiltonian 7-cycle. Thus only (ii) is sufficient, option 2.

## Key Points

- Recognize Ore’s degree-sum theorem; disprove weaker proposed bounds with small disconnected or unbalanced-bipartite counterexamples.

## Why the other options are incorrect

Options 1, 3, and 4 include at least one disproved condition. The classical minimum-degree sufficient bound is n/2 (Dirac), not n/3, and the printed one-third edge bound is too weak.

## References

- [Emory University mathematics paper — statement of Ore’s theorem](https://www.math.emory.edu/~rg/P133Y09.pdf)
