# Question 9

*UGC NET CS · 2012 June Paper 2 · Database Languages and Interfaces · xBase Record Deletion Commands*

What deletes the entire file except the file structure ?

- **A.** ERASE
- **B.** DELETE
- **C.** ZAP
- **D.** PACK

> [!TIP]
> **Correct answer: C. ZAP**

## Solution

In dBASE/xBase terminology, ZAP physically removes every record from the currently open table while retaining the table definition/DBF structure for reuse. It is effectively a fast 'remove all rows' operation and normally requires exclusive access.

## Key Points

- DELETE marks rows, PACK removes marked rows, ZAP removes all rows but preserves the table structure.

## Why the other options are incorrect

ERASE removes a file itself. DELETE usually marks selected records as deleted rather than immediately removing all of them. PACK physically removes records that were previously marked for deletion; it is not the direct all-record command.
