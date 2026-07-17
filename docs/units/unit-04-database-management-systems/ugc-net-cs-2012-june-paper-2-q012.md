# Question 12

*UGC NET CS · 2012 June Paper 2 · Transaction Processing and Concurrency Control · Transaction Manager*

A Transaction Manager is which of the following ?

- **A.** Maintains a log of transactions
- **B.** Maintains before and after database images
- **C.** Maintains appropriate concurrency control
- **D.** All of the above

> [!TIP]
> **Correct answer: D. All of the above**

## Solution

In the broad architecture assumed by the question, the transaction manager coordinates transaction execution and recovery. It maintains or works with the transaction log, records before/after information needed for undo and redo, and applies concurrency-control rules so simultaneous transactions preserve isolation and consistency. Therefore all three listed responsibilities are included.

## Key Points

- Transaction management combines concurrency control with logging and recovery information.

## Why the other options are incorrect

Options A-C each name only one required aspect. Some DBMS descriptions split these duties among a scheduler/concurrency manager and recovery manager, but together they form the transaction-management subsystem meant here.
