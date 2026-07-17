# Question 73

*UGC NET CS · 2013 Dec Paper 3 · Unix Operating System · Process 0, Swapper and Init*

Which statement is not true about process 0 in the Unix operating system?

- **A.** Process 0 is called the init process.
- **B.** Process 0 is not created by the fork system call.
- **C.** After forking process 1, process 0 becomes the swapper process.
- **D.** Process 0 is a special process created when the system boots.

> [!TIP]
> **Correct answer: A. Process 0 is called the init process.**

## Solution

In traditional UNIX boot terminology, process 0 is a special kernel-created process, not a child made by fork. It creates process 1 and then serves as the swapper/scheduler idle process. Process 1, not process 0, is the init process (or the modern init-system equivalent). Therefore statement A is the statement that is not true.

## Key Points

- Traditional UNIX: PID 0=swapper/scheduler; PID 1=init; ordinary processes descend through fork.

## Why the other options are incorrect

B is true because process 0 exists as part of kernel initialization rather than being produced by fork. C expresses its traditional post-boot role as swapper after process 1 is created. D correctly describes it as a special boot-created process.
