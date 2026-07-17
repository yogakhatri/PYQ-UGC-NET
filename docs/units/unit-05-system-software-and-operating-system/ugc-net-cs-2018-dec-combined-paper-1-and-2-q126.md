# Question 126

*UGC NET CS · 2018 Dec Paper 1 And 2 · Process Management · Unix fork System Call*

_____ system call creates a new process in Unix.

- **1.** create
- **2.** create new
- **3.** fork
- **4.** fork new

> [!TIP]
> **Correct answer: 3. fork**

## Solution

In Unix, `fork()` creates a new process by duplicating the calling process. After a successful call, both parent and child continue from the instruction after `fork`; the parent receives the child's positive process ID, the child receives 0, and failure returns -1 to the parent. Therefore option 3 is correct.

## Key Points

- Unix process launch is usually fork-then-exec: `fork()` creates the child; `exec()` loads a new program into an existing process.

## Why the other options are incorrect

`create`, `create new`, and `fork new` are not the Unix process-creation system-call names. A child commonly calls an `exec` function after `fork` to replace its program image, but `exec` does not itself create a second process.
