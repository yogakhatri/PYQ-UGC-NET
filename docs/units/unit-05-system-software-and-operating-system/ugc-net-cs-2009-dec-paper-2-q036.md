# Question 36

*UGC NET CS · 2009 Dec Paper 2 · Process Management · Client-Server Communication*

In the process management Round-robin method is essentially the pre -emptive version of _________

- **A.** FILO
- **B.** FIFO
- **C.** SSF
- **D.** Longest time first

> [!TIP]
> **Correct answer: B. FIFO**

## Solution

Round-robin keeps ready processes in FIFO order, but adds a time quantum: when a running process exhausts its quantum, it is preempted and placed at the rear. It is therefore the preemptive form of FIFO/FCFS scheduling.

## Key Points

- Round-robin = FIFO rotation plus timer-driven preemption.

## Why the other options are incorrect

FILO, shortest-seek-first, and longest-time-first do not describe the circular ready-queue discipline.
