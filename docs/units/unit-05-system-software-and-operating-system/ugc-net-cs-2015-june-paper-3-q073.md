# Question 73

*UGC NET CS · 2015 June Paper 3 · Unix Process Management · exec, brk, wait, and fork System Calls*

Match the following for unix system calls : List - I List - II (a) exec (i) Creates a new process (b) brk (ii) Invokes another program overlaying memory space with a copy of an executable file (c) wait (iii) To increase or decrease the size of data region (d) fork (iv) A process synchronizes with termination of child process Codes : (a) (b) (c) (d)

- **1.** (ii) (iii) (iv) (i)
- **2.** (iii) (ii) (iv) (i)
- **3.** (iv) (iii) (ii) (i)
- **4.** (iv) (iii) (i) (ii)

> [!TIP]
> **Correct answer: 1. (ii) (iii) (iv) (i)**

## Solution

`exec` replaces the current process image with an executable: (a)–(ii). `brk` changes the end of the data segment and thus its size: (b)–(iii). `wait` lets a parent synchronize with and collect a terminated child: (c)–(iv). `fork` creates a new child process: (d)–(i). The sequence is `(ii),(iii),(iv),(i)`.

## Key Points

- Classic Unix lifecycle: fork a child, exec a program, wait for termination; brk adjusts the data region.

## Why the other options are incorrect

The other codes swap process creation, image replacement, memory-region adjustment, or child synchronization. Remember the Unix pattern: `fork` creates, `exec` replaces, and `wait` reaps.
