# Question 13

*UGC NET CS · 2012 Dec Paper 2 · Normalization · BCNF and 3NF*

Which statement is true?

- **1.** A relation in BCNF is always in 3NF
- **2.** A relation in 3NF is always in BCNF
- **3.** BCNF and 3NF are the same
- **4.** A relation in BCNF is not in 3NF

> [!TIP]
> **Correct answer: 1. A relation in BCNF is always in 3NF**

## Solution

BCNF requires every nontrivial functional dependency X -> Y to have X as a superkey. Third normal form permits one additional case: when X is not a superkey, the dependency may still be accepted if each attribute of Y is prime. BCNF therefore imposes at least all the restrictions of 3NF, so every BCNF relation is in 3NF.

## Key Points

- BCNF is stricter than 3NF: BCNF implies 3NF, but 3NF does not always imply BCNF.

## Why the other options are incorrect

A 3NF relation need not be in BCNF because 3NF's prime-attribute exception can allow a determinant that is not a superkey. Consequently the two forms are not identical, and a BCNF relation cannot fail 3NF.
