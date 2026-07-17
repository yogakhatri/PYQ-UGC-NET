# Question 65

*UGC NET CS · 2013 June Paper 3 · Processes and Threads · Per-Thread versus Per-Process State*

A thread is usually defined as a light weight process because an Operating System (OS) maintains smaller data structure for a thread than for a process. In relation to this, which of the following statement is correct ?

- **A.** OS maintains only scheduling and accounting information for each thread.
- **B.** OS maintains only CPU registers for each thread.
- **C.** OS does not maintain a separate stack for each thread.
- **D.** OS does not maintain virtual memory state for each thread.

> [!TIP]
> **Correct answer: D. OS does not maintain virtual memory state for each thread.**

## Solution

Threads in one process share the process's address space and therefore its virtual-memory mappings. The OS does not need a separate virtual-memory state for every thread. Each thread still needs its own program counter/register context, scheduling information and stack so that calls, local variables and execution position remain independent.

## Key Points

- Per thread: registers, stack and scheduling state; per process: address space and resources shared by its threads.

## Why the other options are incorrect

A and B say 'only' and omit other essential per-thread state. C is false because each thread requires a separate stack. D correctly identifies major state shared at process level rather than duplicated per thread.
