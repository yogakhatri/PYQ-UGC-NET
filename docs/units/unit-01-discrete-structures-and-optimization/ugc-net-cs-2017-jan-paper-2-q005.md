# Question 5

*UGC NET CS · 2017 Jan Paper 2 · Graph Theory · Hamiltonian Paths and Circuits*

Consider a Hamiltonian graph G with no loops or parallel edges and with |V(G)|=n≥3. Which of the following must be true?

- **1.** deg(v) ≥ n/2 for each vertex v.
- **2.** |E(G)| ≥ (1/2)(n−1)(n−2)+2
- **3.** deg (v) + deg(w) ≥ n whenever v and w are not connected by an edge.
- **4.** All of the above

> [!TIP]
> **Correct answer: No listed option is necessarily true — the three conditions are sufficient for Hamiltonicity, not necessary**

## Solution

A Hamiltonian graph contains a spanning cycle, but it need not be dense. Take the cycle graph C₆. It is Hamiltonian, simple, and has n=6. Every vertex has degree 2, so statement 1 fails because 2<6/2. It has only 6 edges, so statement 2 fails because 6<(1/2)(5)(4)+2=12. Any two nonadjacent vertices still have degree sum 2+2=4<6, so statement 3 also fails. Thus a single valid Hamiltonian graph refutes all three universal claims, and 'all of the above' is also false.

## Key Points

- Do not reverse a sufficient-condition theorem: dense enough ⇒ Hamiltonian does not mean Hamiltonian ⇒ dense enough.

## Why the other options are incorrect

Statements 1 and 3 are the hypotheses of Dirac's and Ore's theorems: if a graph satisfies them, Hamiltonicity follows. The implication does not reverse. The large edge-count bound is likewise a sufficient density condition, not something every Hamiltonian graph must satisfy.

## Additional Information

This question is defective as printed because it provides no 'none of the above' option. A cycle Cₙ for sufficiently large n is the standard counterexample.

## References

- [Biton, Levi and Medina — Dirac and Ore graph conditions](https://arxiv.org/abs/2302.00742)
