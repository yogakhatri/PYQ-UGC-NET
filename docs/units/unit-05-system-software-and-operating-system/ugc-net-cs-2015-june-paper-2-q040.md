# Question 40

*UGC NET CS · 2015 June Paper 2 · Unix Process Management · Process Table and User Area*

The Unix Kernel maintains two key data structures related to processes, the process table and the user structure. Which of the following information is not the part of user structure ?

- **1.** File descriptor table
- **2.** System call state
- **3.** Scheduling parameters
- **4.** Kernel stack

> [!TIP]
> **Correct answer: 3. Scheduling parameters**

## Solution

In the classic Unix organization assumed here, the user area stores information needed while the process is executing, including its open-file descriptor table, current system-call state, and kernel stack. Scheduling information such as priority, CPU usage, and runnable state must remain available to the scheduler even when the process is not currently running, so it belongs to the resident process/thread table rather than the user structure.

## Key Points

- Always-resident scheduling state goes in the process table; execution-specific state and the kernel stack go in the classic user area.

## Why the other options are incorrect

Options 1, 2, and 4 are characteristic user-area contents in the textbook Unix model. Modern Unix-like kernels organize these fields differently, but the question explicitly contrasts the classic process table with the user structure; under that model only scheduling parameters are excluded.
