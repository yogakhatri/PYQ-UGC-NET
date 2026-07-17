# Question 62

*UGC NET CS · 2013 June Paper 3 · Processes and Threads · Mode Switch versus Context Switch*

Let the time taken to switch between user mode and kernel mode of execution be T1 while time taken to switch between two user processes be T2. Which of the following is correct ?

- **A.** T1 < T2
- **B.** T1 > T2
- **C.** T1 = T2
- **D.** Nothing can be said about the relation between T1 and T2.

> [!TIP]
> **Correct answer: A. T1 < T2**

## Solution

A user-to-kernel mode switch normally continues executing on behalf of the same process; it changes privilege level and transfers control to kernel code but does not replace the whole running process. A switch between user processes must save one process's CPU context, choose another runnable process, restore its context and often disturb caches or address-translation state. Therefore the usual cost relation is T1<T2.

## Key Points

- A mode switch changes privilege within one execution context; a process switch changes the execution context itself.

## Why the other options are incorrect

T1>T2 contradicts the extra scheduling and context-management work in a process switch. Equality is not generally expected because the operations differ. Although exact timings depend on hardware and OS design, the standard architectural comparison is sufficiently clear to reject 'nothing can be said.'
