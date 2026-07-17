# Question 39

*UGC NET CS · 2017 Jan Paper 2 · CPU Scheduling · Aging and Starvation*

Which of the following scheduling algorithms may cause starvation ? a. First-come-first-served b. Round Robin c. Priority d. Shortest process next e. Shortest remaining time first

- **1.** a, c and e
- **2.** c, d and e
- **3.** b, d and e
- **4.** b, c and d

> [!TIP]
> **Correct answer: 2. c, d and e**

## Solution

Priority scheduling can indefinitely postpone low-priority jobs if higher-priority work keeps arriving. Shortest-process-next can indefinitely postpone a long job when short jobs keep arriving, and its preemptive version, shortest-remaining-time-first, has the same risk. FCFS serves jobs in arrival order, and Round Robin repeatedly gives each ready job a time slice, so neither normally starves a continuously ready process. Thus c,d,e—option 2—may cause starvation.

## Key Points

- A policy can starve jobs when a continuing stream of 'better' jobs—higher priority or shorter—can always overtake them.

## Why the other options are incorrect

Options 1, 3, and 4 include FCFS or Round Robin, which provide eventual service under the standard assumptions, or omit one of the size/priority-biased schedulers that can postpone a job indefinitely.
