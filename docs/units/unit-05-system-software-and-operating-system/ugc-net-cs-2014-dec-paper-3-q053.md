# Question 53

*UGC NET CS · 2014 Dec Paper 3 · Process Synchronization · Monitors, Semaphores and Message Passing*

Which statement correctly describes a monitor as a synchronization/IPC technique?

- **A.** It is a higher-level synchronization primitive: procedures, variables, and data structures grouped together in a special package.
- **B.** It is a nonnegative integer that, apart from initialization, is acted upon by wait and signal operations.
- **C.** It uses two primitives, send and receive which are system calls rather than language constructs.
- **D.** It consists of IPC primitives implemented as system calls that block a process when it cannot enter a critical region.

> [!TIP]
> **Correct answer: A. It is a higher-level synchronization primitive: procedures, variables, and data structures grouped together in a special package.**

## Solution

A monitor is a high-level synchronization abstraction that encapsulates shared data with the procedures that operate on it and enforces mutual exclusion for those procedures. Condition variables may additionally let a thread wait and be signaled while preserving the monitor discipline. This matches A's packaged procedures, variables, and data structures.

## Key Points

- Monitor = shared state + operations + automatic mutual exclusion; semaphore = integer with wait/signal; message passing = send/receive.

## Why the other options are incorrect

B defines a semaphore. C describes message passing with send and receive. D describes blocking behavior at a lower system-call level but not the defining encapsulated structure of a monitor. A uniquely identifies the abstraction.
