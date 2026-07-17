# Question 142

*UGC NET CS · 2019 June Paper 1 And 2 · Approaches to AI · Best-first search*

Match List I with List II. List I: (a) Greedy best-first; (b) Lowest cost-first; (c) A* algorithm. List II: (i) minimal cost(p)+h(p); (ii) minimal h(p); (iii) minimal cost(p).

- **1.** a-i, b-ii, c-iii
- **2.** a-iii, b-ii, c-i
- **3.** a-i, b-iii, c-ii
- **4.** a-ii, b-iii, c-i

> [!TIP]
> **Correct answer: 4. a-ii, b-iii, c-i**

## Solution

Greedy best-first search selects the path or node with the smallest heuristic estimate h(p), so (a)-(ii). Lowest-cost-first, also called uniform-cost search, selects the smallest accumulated path cost cost(p), so (b)-(iii). A* selects the smallest estimated total solution cost cost(p)+h(p), so (c)-(i). The matching is a-ii, b-iii, c-i.

## Key Points

- Greedy uses h; uniform-cost uses g; A* uses f=g+h.

## Why the other options are incorrect

Options 1-3 interchange the evaluation functions. The diagnostic distinction is that greedy ignores cost-so-far, uniform-cost ignores the heuristic, and A* adds both.
