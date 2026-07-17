# Question 16

*UGC NET CS · 2015 June Paper 2 · Database Languages and SQL · Assertions and Database-Wide Constraints*

An Assertion is a predicate expressing a condition we wish database to always satisfy. The correct syntax for Assertion is :

- **1.** CREATE ASSERTION Assertion_Name CHECK (Predicate)
- **2.** CREATE ASSERTION Assertion_Name
- **3.** CREATE ASSERTION, CHECK Predicate
- **4.** SELECT ASSERTION

> [!TIP]
> **Correct answer: 1. CREATE ASSERTION Assertion_Name CHECK (Predicate)**

## Solution

An SQL assertion is a named, database-wide integrity constraint. Its standard form is `CREATE ASSERTION assertion_name CHECK (search_condition);`. The condition may involve several tables and must remain true after every relevant database update. Therefore option 1 contains the required sequence: `CREATE ASSERTION`, a constraint name, and a `CHECK` predicate.

## Key Points

- Use `CREATE ASSERTION name CHECK (condition)` for a named database-wide constraint.

## Why the other options are incorrect

Option 2 supplies no condition to enforce. Option 3 omits the assertion name and is not valid SQL syntax. Option 4 uses `SELECT`, which retrieves data rather than declaring an integrity constraint.
