# Question 136

*UGC NET CS · 2020 Nov With Answers · Graph Algorithms · DFS Edge Types and BFS Levels*

Let G be a simple undirected graph, TD a DFS tree of G, and TB a BFS tree of G. Statement I: No edge of G is a cross edge with respect to TD. Statement II: For every edge (u,v) of G, if u is at depth i and v at depth j in TB, then |i-j|=1. Choose the correct evaluation.

- **1.** Both Statement I and Statement II are true
- **2.** Both Statement I and Statement Il are false
- **3.** Statement I is correct but Statement II is false
- **4.** Statement I is incorrect but Statement Il is true.

> [!TIP]
> **Correct answer: 3. Statement I is correct but Statement II is false**

## Solution

During DFS of an undirected graph, an edge either becomes a tree edge or joins a vertex to one of its ancestors, making it a back edge; undirected DFS has no cross edges. Statement I is therefore true. In BFS, an edge can join vertices on the same level or on adjacent levels, so the guaranteed condition is |i−j|≤1, not |i−j|=1. A triangle rooted at one vertex gives an immediate same-level edge between the other two vertices. Statement II is false, so option 3 is correct.

## Key Points

- Undirected DFS non-tree edges go to ancestors; BFS endpoints of an edge differ in depth by at most one.

## Why the other options are incorrect

Options 1 and 4 accept the too-strong equality for BFS levels. Option 2 incorrectly imports directed-graph DFS edge categories into a simple undirected DFS.
