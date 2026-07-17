# Question 29

*UGC NET CS · 2012 June Paper 2 · CPU Scheduling · Pre-emptive Scheduling*

Pre-emptive scheduling is the strategy of temporarily suspending a running process:

- **A.** before the CPU time slice expires
- **B.** to allow starving processes to run
- **C.** when it requests I/O
- **D.** to avoid collision

> [!TIP]
> **Correct answer: A. before the CPU time slice expires**

## Solution

A pre-emptive scheduler can take the CPU from a running process before that process voluntarily blocks or completes its allowed execution interval, for example when a higher-priority process becomes ready. The saved context lets the suspended process resume later. Option A best expresses this early forced suspension.

## Key Points

- Pre-emption is involuntary CPU revocation while a process is still runnable.

## Why the other options are incorrect

Helping a starving process can be one policy reason but is not the definition. A process that requests I/O blocks voluntarily. Collision avoidance is unrelated to CPU scheduling.
