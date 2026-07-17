# Question 50

*UGC NET CS · 2016 July Paper 3 · Unix Process Management · fork and Address-Space Sharing*

In Unix operating system, when a process creates a new process using the fork () system call, which of the following state is shared between the parent process and child process ?

- **1.** Heap
- **2.** Stack
- **3.** Shared memory segments
- **4.** Both Heap and Stack

> [!TIP]
> **Correct answer: 3. Shared memory segments**

## Solution

After fork(), the child receives its own virtual address space initialized from the parent's address space. Heap and stack pages may initially use copy-on-write for efficiency, but logically they are private: a later write in one process is not a write to the other's heap or stack. In contrast, an attached shared-memory segment remains mapped as shared in both processes, so option 3 is correct.

## Key Points

- fork duplicates private process memory logically; explicitly shared-memory mappings remain shared.

## Why the other options are incorrect

Calling copy-on-write heap or stack pages 'shared state' confuses a physical-memory optimization with process semantics. Both processes may temporarily map the same physical page, but a write creates a private copy. Therefore heap, stack, and 'both heap and stack' are not the requested answer.
