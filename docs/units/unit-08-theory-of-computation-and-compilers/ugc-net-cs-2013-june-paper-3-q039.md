# Question 39

*UGC NET CS · 2013 June Paper 3 · Chomsky Hierarchy · Grammar and Machine Equivalences*

Match the following : a. Context sensitive language i. Deterministic finite automation b. Regular grammar ii. Recursive enumerable c. Context free grammar iii. Recursive language d. Unrestricted grammar iv. Pushdown automation Codes : a b c d

- **A.** ii i iv iii
- **B.** iii iv i ii
- **C.** iii i iv ii
- **D.** ii iv i iii

> [!TIP]
> **Correct answer: C. iii i iv ii**

## Solution

A regular grammar is recognized by a deterministic finite automaton, so b→i. A context-free grammar is recognized by a pushdown automaton, so c→iv. An unrestricted grammar generates a recursively enumerable language, so d→ii. Context-sensitive languages are decidable and therefore recursive, giving a→iii among the supplied choices. The sequence is iii, i, iv, ii.

## Key Points

- Regular↔finite automaton, context-free↔PDA, unrestricted↔recursively enumerable; context-sensitive languages are recursive.

## Why the other options are incorrect

A and D associate context-sensitive languages with recursively enumerable and unrestricted grammars with recursive, losing the intended Chomsky-hierarchy pairing. B incorrectly connects a regular grammar to a PDA and a context-free grammar to a DFA.
