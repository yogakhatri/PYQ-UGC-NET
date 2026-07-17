# Question 40

*UGC NET CS · 2017 Nov Paper 2 · Process Synchronization · Atomic Semaphore Operations*

Two atomic operations permissible on Semaphores are __________ and __________.

- **1.** wait, stop
- **2.** wait, hold
- **3.** hold, signal
- **4.** wait, signal

> [!TIP]
> **Correct answer: 4. wait, signal**

## Solution

A semaphore exposes two atomic operations: `wait` (also P/down), which decrements or blocks when the resource is unavailable, and `signal` (also V/up), which increments and may wake a blocked process. Thus option 4 is correct.

## Key Points

- Semaphore primitives are wait/P/down and signal/V/up, executed atomically to coordinate concurrent processes.

## Why the other options are incorrect

`stop` and `hold` are not the conventional primitive semaphore operations, so options 1–3 each contain at least one invalid term. Atomicity is essential so two processes cannot interleave updates and corrupt the semaphore state.
