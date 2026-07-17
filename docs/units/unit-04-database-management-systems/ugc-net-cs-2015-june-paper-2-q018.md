# Question 18

*UGC NET CS · 2015 June Paper 2 · Database Constraints · Foreign-Key References and DROP TABLE*

DROP TABLE cannot be used to drop a table referenced by which constraint? (a) Primary key (b) Sub key (c) Super key (d) Foreign key

- **1.** (a) only
- **2.** (a), (b), and (c)
- **3.** (d) only
- **4.** (a) and (d)

> [!TIP]
> **Correct answer: 3. (d) only**

## Solution

A foreign-key constraint in one table refers to a candidate key—commonly the primary key—of another table. Dropping the referenced table would leave that foreign key with no target, so a DBMS using restrictive drop semantics rejects the operation. The referencing foreign key must first be removed, or an explicitly supported cascading drop must be requested. Therefore statement (d) alone identifies the blocking constraint.

## Key Points

- A table cannot be restrictively dropped while another table's foreign key still references it.

## Why the other options are incorrect

Primary, subkey, and superkey are descriptions of keys within the table being dropped; they are not themselves incoming references from another table. A primary key can be the target of a foreign key, but the dependency that blocks the drop is the foreign-key constraint. Hence options 1, 2, and 4 misidentify the referencing constraint.
