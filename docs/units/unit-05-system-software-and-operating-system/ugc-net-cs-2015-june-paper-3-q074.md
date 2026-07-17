# Question 74

*UGC NET CS · 2015 June Paper 3 · Operating-System Architectures · WOW32 Compatibility Environment*

WOW32 is a :

- **1.** Win 32 API library for creating processes and threads.
- **2.** Special kind of file system to the NT name space.
- **3.** Kernel - mode objects accessible through Win 32 API
- **4.** Special execution environment used to run 16 bit Windows applications on 32 - bit machines.

> [!TIP]
> **Correct answer: 4. Special execution environment used to run 16 bit Windows applications on 32 - bit machines.**

## Solution

WOW32 means Windows on Windows 32. It is the compatibility/execution environment used by 32-bit Windows NT-family systems to run legacy 16-bit Windows applications, coordinating their calls through the appropriate subsystem. Therefore option 4 is correct.

## Key Points

- WOW32 is a legacy 16-on-32 Windows compatibility environment.

## Why the other options are incorrect

WOW32 is not merely a process/thread API library, a filesystem namespace, or a class of kernel-mode object. Those descriptions concern different Windows components.
