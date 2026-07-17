# Question 12

*UGC NET CS · 2014 Dec Paper 3 · Normalization for Relational Databases · BCNF and Dependency Types*

Which of the following is false ?

- **A.** Every binary relation is never be in BCNF.
- **B.** Every BCNF relation is in 3NF.
- **C.** 1 NF, 2 NF, 3 NF and BCNF are based on functional dependencies.
- **D.** Multivalued Dependency (MVD) is a special case of Join Dependency (JD) .

> [!TIP]
> **Correct answer: Both A and C are false, so the question has no unique correct option.**

## Solution

A two-attribute (binary) relation schema is always in BCNF: any nontrivial dependency from one attribute to the other makes the determinant a key, and without such a dependency BCNF holds vacuously. Therefore A's claim that every binary relation is never in BCNF is false. C is also false because 1NF is based on atomic domains/repeating-group structure, not functional dependencies; 2NF, 3NF and BCNF use FDs. B is true because BCNF is stronger than 3NF, and D is true because an MVD is a special two-component join dependency.

## Key Points

- Every binary schema is BCNF; 1NF concerns atomicity, while higher dependency normal forms use FDs, MVDs or JDs.

## Why the other options are incorrect

B and D are true statements and therefore cannot answer 'which is false.' The defect is that both A and C qualify, so selecting only one would hide a genuine normalization distinction.
