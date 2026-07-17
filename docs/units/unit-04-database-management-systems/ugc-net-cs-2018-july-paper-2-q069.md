# Question 69

*UGC NET CS · 2018 July Paper 2 · Integrity Constraints · Referential Integrity on Insert and Delete*

Let R1(a,b,c) and R2(x,y,z) be relations in which a is a foreign key of R1 referring to the primary key of R2. Consider: (a) insert into R1, (b) insert into R2, (c) delete from R1, and (d) delete from R2. Which operations can violate referential integrity?

- **1.** Operations (a) and (b) will cause violation.
- **2.** Operations (b) and (c) will cause violation.
- **3.** Operations (c) and (d) will cause violation.
- **4.** Operations (d) and (a) will cause violation.

> [!TIP]
> **Correct answer: 4. Operations (d) and (a) will cause violation.**

## Solution

R1 is the child relation and R2 the parent. Inserting a child row into R1 can violate referential integrity if its foreign-key value has no matching R2 key. Deleting an R2 parent row can violate it if R1 rows still reference that key. Inserting a parent and deleting a child are safe with respect to this constraint. Hence operations (d) and (a) can violate it, option 4.

## Key Points

- Foreign-key risk occurs when adding a child or removing its referenced parent.

## Why the other options are incorrect

Options 1–3 each include insertion into the parent or deletion from the child as a violating operation; neither creates a dangling child reference. Actual DBMS actions such as RESTRICT, CASCADE, or SET NULL determine how an attempted parent deletion is handled.
