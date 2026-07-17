# Question 2

*UGC NET CS · 2015 Dec Paper 2 · Graph Theory · Euler, Hamilton and bipartite graph properties*

Which of the following statements are false? (a) A connected multigraph has an Euler circuit if and only if each of its vertices has even degree. (b) A connected multigraph has an Euler path but not an Euler circuit if and only if it has exactly two vertices of odd degree. (c) A complete graph K_n has a Hamilton circuit whenever n ≥ 3. (d) A cycle over six vertices C_6 is not bipartite, but a complete graph over three vertices K_3 is bipartite.

- **1.** (a) only
- **2.** (b) and (c)
- **3.** (c) only
- **4.** (d) only

> [!TIP]
> **Correct answer: 4. (d) only**

## Solution

Statements (a), (b), and (c) are standard graph-theory facts. A connected multigraph has an Euler circuit exactly when every vertex has even degree; it has an open Euler path exactly when two vertices have odd degree; and K_n has a Hamilton cycle for every n ≥ 3. Statement (d) reverses both bipartite facts: the even cycle C_6 is bipartite, while K_3 is an odd cycle and is not bipartite. Therefore only (d) is false.

## Key Points

- Euler conditions depend on vertex parity; bipartiteness is equivalent to having no odd cycle.

## Why the other options are incorrect

Options 1–3 mark at least one of the true statements (a)–(c) as false. The quick bipartite test is that a graph is bipartite exactly when it contains no odd cycle.
