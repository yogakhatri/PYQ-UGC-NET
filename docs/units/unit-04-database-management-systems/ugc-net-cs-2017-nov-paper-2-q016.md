# Question 16

*UGC NET CS · 2017 Nov Paper 2 · SQL · Views and Virtual Tables*

Which of the following is/are true with reference to ‘view’ in DBMS ? (a) A ‘view’ is a special stored procedure executed when certain event occurs. (b) A ‘view’ is a virtual table, which occurs after executing a pre-compiled query.

- **1.** Only (a) is true
- **2.** Only (b) is true
- **3.** Both (a) and (b) are true
- **4.** Neither (a) nor (b) are true

> [!TIP]
> **Correct answer: 2. Only (b) is true**

## Solution

Statement (a) describes a database trigger: code that runs automatically when a specified event occurs. A view is instead a named query presented to users as a virtual table. Its rows are obtained by evaluating the view's stored query rather than being an independently stored base table in the ordinary case. Thus (a) is false and (b) expresses the intended idea, so option 2 is correct.

## Key Points

- View = virtual table defined by a query; trigger = event-driven database action; stored procedure = explicitly invocable program unit.

## Why the other options are incorrect

Options 1 and 3 wrongly call a view an event-driven stored procedure. Option 4 rejects the valid virtual-table description. The phrase 'pre-compiled query' is implementation-oriented; the essential definition is a virtual table derived from a stored query.
