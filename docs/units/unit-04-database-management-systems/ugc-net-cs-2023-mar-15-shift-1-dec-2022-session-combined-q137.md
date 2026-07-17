# Question 137

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Normalization for Relational Databases · Functional Dependencies and Normalization*

Given below are the two statements: Statement I : Any retrieval request that is specified in the basic relational algebra can also be specified in relational calculus. Statement II : Any retrieval request that is specified in the relational calculus can also be specified in basic relational algebra. In the light of the above statements, choose the correct answer from the options given below:

- **1.** Both Statement I and Statement Il are true.
- **2.** Both Statement I and Statement Il are false.
- **3.** Statement I is true but Statement Il is false.
- **4.** Statement I is false but Statement Il is true.

> [!TIP]
> **Correct answer: 1. Both Statement I and Statement Il are true.**

## Solution

Codd's expressive-equivalence result states that relational algebra and safe (domain-independent) relational calculus express the same class of database queries. Thus an algebra query can be written in calculus, and a safe calculus query can be written in algebra. Both statements are true under the standard database interpretation.

## Key Points

- Relational algebra and safe relational calculus are relationally complete and expressively equivalent.

## Why the other options are incorrect

The other choices deny one or both directions of this equivalence. Unrestricted, unsafe calculus expressions are excluded in the standard theorem.
