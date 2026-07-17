# Question 80

*UGC NET CS · 2019 Dec Paper 1 And 2 · CPU Scheduling · Round-Robin Turnaround and Waiting Time*

Using round-robin CPU scheduling with a 2 ms time quantum, find the average turnaround time and average waiting time for the given processes.

- **1.** 4, 0
- **2.** 5.66, 1.66
- **3.** 5.66, 0
- **4.** 7, 2

> [!TIP]
> **Correct answer: 2. 5.66, 1.66**

## Solution

With quantum 2 ms, the schedule is P1:0–2, P2:2–4, P1:4–5, P2:5–7, then P3:7–9, 9–11, and 11–12. Completion times are C1=5, C2=7, C3=12. Turnaround times C−arrival are 5,5,7, averaging 17/3=5.66 ms. Waiting times turnaround−burst are 2,1,2, averaging 5/3=1.66 ms. Therefore option 2.

## Key Points

- For round robin, build the ready-queue timeline first; then turnaround=C−A and waiting=turnaround−burst.

## Why the other options are incorrect

Option 1 ignores most queueing delay. Option 3 incorrectly makes average waiting zero even though P1, P2, and P3 all spend time ready but not running. Option 4 does not match either average obtained from the completion timeline.
