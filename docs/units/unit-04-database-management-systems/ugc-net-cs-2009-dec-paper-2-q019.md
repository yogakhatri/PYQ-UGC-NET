# Question 19

*UGC NET CS · 2009 Dec Paper 2 · Normalization for Relational Databases · Functional Dependencies and Normalization*

A function that has no partial functional dependencies is in __________ form.

- **A.** 3 NF
- **B.** 2 NF
- **C.** 4 NF
- **D.** BCNF

> [!TIP]
> **Correct answer: B. 2 NF**

## Solution

Second normal form requires a relation already in 1NF to have no partial dependency of a non-prime attribute on a proper subset of a candidate key. Therefore absence of partial functional dependencies is the defining 2NF condition.

## Key Points

- 2NF removes partial-key dependencies.

## Why the other options are incorrect

3NF additionally addresses transitive dependencies, BCNF strengthens determinant requirements, and 4NF addresses nontrivial multivalued dependencies.
