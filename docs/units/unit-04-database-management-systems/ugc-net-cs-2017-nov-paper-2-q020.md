# Question 20

*UGC NET CS · 2017 Nov Paper 2 · SQL · Updating Existing Rows*

__________ SQL command changes one or more fields in a record.

- **1.** LOOK-UP
- **2.** INSERT
- **3.** MODIFY
- **4.** CHANGE

> [!TIP]
> **Correct answer: No valid option: the standard SQL command that changes fields in existing records is UPDATE.**

## Solution

To change one or more column values in an existing row, SQL uses `UPDATE table_name SET column=value WHERE condition`. `INSERT` creates a new row; it does not modify an existing record. None of LOOK-UP, MODIFY, or CHANGE is the standard SQL data-manipulation command requested. Therefore the correct word is `UPDATE`, which is absent from the choices.

## Key Points

- SQL DML: `INSERT` adds rows, `UPDATE` changes existing rows, and `DELETE` removes rows.

## Why the other options are incorrect

Option 2 performs insertion, not modification. `MODIFY` appears in some products as part of schema-alteration syntax for changing a column definition, but that is not the operation described. LOOK-UP and CHANGE are not standard SQL commands for updating row values.

## References

- [PostgreSQL documentation — UPDATE](https://www.postgresql.org/docs/current/sql-update.html)
