# Question 39

*UGC NET CS · 2010 June Paper 2 · Process Management · Client-Server Communication*

In order to allow only one process to enter its critical section, binary semaphore are initialized to

- **A.** 0
- **B.** 1
- **C.** 2
- **D.** 3

> [!TIP]
> **Correct answer: B. 1**

## Solution

A binary semaphore used as a mutex is initialized to 1, representing one available permit. The first process performs wait and changes it to 0; others then block until the owner signals it back to 1.

## Key Points

- Mutex semaphore: 1 means free, 0 means occupied.

## Why the other options are incorrect

Starting at 0 blocks every process initially, while 2 or 3 would permit multiple entrants and violate mutual exclusion.
