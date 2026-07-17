# Question 49

*UGC NET CS · 2016 July Paper 3 · Unix Process Management · Process Termination, wait, and Zombie Processes*

In UNIX, processes that have finished execution but have not yet had their status collected are known as _________.

- **1.** Sleeping processes
- **2.** Stopped processes
- **3.** Zombie processes
- **4.** Orphan processes

> [!TIP]
> **Correct answer: 3. Zombie processes**

## Solution

When a child exits, the kernel keeps a small process-table record containing its PID and termination status so that its parent can collect that status with wait() or waitpid(). The child has finished executing but this record has not yet been reaped; such a process is called a zombie. Therefore option 3 is correct.

## Key Points

- Zombie = dead child awaiting wait(); orphan = live child whose parent has died.

## Why the other options are incorrect

A sleeping process is alive but waiting for an event. A stopped process is suspended and can continue later. An orphan is a still-running child whose parent has terminated; it is adopted by a system reaper. None of these means 'finished but not yet waited for.'
