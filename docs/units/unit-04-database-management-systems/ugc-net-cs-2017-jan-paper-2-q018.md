# Question 18

*UGC NET CS · 2017 Jan Paper 2 · ER-to-Relational Mapping · Mapping One-to-Many and Many-to-Many Relationships*

Let M and N be two entities in an E-R diagram with simple single value attributes. R1 and R2 are two relationship between M and N, where as R1 is one-to-many and R2 is many-to-many. The minimum number of tables required to represent M, N, R1 and R2 in the relational model are _______.

- **1.** 4
- **2.** 6
- **3.** 7
- **4.** 3

> [!TIP]
> **Correct answer: 4. 3**

## Solution

Create one table for entity M and one for entity N. A one-to-many relationship R₁ with no relationship attributes can be represented by placing the primary key of the 'one' side as a foreign key in the table on the 'many' side, so it needs no separate relation. The many-to-many relationship R₂ requires a junction table containing the keys of M and N. Total tables=2 entity tables+1 junction table=3, which is option 4.

## Key Points

- 1:N relationship → foreign key on N side; M:N relationship → separate junction relation.

## Why the other options are incorrect

Four would unnecessarily create a separate table for the one-to-many relationship. Six and seven count each conceptual component or attribute as though it always required an independent table, which is not how ER-to-relational mapping works for simple single-valued attributes.
