# Question 61

*UGC NET CS · 2018 July Paper 2 · Relational Algebra · Inner, Outer, Semi and Anti Joins*

In RDBMS, which type of Join returns all rows that satisfy the join condition ?

- **1.** Inner Join
- **2.** Outer Join
- **3.** Semi Join
- **4.** Anti Join

> [!TIP]
> **Correct answer: 1. Inner Join**

## Solution

An inner join combines exactly those row pairs for which the join predicate evaluates to true. It therefore returns all rows that satisfy the join condition and excludes unmatched rows. Hence option 1 is correct.

## Key Points

- Inner join = matching row pairs only; outer join = matching pairs plus specified unmatched rows.

## Why the other options are incorrect

An outer join additionally preserves unmatched rows from one or both inputs and fills the missing side with NULLs. A semijoin returns matching rows from only one relation rather than the combined pair. An antijoin returns rows for which no match exists.
