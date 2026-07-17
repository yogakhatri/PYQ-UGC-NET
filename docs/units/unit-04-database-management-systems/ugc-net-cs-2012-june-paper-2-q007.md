# Question 7

*UGC NET CS · 2012 June Paper 2 · Transaction Processing and Concurrency Control · Record Locking*

In multiuser database if two users wish to update the same record at the same time, they are prevented from doing so by

- **A.** Jamming
- **B.** Password
- **C.** Documentation
- **D.** Record lock

> [!TIP]
> **Correct answer: D. Record lock**

## Solution

A record lock grants one transaction exclusive update access to a record while other transactions wait or fail according to policy. This prevents lost updates and inconsistent interleavings when two users try to modify the same row simultaneously. The lock is released at commit or rollback under the transaction protocol.

## Key Points

- Concurrency control uses locks to serialize conflicting access to the same data item.

## Why the other options are incorrect

A password authenticates or authorizes a user but does not serialize simultaneous updates. Documentation has no runtime enforcement role. Jamming is unrelated to database concurrency.
