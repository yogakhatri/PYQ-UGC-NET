# Question 89

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Approaches to AI · Alpha-beta pruning*

Where does the values of alpha-beta search get updated?

- **1.** Along the path of search.
- **2.** Initial state itself.
- **3.** At the end.
- **4.** None of these.

> [!TIP]
> **Correct answer: 1. Along the path of search.**

## Solution

Alpha and beta are bounds associated with nodes on the current minimax search path. As child values return, the algorithm updates these bounds up the ancestor path and prunes when α≥β.

## Key Points

- Alpha-beta pruning propagates bounds along the active root-to-node path.

## Why the other options are incorrect

The bounds are not fixed only at the initial state or postponed until the entire search ends; incremental updates are exactly what enables pruning.
