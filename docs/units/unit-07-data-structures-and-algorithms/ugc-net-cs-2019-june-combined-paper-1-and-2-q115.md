# Question 115

*UGC NET CS · 2019 June Paper 1 And 2 · Graph Algorithms · DFS*

Which of the following is application of depth-first search?

- **1.** Only topological sort
- **2.** Only strongly connected components
- **3.** Both topological sort and strongly connected components
- **4.** Neither topological sort nor strongly connected components

> [!TIP]
> **Correct answer: 3. Both topological sort and strongly connected components**

## Solution

Depth-first search supplies the finishing-time information needed for both applications. In a directed acyclic graph, listing vertices in decreasing DFS finishing time gives a topological order. For strongly connected components, Kosaraju's algorithm uses DFS finishing times and a second DFS on the transpose graph; Tarjan's algorithm also obtains SCCs from one DFS using low-link values. Thus both are DFS applications.

## Key Points

- DFS finishing times drive topological sorting and SCC algorithms.

## Why the other options are incorrect

Options 1 and 2 omit one valid application. Option 4 rejects two standard textbook uses of DFS.
