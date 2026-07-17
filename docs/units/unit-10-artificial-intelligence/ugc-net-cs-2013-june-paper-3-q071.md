# Question 71

*UGC NET CS · 2013 June Paper 3 · Constraint Satisfaction · Map Coloring*

The map colouring problem can be solved using which of the following technique ?

- **A.** Means-end analysis
- **B.** Constraint satisfaction
- **C.** AO* search
- **D.** Breadth first search

> [!TIP]
> **Correct answer: B. Constraint satisfaction**

## Solution

Treat each map region as a variable, its allowed colors as the domain, and every shared border as a binary constraint requiring different colors. A solution is an assignment satisfying all adjacency constraints, which is exactly a constraint-satisfaction problem. Backtracking, constraint propagation and variable-ordering heuristics can then solve it efficiently.

## Key Points

- Map coloring is the canonical CSP: regions=variables, colors=domains, adjacent regions≠constraints.

## Why the other options are incorrect

Means-end analysis reduces differences between current and goal states but is not the natural formulation. AO* targets AND-OR graphs. Breadth-first search could enumerate assignments but ignores the problem's constraint structure and is not the defining technique.
