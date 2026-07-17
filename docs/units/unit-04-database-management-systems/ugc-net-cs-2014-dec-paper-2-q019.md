# Question 19

*UGC NET CS · 2014 Dec Paper 2 · Normalization for Relational Databases · Third Normal Form versus BCNF*

The best normal form of relation scheme R(A, B, C, D) along with the set of functional dependencies F = {AB → C, AB → D, C → A, D → B} is

- **A.** Boyce-Codd Normal form
- **B.** Third Normal form
- **C.** Second Normal form
- **D.** First Normal form

> [!TIP]
> **Correct answer: B. Third Normal form**

## Solution

AB is a candidate key because AB→C and AB→D; other candidate keys include AD, BC and CD. Hence every attribute A,B,C,D is prime. The dependencies C→A and D→B violate BCNF because C and D are not superkeys. They still satisfy 3NF because their right-hand attributes A and B are prime. The AB dependencies have a superkey determinant, so the relation's highest normal form is 3NF.

## Key Points

- 3NF permits a non-superkey determinant when the dependent attribute is prime; BCNF does not.

## Why the other options are incorrect

A ignores the non-superkey determinants C and D. C and D understate the result: the schema satisfies 3NF, not merely 2NF or 1NF.
