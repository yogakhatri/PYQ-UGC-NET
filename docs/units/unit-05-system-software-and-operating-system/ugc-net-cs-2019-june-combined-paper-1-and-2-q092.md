# Question 92

*UGC NET CS · 2019 June Paper 1 And 2 · Basics of Operating Systems · Operating-system abstractions*

Match List I with List II. List I: (a) Disk; (b) CPU; (c) Memory; (d) Interrupt. List II: (i) Thread; (ii) Signal; (iii) File system; (iv) Virtual address space.

- **1.** a-i, b-ii, c-iii, d-iv
- **2.** a-iii, b-i, c-iv, d-ii
- **3.** a-ii, b-i, c-iv, d-iii
- **4.** a-ii, b-iv, c-iii, d-i

> [!TIP]
> **Correct answer: 2. a-iii, b-i, c-iv, d-ii**

## Solution

A disk is organized and exposed through a file system. The CPU schedules and executes threads. Memory is represented to a process through its virtual address space. An interrupt is delivered to software in a signal-like form. The matching is therefore disk-file system, CPU-thread, memory-virtual address space and interrupt-signal: a-iii, b-i, c-iv, d-ii.

## Key Points

- Operating systems present hardware through abstractions: disks as files, CPU work as threads, memory as address spaces and events as signals.

## Why the other options are incorrect

Options 1, 3 and 4 associate at least one hardware resource with an unrelated abstraction, such as a disk with a thread or an interrupt with a file system.
