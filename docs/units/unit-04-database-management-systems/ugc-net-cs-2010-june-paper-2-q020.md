# Question 20

*UGC NET CS · 2010 June Paper 2 · Database System Concepts and Architecture · Centralized and Client/Server DBMS Architectures*

The PROJECT command creates a new table that has:

- **A.** more fields than the original table
- **B.** more rows than the original table
- **C.** both more fields and more rows
- **D.** none of these

> [!TIP]
> **Correct answer: D. none of these**

## Solution

Relational PROJECT selects specified columns. The result therefore has no more fields than the original; it may have fewer. Projection also does not create additional rows and duplicate elimination may reduce their number. None of A–C is true.

## Key Points

- Projection is a vertical subset of a relation, with duplicate result tuples removed.

## Why the other options are incorrect

A and C wrongly claim more columns, while B and C wrongly claim more tuples.
