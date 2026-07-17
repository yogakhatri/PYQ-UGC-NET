# Question 94

*UGC NET CS · 2019 June Paper 1 And 2 · Threads · Shared and private thread resources*

Which resources are not shared by threads of the same process? (a) Stack. (b) Registers. (c) Address space. (d) Message queue.

- **A.** (a) and (d)
- **B.** (b) and (c)
- **C.** (a) and (b)
- **D.** (a), (b) and (c)

> [!TIP]
> **Correct answer: C. (a) and (b)**

## Solution

Every thread needs its own execution state: a private stack for calls and local variables, and a private register set containing values such as the program counter and stack pointer. Threads of one process share the process address space and process-level communication resources. Thus stack and registers, (a) and (b), are not shared.

## Key Points

- Threads share code, data and address space, but each thread owns its registers and stack.

## Why the other options are incorrect

The other combinations incorrectly mark the shared address space or process communication resource as private, or omit one of the two private execution-state components.
