# Question 27

*UGC NET CS · 2015 Dec Paper 3 · Finite Automata · Counting Deterministic Automata*

How many deterministic finite automata have the three named states x,y,z over alphabet {a,b}, with x fixed as the start state?

- **1.** 64
- **2.** 256
- **3.** 1024
- **4.** 5832

> [!TIP]
> **Correct answer: 4. 5832**

## Solution

A DFA transition function must choose one of 3 destinations for each of 3 states and 2 input symbols, giving 3^(3×2)=3^6=729 transition functions. The fixed start state adds no choice. Any subset of the 3 states may be accepting, giving 2^3=8 choices. Total=729×8=5,832.

## Key Points

- Number of labeled DFAs = n^(n|Σ|) transition functions × 2^n final-state sets when the start is fixed.

## Why the other options are incorrect

64, 256, and 1,024 count only partial structural choices. A complete DFA count must include every state-symbol transition and every possible accepting-state subset.
