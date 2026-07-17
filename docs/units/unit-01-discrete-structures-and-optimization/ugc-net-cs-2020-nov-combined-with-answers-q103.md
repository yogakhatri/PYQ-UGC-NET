# Question 103

*UGC NET CS · 2020 Nov With Answers · Graph Theory · Graph Colouring and Bipartite Graphs*

Consider the statements: (A) Every tree is 2-colourable. (B) A bipartite graph has no cycles of even length. (C) A bipartite graph is 2-colourable. (D) A graph of maximum degree d can be coloured with d+1 colours. (E) A graph with O(|V|) edges can always be coloured with O(log |V|) colours. Which pair of statements is incorrect?

- **1.** (C) and (E) are incorrect
- **2.** (B) and (C) are incorrect
- **3.** (B) and (E) are incorrect
- **4.** (A) and (D) are incorrect

> [!TIP]
> **Correct answer: 3. (B) and (E) are incorrect**

## Solution

A tree has no cycle, hence no odd cycle, so it is bipartite and 2-colourable: A is true. A graph is bipartite exactly when it has no odd cycle; it may certainly contain even cycles such as C₄, so B is false and C is true. Greedy colouring uses at most d+1 colours when maximum degree is d, so D is true. E is false: take a clique on about √n vertices plus enough isolated vertices to make n total vertices. It has Θ(n) edges but needs Θ(√n) colours, not O(log n). Thus the incorrect statements are B and E, option 3.

## Key Points

- Bipartite forbids odd—not even—cycles, and a sparse whole graph can still contain a moderately large clique.

## Why the other options are incorrect

Options 1 and 2 wrongly mark C incorrect, even though bipartite and 2-colourable are equivalent. Option 4 wrongly rejects the standard tree and greedy-colouring facts.
