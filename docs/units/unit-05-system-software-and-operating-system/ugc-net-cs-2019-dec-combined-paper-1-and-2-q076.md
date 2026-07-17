# Question 76

*UGC NET CS · 2019 Dec Paper 1 And 2 · CPU Scheduling · Criteria and Algorithms*

Which of the following CPU scheduling algorithms is/are supported by LINUX operating system?

- **1.** Non-preemptive priority scheduling
- **2.** Preemptive priority scheduling and time sharing CPU scheduling
- **3.** Time sharing scheduling only
- **4.** Priority scheduling only

> [!TIP]
> **Correct answer: 2. Preemptive priority scheduling and time sharing CPU scheduling**

## Solution

Linux supports preemptive scheduling: a runnable higher-priority task can preempt another task. It also supports time sharing for ordinary tasks, distributing CPU time among runnable processes. Hence the combined description in option 2 is correct.

## Key Points

- Linux combines preemptive priority handling with time-shared scheduling classes for ordinary workloads.

## Why the other options are incorrect

Option 1 incorrectly characterizes Linux priority scheduling as only non-preemptive. Options 3 and 4 each mention only one of the supported scheduling behaviours and therefore omit the other.
