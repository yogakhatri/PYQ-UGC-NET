# Question 143

*UGC NET CS · 2018 Dec Paper 1 And 2 · Uninformed Search Strategies · Space Complexity of BFS, DFS, DLS and IDS*

Let b be the branching factor, d the depth of the shallowest solution, m the maximum depth of the search tree, and l the depth limit. Match each algorithm with its space complexity: (a) breadth-first search, (b) depth-first search, (c) depth-limited search, (d) iterative-deepening search; (i) O(bd), (ii) O(b^d), (iii) O(bm), (iv) O(bl).

- **1.** (a)-(i), (b)-(ii), (c)-(iv), (d)-(iii)
- **2.** (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)
- **3.** (a)-(iii), (b)-(ii), (c)-(iv), (d)-(i)
- **4.** (a)-(i), (b)-(iii), (c)-(iv), (d)-(ii)

> [!TIP]
> **Correct answer: 2. (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)**

## Solution

Breadth-first search keeps an entire frontier whose size can grow exponentially to O(b^d), so (a)→(ii). Depth-first search stores at most a path of length m plus up to b pending siblings per level, O(bm), so (b)→(iii). A depth limit l changes that bound to O(bl), giving (c)→(iv). Iterative deepening repeatedly runs depth-limited DFS but retains only its current path and siblings; at the successful limit d its space is O(bd), so (d)→(i). The complete matching is option 2.

## Key Points

- BFS pays exponential memory for its frontier; DFS-family methods keep only a path and pending siblings, giving linear-in-depth memory.

## Why the other options are incorrect

Options 1 and 4 incorrectly give breadth-first search linear path-like storage even though BFS retains the wide frontier. Option 3 assigns DFS the exponential BFS bound. Re-expanding shallow nodes increases iterative deepening's time, not its peak space, so its space remains O(bd).
