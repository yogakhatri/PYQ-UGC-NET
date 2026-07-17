# Question 84

*UGC NET CS · 2019 June Paper 1 And 2 · Normalization for Relational Databases · BCNF and the normal-form hierarchy*

In relational databases, if relation R is in BCNF, then which of the following is true about relation R?

- **1.** R is in 4NF
- **2.** R is not in 1NF
- **3.** R is in 2NF but not in 3NF
- **4.** R is in 2NF and 3NF

> [!TIP]
> **Correct answer: 4. R is in 2NF and 3NF**

## Solution

The normal-form hierarchy based on functional dependencies is BCNF ⇒ 3NF ⇒ 2NF ⇒ 1NF. Therefore every BCNF relation is necessarily in both 3NF and 2NF. BCNF does not by itself guarantee 4NF because fourth normal form also constrains nontrivial multivalued dependencies.

## Key Points

- BCNF is stronger than 3NF for functional dependencies, while 4NF adds requirements for multivalued dependencies.

## Why the other options are incorrect

- **Option 1:** BCNF need not satisfy 4NF.
- **Option 2:** BCNF already presupposes first normal form.
- **Option 3:** contradicts the fact that BCNF implies 3NF.
