# Question 139

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Context-Free Language · Chomsky and Greibach Normal Forms*

Consider the following statements: (A) For every regular language, we can design Turing Machine (B) For every context free language, we can design Turing Machine Which of the following is correct?

- **1.** Statement-A is false and Statement-B is true.
- **2.** Statement-A and Statement-B both are false.
- **3.** Statement-A is true and Statement-B is false.
- **4.** Statement-A and Statement-B both are true.

> [!TIP]
> **Correct answer: 4. Statement-A and Statement-B both are true.**

## Solution

Every regular language is accepted by a finite automaton and can also be decided by a Turing machine that simulates that automaton. Likewise, every context-free language has a pushdown automaton and a Turing machine can simulate it; membership in a CFL is decidable. Therefore both A and B are true.

## Key Points

- A Turing machine can simulate weaker automata such as finite automata and pushdown automata.

## Why the other options are incorrect

Regular and context-free languages are both strict subsets of the decidable languages, so neither assertion is false.
