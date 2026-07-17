# Question 67

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Linux Operating Systems · Process Management and Scheduling*

S8.10:187017 is invoked. it is passed a set of flags that determine how much In Linux Operating System, when sharing is to take place berween the parent and child tasks.

- **1.** fork0
- **2.** cloneo
- **3.** pthread
- **4.** thread(

> [!TIP]
> **Correct answer: 2. cloneo**

## Solution

Linux uses the clone() system call to create a child task while letting the caller specify sharing behavior through flags. Flags such as CLONE_VM, CLONE_FILES, and CLONE_SIGHAND determine whether the parent and child share address space, file-descriptor tables, signal handlers, and other resources.

## Key Points

- On Linux, clone() is the low-level primitive whose flags control which execution resources are shared.

## Why the other options are incorrect

fork() creates a child with a fixed process-style sharing model and does not take the described sharing flags. pthread() is a user-level threading API commonly implemented using clone(), while thread() is not the Linux system call described.
