# Question 50

*UGC NET CS · 2013 Dec Paper 2 · Linux Operating Systems · Process Management and Scheduling*

Linux operating system uses

- **A.** Affinity Scheduling
- **B.** Fair Preemptive Scheduling
- **C.** Hand Shaking
- **D.** Highest Penalty Ratio Next

> [!TIP]
> **Correct answer: B. Fair Preemptive Scheduling**

## Solution

Modern Linux uses the Completely Fair Scheduler for ordinary tasks. CFS is preemptive and attempts to distribute CPU time fairly by tracking each runnable task's virtual runtime and favoring the task that has received the least weighted CPU service.

## Key Points

- Linux CFS is a fair preemptive scheduler based on weighted virtual runtime.

## Why the other options are incorrect

Processor affinity constrains where a task may run but is not the overall scheduling policy. Handshaking is a synchronization/communication concept. Highest Penalty Ratio Next is a different non-preemptive response-ratio policy, not Linux's general scheduler.
