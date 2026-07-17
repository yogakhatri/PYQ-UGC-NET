# Question 14

*UGC NET CS · 2011 Dec Paper 3 · Transaction Processing and Concurrency Control · Optimistic Concurrency Control*

What is the basic difference between optimistic concurrency contr ol and other concurrency control technique. Describe the different phases of an optim istic concurrency control scheme. _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________ _______________________________________________________________________________________________


> [!TIP]
> **Correct answer: Optimistic control runs without locks, validates at commit, then writes only if validation succeeds**

## Solution

Locking and timestamp protocols prevent or order conflicts while transactions execute. Optimistic concurrency control instead assumes conflicts are rare. Transactions work on private state without holding long-lived data locks; just before commit, the system checks whether the observed reads and proposed writes can be serialized. A conflicting transaction is restarted rather than having been blocked earlier.

The three phases are:

1. **Read phase:** read database items and perform computation, keeping updates in a private workspace. Record read-set RS(T), write-set WS(T), start time and tentative values.
2. **Validation phase:** assign a validation/serialization position and test the transaction against overlapping transactions. A typical rule requires earlier transactions to have finished before T began, or to have write sets disjoint from T's reads (and, depending on the overlap case, T's writes). If the test fails, abort and restart T.
3. **Write phase:** if validation succeeds, copy the private updates to the database atomically. Read-only transactions need no database write.

OCC avoids lock overhead and deadlock and works well for low-contention, read-heavy or disconnected workloads. Under high contention or long transactions it can waste substantial work through repeated aborts.

## Key Points

- Optimism shifts conflict handling from blocking during execution to read/write-set validation immediately before commit.

## Common mistakes to avoid

Validation after exposing writes is too late. Checking only write-write overlap misses a writer invalidating a value that another transaction read. OCC is not 'no concurrency control'; validation is the mechanism that enforces serializability.
