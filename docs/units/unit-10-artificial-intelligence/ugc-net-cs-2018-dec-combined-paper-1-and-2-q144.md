# Question 144

*UGC NET CS · 2018 Dec Paper 1 And 2 · Informed Search Strategies · Greedy, A-star, RBFS and IDA-star*

Match the search algorithms with their descriptions: (a) Greedy best-first search, (b) A* search, (c) recursive best-first search, (d) iterative-deepening A* search; (i) selects a node for expansion if an optimal path to that node has been found, (ii) avoids the substantial overhead associated with keeping a sorted queue of nodes, (iii) suffers from excessive node generation, (iv) time complexity depends on the quality of the heuristic.

- **1.** (a)-(i), (b)-(ii), (c)-(iii), (d)-(iv)
- **2.** (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)
- **3.** (a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)
- **4.** (a)-(i), (b)-(iv), (c)-(iii), (d)-(ii)

> [!TIP]
> **Correct answer: 2. (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)**

## Solution

Greedy best-first search orders nodes only by h(n), so its running time depends strongly on how informative the heuristic is: (a)→(iv). With a consistent heuristic, when A* removes a node for expansion, the least-cost path to that node has been found: (b)→(i). Recursive best-first search uses recursion and backed-up f-values instead of retaining a globally sorted best-first queue, so (c)→(ii). Iterative-deepening A* repeats bounded searches and can regenerate many nodes, giving (d)→(iii). Hence option 2.

## Key Points

- Best-first variants trade heuristic guidance, optimality conditions, memory, and repeated work in different ways.

## Why the other options are incorrect

The other matchings exchange defining properties among algorithms. In particular, greedy search has no guarantee that an expanded node has been reached optimally; RBFS is the memory-saving method that avoids the large sorted frontier; and IDA* trades low memory for repeated generation across successive thresholds.
