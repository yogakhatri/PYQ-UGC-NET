# Question 53

*UGC NET CS · 2017 Jan Paper 3 · Process Management · User-Level versus Kernel-Level Threads*

One of the disadvantages of user level threads compared to Kernel level threads is

- **1.** If a user level thread of a process executes a system call, all threads in that process are blocked.
- **2.** Scheduling is application dependent.
- **3.** Thread switching doesn’t require kernel mode privileges.
- **4.** The library procedures invoked for thread management in user level threads are local procedures.

> [!TIP]
> **Correct answer: 1. If a user level thread of a process executes a system call, all threads in that process are blocked.**

## Solution

In a many-to-one user-level threading model, the kernel sees only one schedulable entity for the process. If one user thread makes a blocking system call, the kernel blocks that entity, so every user thread in the process stops even if another could run. This is a major disadvantage compared with separately kernel-managed threads, so option 1 is correct.

## Key Points

- Kernel-unaware user threads are cheap to manage, but one blocking kernel operation can block the entire process.

## Why the other options are incorrect

Application-controlled scheduling can be tailored to the program, while switching without kernel privilege and using local library calls are performance advantages of user-level threads. They reduce overhead rather than cause the blocking defect asked for.
