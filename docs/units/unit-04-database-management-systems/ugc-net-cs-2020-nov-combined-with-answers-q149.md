# Question 149

*UGC NET CS · 2020 Nov With Answers · SQL · ALTER TABLE and DROP COLUMN*

Which query or queries will drop the SALARY column from the EMPLOYEE table? A. ALTER TABLE EMPLOYEE DROP SALARY CASCADE; B. ALTER TABLE EMPLOYEE DROP SALARY RESTRICT; C. ALTER EMPLOYEE DROP SALARY.

- **1.** A and B only
- **2.** A and C only
- **3.** B and C only
- **4.** A only

> [!TIP]
> **Correct answer: 1. A and B only**

## Solution

In the SQL form used by the question, ALTER TABLE EMPLOYEE DROP SALARY may be followed by CASCADE or RESTRICT. CASCADE removes dependent schema objects along with the column; RESTRICT permits the drop only when no dependent object blocks it. No dependency on SALARY is specified, so both A and B are valid column-drop statements. C is syntactically invalid because ALTER must be followed by TABLE. Therefore A and B only, option 1.

## Key Points

- DDL syntax begins ALTER TABLE; CASCADE and RESTRICT specify what happens when other schema objects depend on the dropped column.

## Why the other options are incorrect

Options 2 and 3 include invalid statement C. Option 4 excludes the valid RESTRICT form. CASCADE and RESTRICT change dependency handling, not the fact that the command is a column drop.
