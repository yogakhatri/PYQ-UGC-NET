# Question 7

*UGC NET CS · 2015 June Paper 3 · ER-to-Relational Mapping · Mapping One-to-Many and Many-to-Many Relationships*

Let E1 and E2 be two entities in E-R diagram with simple single valued attributes. R1 and R2 are two relationships between E1 and E2 where R1 is one - many and R2 is many - many. R1 and R2 donot have any attribute of their own. How many minimum number of tables are required to represent this situation in the Relational Model ?

- **1.** 4
- **2.** 3
- **3.** 2
- **4.** 1

> [!TIP]
> **Correct answer: 2. 3**

## Solution

Create one table for E1 and one for E2. The one-to-many relationship R1 has no attributes, so it can be represented by placing the primary key of the one side as a foreign key on the many side; it needs no separate table. The many-to-many relationship R2 requires a junction table containing the keys of E1 and E2. Total: `2 entity tables + 1 relationship table = 3`.

## Key Points

- 1:N without relationship attributes → foreign key; M:N → separate junction table.

## Why the other options are incorrect

Four tables unnecessarily creates a separate table for the attribute-free one-to-many relationship. Two tables cannot represent the independent many-to-many relationship without a multivalued field or repeated rows, and one table cannot faithfully represent both entity sets and both relationships.
