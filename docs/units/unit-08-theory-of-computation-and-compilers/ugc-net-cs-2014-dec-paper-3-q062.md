# Question 62

*UGC NET CS · 2014 Dec Paper 3 · Formal Grammars and Automata · Grammar-to-Machine Correspondence*

Match the following : List – I List – II a. Context free grammar i. Linear bounded automaton b. Regular grammar ii. Pushdown automaton c. Context sensitive grammar iii. Turing machine d. Unrestricted grammar iv. Deterministic finite automaton Codes : a b c d

- **A.** ii iv iii i
- **B.** ii iv i iii
- **C.** iv i ii iii
- **D.** i iv iii ii

> [!TIP]
> **Correct answer: B. ii iv i iii**

## Solution

A context-free grammar is equivalent in expressive power to a pushdown automaton, so a→ii. A regular grammar corresponds to a finite automaton, here a DFA, b→iv. A context-sensitive grammar corresponds to a linear-bounded automaton, c→i. An unrestricted grammar generates recursively enumerable languages recognized by a Turing machine, d→iii. The code is ii, iv, i, iii.

## Key Points

- Type 3→FA, Type 2→PDA, Type 1→LBA, Type 0→Turing machine.

## Why the other options are incorrect

A associates context-sensitive grammar with a Turing machine and unrestricted grammar with an LBA, reversing the top two levels. C and D mismatch the CFG/PDA relation and other hierarchy levels. B follows the Chomsky hierarchy exactly.
