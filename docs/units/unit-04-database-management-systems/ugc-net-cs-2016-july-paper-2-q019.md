# Question 19

*UGC NET CS · 2016 July Paper 2 · SQL · DROP TABLE versus DELETE*

Consider the following two commands C1 and C2 on the relation R from an SQL database : C1 : drop table R; C2 : delete from R; Which of the following statements is TRUE ? I. Both C1 and C2 delete the schema for R. II. C2 retains relation R, but deletes all tuples in R. III. C1 deletes not only all tuples of R, but also the schema for R.

- **1.** I only
- **2.** I and II only
- **3.** II and III only
- **4.** I, II and III

> [!TIP]
> **Correct answer: 3. II and III only**

## Solution

DELETE FROM R with no WHERE clause removes every row but leaves relation R's definition available for later use, so statement II is true. DROP TABLE R removes the table object itself—its rows and schema definition—so statement III is true. Statement I is false because DELETE does not delete the schema. Hence II and III only, option 3.

## Key Points

- DELETE removes rows; DROP removes the table definition and its data.

## Why the other options are incorrect

Options 1, 2, and 4 include statement I or omit one of the two true statements. Transaction/rollback details can vary by DBMS, but the central DDL-versus-DML distinction asked here is unchanged.
