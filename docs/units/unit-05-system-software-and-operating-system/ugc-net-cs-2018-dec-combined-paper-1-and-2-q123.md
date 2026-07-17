# Question 123

*UGC NET CS · 2018 Dec Paper 1 And 2 · CPU Scheduling · Round-Robin Waiting Time*

Consider the following set of processes and CPU burst times in milliseconds: P1 = 5, P2 = 7, P3 = 6, P4 = 4. Assume that the processes are scheduled with the Round-Robin scheduling algorithm using a time quantum of 4 ms. The waiting time for P4 is ____ ms.

- **1.** 0
- **2.** 4
- **3.** 12
- **4.** 6

> [!TIP]
> **Correct answer: 3. 12**

## Solution

Assuming all four processes are ready initially in the listed order, the first Round-Robin cycle with quantum 4 is P1 from 0–4, P2 from 4–8, P3 from 8–12, and P4 from 12–16. P4 needs exactly 4 ms, so it completes in that first turn. It spent the interval 0–12 waiting in the ready queue, giving a waiting time of 12 ms, option 3.

## Key Points

- Draw the Round-Robin Gantt chart; a process whose burst equals one quantum has waiting time equal to the start of its only slice when all arrive at time 0.

## Why the other options are incorrect

0 would apply only if P4 ran first. Values 4 and 6 do not include the three complete four-millisecond slices used by P1, P2, and P3 before P4's first turn. Since P4 completes in one quantum, no later waiting interval must be added.
