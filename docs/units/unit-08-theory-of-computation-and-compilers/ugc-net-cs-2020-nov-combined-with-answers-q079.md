# Question 79

*UGC NET CS · 2020 Nov With Answers · Context-Free Language · Closure Properties and Determinism*

Which of the following statements is true?

- **1.** The union of two context-free languages is context-free.
- **2.** The intersection of two context free languages is context free.
- **3.** The complement of a context free language is context free.
- **4.** If a language is context free, it can always be accepted by a deterministic pushdown automaton.

> [!TIP]
> **Correct answer: 1. The union of two context-free languages is context-free.**

## Solution

Context-free languages are closed under union: given grammars for L1 and L2, add a fresh start symbol S with productions S→S1|S2. They are not closed in general under intersection or complement. They are also accepted in general by nondeterministic pushdown automata; deterministic CFLs form a proper subclass, so not every CFL has a DPDA. Therefore only statement 1 is true.

## Key Points

- CFL closure mnemonic: union, concatenation, and star—yes; arbitrary intersection and complement—no; NPDA, not always DPDA.

## Why the other options are incorrect

If CFLs were closed under complement as well as union, De Morgan's law would imply closure under intersection, which is known to fail. Statement 4 confuses NPDA power with the strictly weaker DPDA class.
