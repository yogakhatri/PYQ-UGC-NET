# Question 9

*UGC NET CS · 2015 June Paper 3 · Relational Database Design · 3NF, BCNF, Losslessness, and Dependency Preservation*

Select the False statement from the following statements about Normal Forms :

- **1.** Lossless preserving decomposition into 3NF is always possible
- **2.** Lossless preserving decomposition into BCNF is always possible
- **3.** Any Relation with two attributes is in BCNF
- **4.** BCNF is stronger than 3NF

> [!TIP]
> **Correct answer: 2. Lossless preserving decomposition into BCNF is always possible**

## Solution

Every relation can be decomposed losslessly into BCNF, but preserving every original functional dependency at the same time is not always possible. Therefore the claim that a lossless, dependency-preserving BCNF decomposition is always possible is false.

## Key Points

- 3NF can guarantee both losslessness and dependency preservation; BCNF may require sacrificing dependency preservation.

## Why the other options are incorrect

A synthesis algorithm always gives a lossless, dependency-preserving 3NF decomposition, so statement 1 is true. Any nontrivial dependency in a two-attribute relation makes its determinant a key, so statement 3 is true. BCNF is stricter than 3NF because it requires every determinant of a nontrivial FD to be a superkey, making statement 4 true.
