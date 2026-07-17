# Question 102

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Process Management · Critical-Section Problem*

SToption 10-395031 • No.: 3ID:18705 In design protocol of critical section problem, each process must ask permission to enter critical section in code; it then executes in the critical section; once it finishes executes in the critical section it enters the code. code. The process then enters the

- **1.** entry section, remainder section, exit section
- **2.** entry section, exit section, remainder section
- **3.** remainder section, entry section, exit section
- **4.** remainder section, exit section, entry section

> [!TIP]
> **Correct answer: 2. entry section, exit section, remainder section**

## Solution

A process executes its entry section to obtain permission, then its critical section, then its exit section to release permission, and finally its remainder section. The three requested blanks are therefore entry, exit, remainder.

## Key Points

- Protocol order: entry → critical → exit → remainder.

## Why the other options are incorrect

The other orders perform ordinary remainder work before permission acquisition or postpone release until after the remainder work.
