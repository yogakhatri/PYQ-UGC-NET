# Question 17

*UGC NET CS · 2015 June Paper 2 · Transaction Processing and Concurrency Control · Two-Phase Locking and Timestamp Ordering*

Which of the following concurrency protocols ensures both conflict serializability and freedom from deadlock? (a) Two-phase locking (b) Timestamp ordering

- **1.** Both (a) and (b)
- **2.** (a) only
- **3.** (b) only
- **4.** Neither (a) nor (b)

> [!TIP]
> **Correct answer: 3. (b) only**

## Solution

Basic timestamp ordering assigns each transaction a timestamp and orders conflicting reads and writes by those timestamps. A transaction whose operation violates the required order is rolled back instead of waiting for another lock. The timestamp order makes the schedule conflict-serializable, and the absence of lock waiting prevents a wait-for cycle; hence it is deadlock-free. Statement (b) alone has both properties.

## Key Points

- 2PL gives serializability but may deadlock; basic timestamp ordering gives serializability without lock deadlocks.

## Why the other options are incorrect

Two-phase locking guarantees conflict serializability because each transaction has a growing lock phase followed by a shrinking phase, but transactions can wait for one another in a cycle and deadlock. Thus (a) is not deadlock-free, eliminating options 1 and 2; option 4 incorrectly rejects timestamp ordering.
