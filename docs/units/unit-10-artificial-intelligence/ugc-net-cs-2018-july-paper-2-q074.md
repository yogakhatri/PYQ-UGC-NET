# Question 74

*UGC NET CS · 2018 July Paper 2 · Heuristic Search · A* Node Expansion and Pruning*

Consider statements about A*: (a) A* expands all nodes with f(n)<C*. (b) A* expands no nodes with f(n)≥C*. (c) Pruning is integral to A*. Here C* is the cost of an optimal solution path. Which choice is correct?

- **1.** Both statement (a) and statement (b) are true.
- **2.** Both statement (a) and statement (c) are true.
- **3.** Both statement (b) and statement (c) are true.
- **4.** All the statements (a), (b) and (c) are true.

> [!TIP]
> **Correct answer: 2. Both statement (a) and statement (c) are true.**

## Solution

Statement (a) is true: with the standard admissible/consistent A* conditions, nodes with f(n)<C* are surely expanded. Statement (b), exactly as printed, is false because A* may expand some nodes on the goal contour f(n)=C*; the no-expansion guarantee applies to f(n)>C*, not f(n)≥C*. Statement (c) is true in the textbook sense that A* uses its f-cost bound to leave unnecessary higher-contour nodes unexpanded—an effective pruning of the search space. Thus (a) and (c) are true, option 2.

## Key Points

- A* surely expands f<C*, may expand f=C*, and expands no f>C* nodes; equality is the crucial boundary case.

## Why the other options are incorrect

Options 1, 3, and 4 all accept statement (b) and incorrectly exclude the equality contour. Tie-breaking can make A* expand one or several f=C* nodes before choosing an optimal goal.

## References

- [University of Nebraska–Lincoln — Informed Search Methods](https://cse.unl.edu/~choueiry/F23-476-876/Slides/search-3.pdf)
