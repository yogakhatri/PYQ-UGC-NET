# Question 7

*UGC NET CS · 2013 June Paper 3 · Relational Model and Algebra · Projection and Duplicate Elimination*

The “PROJECT” operator of a relational algebra creates a new table that has always

- **A.** More columns than columns in original table
- **B.** More rows than original table
- **C.** Same number of rows as the original table
- **D.** Same number of columns as the original table

> [!TIP]
> **Correct answer: No listed option is always true. Projection produces no more columns and no more rows than the original relation; duplicate elimination can reduce the row count.**

## Solution

Relational-algebra projection pi_A1,...,Ak(R) retains only the named attributes, so its number of columns is k≤the original degree. Because relations are sets, duplicate projected tuples are eliminated; its number of rows is therefore at most the original cardinality and may be smaller. Example: projecting Department from two employees in the same department produces one department tuple, not two. Thus neither 'same rows' nor 'same columns' is guaranteed unless extra conditions are supplied.

## Key Points

- Projection can reduce both degree (columns) and cardinality (rows after duplicate removal); it never increases either.

## Why the other options are incorrect

A is impossible because projection selects existing attributes rather than adding columns. B is impossible because deleting attributes and duplicates cannot create more tuples. C fails when two original rows become the same projected tuple. D fails whenever a proper subset of columns is projected.
