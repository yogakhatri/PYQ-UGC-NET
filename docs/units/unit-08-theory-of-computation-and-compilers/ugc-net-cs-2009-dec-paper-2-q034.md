# Question 34

*UGC NET CS · 2009 Dec Paper 2 · Context-Free Language · Linear versus Deterministic Context-Free Languages*

Contex-free Grammar (CFG) can be recognized by

- **A.** Finite state automata
- **B.** 2-way linear bounded automata
- **C.** push down automata
- **D.** both (B) and (C)

> [!TIP]
> **Correct answer: D. both (B) and (C)**

## Solution

A pushdown automaton recognizes exactly the context-free languages. A two-way linear-bounded automaton is at least as powerful for this purpose and can simulate the necessary stack within linearly bounded tape. Therefore both B and C can recognize CFG languages.

## Key Points

- PDA = CFL recognition; stronger bounded-tape machines can also recognize CFLs.

## Why the other options are incorrect

A finite automaton recognizes only regular languages, a strict subset of CFLs, so A alone is insufficient.
