# Question 37

*UGC NET CS · 2018 July Paper 2 · Context-Sensitive Languages · Linear-Bounded Automata*

Context sensitive language can be recognized by a :

- **1.** Finite state machine
- **2.** Deterministic finite automata
- **3.** Non-deterministic finite automata
- **4.** Linear bounded automata

> [!TIP]
> **Correct answer: 4. Linear bounded automata**

## Solution

Context-sensitive languages are characterized by linear-bounded automata: Turing machines whose usable tape is bounded by a linear function of the input length. Therefore option 4 is correct.

## Key Points

- Chomsky hierarchy machine model: regular→finite automaton, context-free→PDA, context-sensitive→LBA, recursively enumerable→Turing machine.

## Why the other options are incorrect

Finite-state machines, DFAs, and NFAs are equivalent in power and recognize only regular languages, a strict subset of context-sensitive languages. They lack the bounded work tape needed for context-dependent counting and rewriting.
