# Question 5

*UGC NET CS · 2015 June Paper 2 · Graph Theory · Sufficient versus Necessary Hamiltonicity Conditions*

For a simple graph G on n vertices, consider these Hamiltonicity conditions: (a) deg(v)≥n/2 for every vertex v; (b) |E(G)|≥(n−1)(n−2)/2+2; (c) deg(v)+deg(w)≥n for every nonadjacent pair v,w. Which listed combination is true with respect to Hamiltonian graphs?

- **1.** (a) and (b)
- **2.** (b) and (c)
- **3.** (a) and (c)
- **4.** (a), (b), and (c)

> [!TIP]
> **Correct answer: As written, no option is necessary for every Hamiltonian graph. If the intended question is which conditions are sufficient for Hamiltonicity, option 4: (a), (b), and (c).**

## Solution

Dirac's condition (a) and Ore's condition (c) are classic sufficient conditions: satisfying either guarantees a Hamiltonian cycle under the usual order assumptions. The extremal edge bound (b) is also sufficient because a simple non-Hamiltonian n-vertex graph has at most C(n−1,2)+1 edges. But none is necessary. For n≥6, the cycle Cₙ is Hamiltonian while every degree is 2, nonadjacent degree sums are 4, and it has only n edges, so it violates all three bounds.

## Key Points

- Do not reverse a sufficient theorem: Dirac/Ore-style degree bounds guarantee Hamiltonicity but Hamiltonian graphs need not satisfy them.

## Why the other options are incorrect

The stem begins by assuming G is Hamiltonian, which asks for necessary consequences; none of the combinations is then guaranteed. Options 1–3 are also incomplete under the alternative sufficient-condition reading, where all three theorems apply. The distinction between 'if condition, then Hamiltonian' and 'if Hamiltonian, then condition' is the defect.
