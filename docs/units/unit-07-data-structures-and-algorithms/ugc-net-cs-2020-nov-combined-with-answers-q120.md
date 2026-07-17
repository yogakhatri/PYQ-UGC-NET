# Question 120

*UGC NET CS · 2020 Nov With Answers · Graph Algorithms · Complexity of Graph Algorithms*

Match the graph algorithms with the listed time bounds: (A) topological sort of a DAG, (B) Kruskal’s MST algorithm, (C) Bellman–Ford single-source shortest paths, (D) Floyd–Warshall all-pairs shortest paths. List II: (I) O(V+E), (II) O(VE), (III) Θ(V+E), (IV) Θ(V³).

- **1.** A-I, B-III, C-IV, D-II
- **2.** A-III, B-I, C-IV, D-II
- **3.** A-III, B-I, C-II, D-IV
- **4.** A-I, B-III, C-II, D-IV

> [!TIP]
> **Correct answer: 3. A-III, B-I, C-II, D-IV**

## Solution

Topological sorting visits each vertex and edge once, giving Θ(V+E), so A→III. Bellman–Ford performs up to V−1 passes over E edges, giving O(VE), so C→II. Floyd–Warshall has three nested vertex loops, giving Θ(V³), so D→IV. The remaining listed match is Kruskal→I, yielding option 3. This I=O(V+E) bound assumes edges are already sorted or can be sorted linearly; with ordinary comparison sorting, standard Kruskal is O(E log E), usually written O(E log V).

## Key Points

- Memorize the robust three: topo Θ(V+E), Bellman–Ford O(VE), Floyd–Warshall Θ(V³); treat Kruskal’s sorting assumption explicitly.

## Why the other options are incorrect

Options 1 and 2 assign Bellman–Ford or Floyd–Warshall the wrong bound; option 4 calls topological sorting only O(V+E) while assigning Θ(V+E) to Kruskal. Under standard unsorted input none of the listed Kruskal bounds is fully general, so the paper’s intended assumption matters.
