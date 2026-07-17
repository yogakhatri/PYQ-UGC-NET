# Question 62

*UGC NET CS · 2017 Jan Paper 3 · Turing Machines · Recursive and Recursively Enumerable Languages*

Which of the following pairs have different expressive power ?

- **1.** Single-tape-turing machine and multi-dimensional turing machine.
- **2.** Multi-tape turing machine and multi-dimensional turing machine.
- **3.** Deterministic push down automata and non-deterministic pushdown automata.
- **4.** Deterministic finite automata and Non-deterministic finite automata

> [!TIP]
> **Correct answer: 3. Deterministic push down automata and non-deterministic pushdown automata.**

## Solution

Single-tape, multitape, and multidimensional Turing machines recognize the same class of languages; the richer tapes can improve convenience or running time but can be simulated by an ordinary Turing machine. DFA and NFA also have equal expressive power because subset construction converts an NFA to a DFA. A nondeterministic PDA recognizes every CFL, while a deterministic PDA recognizes only the proper subclass of deterministic CFLs. Thus DPDA and NPDA have different expressive power, which is option 3.

## Key Points

- Nondeterminism adds no language power to finite automata or Turing machines, but it does add power to pushdown automata.

## Why the other options are incorrect

Options 1 and 2 compare equivalent Turing-machine variants. Option 4 compares equivalent finite-automaton variants. Only pushdown nondeterminism increases the accepted language family.
