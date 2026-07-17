# Question 57

*UGC NET CS · 2017 Jan Paper 3 · Planning · Planning-Graph Levels*

In Artificial Intelligence (AI), what is present in the planning graph ?

- **1.** Sequence of levels
- **2.** Literals
- **3.** Variables
- **4.** Heuristic estimates

> [!TIP]
> **Correct answer: 1. Sequence of levels**

## Solution

A planning graph is fundamentally a leveled structure: it starts from the initial proposition level and alternates action levels with proposition/literal levels as time steps advance. Literals are indeed nodes inside the proposition levels, but the most complete structural answer to what the graph contains is a sequence of levels. Therefore option 1 is correct.

## Key Points

- Planning graph = alternating proposition/literal and action levels, plus edges and mutual-exclusion relations.

## Why the other options are incorrect

Option 2 names only one kind of node within some levels, not the overall structure; action nodes and mutex relations are also present. Variables and heuristic estimates are not the defining contents of the graph, although heuristics can be derived from it.
