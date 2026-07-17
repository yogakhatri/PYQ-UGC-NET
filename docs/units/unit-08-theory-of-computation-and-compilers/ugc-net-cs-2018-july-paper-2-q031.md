# Question 31

*UGC NET CS · 2018 July Paper 2 · Finite Automata · Language Equivalence of Finite-State Machines*

Two finite state machines are said to be equivalent if they :

- **1.** Have the same number of edges
- **2.** Have the same number of states
- **3.** Recognize the same set of tokens
- **4.** Have the same number of states and edges

> [!TIP]
> **Correct answer: 3. Recognize the same set of tokens**

## Solution

Two finite-state machines are equivalent when they accept exactly the same language: for every possible input string, either both accept or both reject. In lexical-analysis wording, that means they recognize the same set of tokens. Therefore option 3 is correct.

## Key Points

- Automaton equivalence is equality of accepted languages, not equality of diagrams.

## Why the other options are incorrect

Equivalent machines need not have the same number of states or transitions; minimization can remove redundant states while preserving the language. Hence edge/state counts in options 1, 2, and 4 are structural properties, not semantic equivalence.
