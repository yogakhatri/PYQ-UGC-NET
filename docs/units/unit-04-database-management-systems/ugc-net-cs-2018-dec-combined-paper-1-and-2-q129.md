# Question 129

*UGC NET CS · 2018 Dec Paper 1 And 2 · SQL · DROP TABLE and Relation Removal*

Which command is used to remove a relation from an SQL database?

- **1.** Drop table
- **2.** Delete table
- **3.** Remove table
- **4.** Update table

> [!TIP]
> **Correct answer: 1. Drop table**

## Solution

`DROP TABLE table_name` removes the table/relation definition from the database catalog and removes its stored data, subject to DBMS dependency rules. Thus the command for removing a relation is DROP TABLE, option 1.

## Key Points

- DROP removes the database object; DELETE removes rows; UPDATE changes rows.

## Why the other options are incorrect

`DELETE FROM table_name` removes selected rows but normally leaves the relation schema in place; `DELETE TABLE` is not the correct SQL syntax. `REMOVE TABLE` is not the standard SQL statement, and UPDATE changes values in existing rows rather than removing the relation.
