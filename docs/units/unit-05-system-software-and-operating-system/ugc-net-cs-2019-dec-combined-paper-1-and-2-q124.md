# Question 124

*UGC NET CS · 2019 Dec Paper 1 And 2 · CPU Scheduling · Preemptive Scheduling Decision Points*

In which circumstances can preemptive CPU scheduling be invoked? (a) A process moves Running→Ready. (b) A process moves Waiting→Ready. (c) A process completes. (d) A process moves Ready→Waiting.

- **1.** (a) and (b) only
- **2.** (a) and (d) only
- **3.** (c) and (d) only
- **4.** (a), (b) and (c) only

> [!TIP]
> **Correct answer: 1. (a) and (b) only**

## Solution

Running→Ready in (a) is preemption itself, commonly caused by a timer expiry or a higher-priority event. Waiting→Ready in (b) can make a newly ready higher-priority process preempt the current runner. Completion in (c) releases the CPU voluntarily and needs a scheduling decision but not preemption. Ready→Waiting in (d) is not a normal direct process transition; a process must be running before it can block. Thus only (a) and (b) identify preemptive circumstances, option 1.

## Key Points

- Preemptive scheduling matters when a running process is forced back to Ready or when a newly Ready process may displace it.

## Why the other options are incorrect

Options 2 and 3 include the invalid Ready→Waiting transition. Option 4 includes process completion, where no running process is forcibly displaced. Preemption specifically means taking the CPU from a still-runnable process.
