# Question 107

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Graph Theory · Hamiltonian Paths and Circuits*

For Hamiltonian problems, assess: A. Hamiltonian cycle is NP-complete. B. Every odd-order undirected bipartite graph is Hamiltonian. C. Hamiltonian path cannot be solved in polynomial time on a DAG. D. The cube G³ of every connected graph G with at least three vertices is Hamiltonian. E. If any NP-complete problem is polynomial-time solvable, then P=NP.

- **1.** A, B, C only
- **2.** B, D, E only
- **3.** A, D, E only
- **4.** A, C, E only

> [!TIP]
> **Correct answer: 3. A, D, E only**

## Solution

A is true. B is false because a bipartite Hamiltonian cycle alternates partitions and therefore has even order. C is false because longest/Hamiltonian path in a DAG is solvable by dynamic programming in topological order. D is the graph-cube Hamiltonicity theorem, and E follows from NP-completeness. Thus A,D,E.

## Key Points

- Hamiltonian path is hard generally but polynomial on DAGs; bipartite Hamilton cycles require equal partitions.

## Why the other options are incorrect

Options 1,2,4 include false B/C or omit true D.
