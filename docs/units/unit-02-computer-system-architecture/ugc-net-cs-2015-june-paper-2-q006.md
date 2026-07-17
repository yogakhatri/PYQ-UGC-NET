# Question 6

*UGC NET CS · 2015 June Paper 2 · Boolean Algebra · Boolean-Expression and Logic-Network Optimization*

Consider the following statements : (a) Boolean expressions and logic networks correspond to labelled acyclic digraphs. (b) Optimal boolean expressions may not correspond to simplest networks. (c) Choosing essential blocks first in a Karnaugh map and then greedily choosing the largest remaining blocks to cover may not give an optimal expression. Which of these statement(s) is/are correct ?

- **1.** (a) only
- **2.** (b) only
- **3.** (a) and (b)
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 4. (a), (b) and (c)**

## Solution

A combinational logic network can be represented as a labeled directed acyclic graph whose nodes are operations/gates and whose edges carry dependencies, so (a) is true. Minimizing a Boolean expression under one measure such as literal count need not minimize a physical network that may share subexpressions or use different gate costs, making (b) true. A greedy Karnaugh-map cover can commit to a large implicant that prevents the globally smallest cover, so (c) is also true.

## Key Points

- Boolean simplification is a cover problem, and expression cost, circuit cost, and a greedy local choice need not share one optimum.

## Why the other options are incorrect

Options 1–3 each discard at least one valid observation. The optimization target for expressions and circuits differs, and greedy set cover is not generally optimal; therefore the full set in option 4 is required.
