# Question 71

*UGC NET CS · 2013 Dec Paper 3 · Deadlocks · Recovery by Process Termination*

Simplest way of deadlock recovery is

- **A.** Roll back
- **B.** Preempt resource
- **C.** Lock one of the processes
- **D.** Kill one of the processes

> [!TIP]
> **Correct answer: D. Kill one of the processes**

## Solution

The most direct way to break a deadlock cycle is to terminate one participating process. Its resources are released, allowing other blocked processes to proceed. A real recovery policy must choose a victim carefully and may need to terminate additional processes if one termination does not remove every cycle, but the mechanism itself is simple.

## Key Points

- Deadlock recovery can break the wait-for cycle by terminating a victim process and releasing its resources.

## Why the other options are incorrect

Rollback needs checkpoints and restoration logic. Resource preemption must identify a safe preemptible resource and handle rollback/starvation. Locking another process cannot release the resources forming the deadlock and can make blocking worse.
