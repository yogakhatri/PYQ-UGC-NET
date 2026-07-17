# Question 63

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Data Modeling · Relational union*

No.1 BID: 8701 _ operation combines the rows of the two relations and outputs a new relation that has both input relations' rows A. in it.

- **1.** difference
- **2.** union
- **3.** cartesian product
- **4.** project

> [!TIP]
> **Correct answer: 2. union**

## Solution

Relational union returns every tuple occurring in either compatible input relation, eliminating duplicates under set semantics. It therefore combines the rows of both relations.

## Key Points

- Union combines rows; projection selects columns.

## Why the other options are incorrect

Difference removes shared/right-side rows, Cartesian product combines columns across tuple pairs, and projection selects columns.
