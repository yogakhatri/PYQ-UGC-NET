# Question 56

*UGC NET CS · 2014 Dec Paper 3 · Approaches to AI · A* Evaluation Function*

An A* algorithm is a heuristic search technique which

- **A.** It is like depth-first search, where the most promising child is selected for expansion.
- **B.** It generates successor nodes, estimates the start-to-goal cost through them, and chooses the generated alternative with the smallest estimated cost.
- **C.** It stores only path costs from the start to generated nodes and chooses the shortest such path for expansion.
- **D.** none of the above

> [!TIP]
> **Correct answer: B. It generates successor nodes, estimates the start-to-goal cost through them, and chooses the generated alternative with the smallest estimated cost.**

## Solution

A* evaluates a generated node n with f(n)=g(n)+h(n), where g is the known cost from the start and h estimates the remaining cost to a goal. It maintains generated alternatives and expands the one with smallest f, which is the start-to-goal cost estimate described by B. With an admissible/consistent heuristic, the usual graph-search form can be optimal under its standard conditions.

## Key Points

- A* balances cost already paid and estimated cost remaining through f=g+h.

## Why the other options are incorrect

A describes a locally promising depth-first/greedy behavior and ignores accumulated cost. C chooses only the smallest path cost from the start, which is uniform-cost search using g alone. B is slightly informal in saying 'successor,' but it is the only choice that combines path cost and a goal estimate, the defining A* idea.
