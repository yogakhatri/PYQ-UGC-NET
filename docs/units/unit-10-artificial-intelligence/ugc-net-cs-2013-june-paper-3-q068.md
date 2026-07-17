# Question 68

*UGC NET CS · 2013 June Paper 3 · AI Search · Informed versus Uninformed Search*

Which one of the following is not an informed search technique ?

- **A.** Hill climbing search
- **B.** Best first search
- **C.** A* search
- **D.** Depth first search

> [!TIP]
> **Correct answer: D. Depth first search**

## Solution

An informed search uses problem-specific heuristic information to choose promising states. Hill climbing follows heuristic improvement, best-first search expands the most promising node according to an evaluation function, and A* uses f(n)=g(n)+h(n). Depth-first search uses only the search-tree structure, expanding the deepest available node without a heuristic, so it is uninformed.

## Key Points

- Informed search consults h(n) or another domain estimate; DFS needs only a stack and successor relation.

## Why the other options are incorrect

A, B and C all explicitly depend on a heuristic or evaluation estimate. D may be combined with heuristics in a hybrid algorithm, but plain DFS itself is not informed search.
