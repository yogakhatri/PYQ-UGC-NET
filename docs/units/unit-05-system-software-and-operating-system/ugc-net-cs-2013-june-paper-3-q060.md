# Question 60

*UGC NET CS · 2013 June Paper 3 · Process Synchronization and Deadlocks · Circular Wait from Lock Ordering*

Suppose S and Q are two semaphores initialized to 1. P1 and P2 are two processes which are sharing resources. P1 has statements P2 has statements wait(S) ; wait(Q) ; wait(Q) ; wait(S) ; critical- section 1; critical- section 2; signal(S) ; signal(Q) ; signal(Q) ; signal(S) ; Their execution may sometimes lead to an undesirable situation called

- **A.** Starvation
- **B.** Race condition
- **C.** Multithreading
- **D.** Deadlock

> [!TIP]
> **Correct answer: D. Deadlock**

## Solution

P1 acquires S before requesting Q, while P2 acquires Q before requesting S. An interleaving can let P1 hold S and P2 hold Q; P1 then waits for Q and P2 waits for S. Neither can reach its signal operations, creating a circular wait with no progress—a deadlock.

## Key Points

- Acquire multiple locks in one global order; opposite lock orders can create circular wait and deadlock.

## Why the other options are incorrect

Starvation means a process is repeatedly denied service while others continue; here both can become permanently blocked. A race condition is an unsynchronized outcome dependency, but the semaphores do synchronize access—the problem is their opposite acquisition order. Multithreading is an execution model, not the failure shown.
