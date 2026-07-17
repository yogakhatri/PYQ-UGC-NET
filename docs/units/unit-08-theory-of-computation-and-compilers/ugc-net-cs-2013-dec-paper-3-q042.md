# Question 42

*UGC NET CS · 2013 Dec Paper 3 · Language Hierarchy · Context-Sensitive and Recursive Languages*

Given the following statements : S 1 : Every context-sensitive language L is recursive. S 2 : There exists a recursive language that is not context sensitive. Which statement is correct ?

- **A.** S 1 is not correct and S 2 is not correct.
- **B.** S 1 is not correct and S 2 is correct.
- **C.** S 1 is correct and S 2 is not correct.
- **D.** S 1 is correct and S2 is correct.

> [!TIP]
> **Correct answer: D. S 1 is correct and S2 is correct.**

## Solution

Every context-sensitive language is decidable: a linear-bounded automaton has only finitely many configurations on a fixed input, so its acceptance can be decided by exploring the configuration graph without looping forever. Thus every context-sensitive language is recursive. The containment is proper; the recursive languages include languages that require more than linear space and are not context-sensitive. Therefore both S1 and S2 are correct.

## Key Points

- Chomsky/decidability containment: regular ⊂ context-free ⊂ context-sensitive ⊂ recursive ⊂ recursively enumerable.

## Why the other options are incorrect

A and B deny the valid inclusion CSL⊆Recursive. C incorrectly treats that inclusion as equality and denies that recursive languages exist outside CSL.
