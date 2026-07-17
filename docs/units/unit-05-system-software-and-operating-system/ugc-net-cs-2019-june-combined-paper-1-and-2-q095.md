# Question 95

*UGC NET CS · 2019 June Paper 1 And 2 · CPU Scheduling · Shortest-remaining-time-first scheduling*

Three CPU-intensive processes require 10, 20 and 30 units of time and arrive at times 0, 2 and 6 respectively. How many context switches are needed under shortest-remaining-time-first scheduling? Do not count switches at time zero or at the end.

- **1.** 4
- **2.** 2
- **3.** 3
- **4.** 1

> [!TIP]
> **Correct answer: 2. 2**

## Solution

Process P1 starts at time 0. At time 2 it has 8 units left, less than P2's 20, so it continues. At time 6 it has 4 units left, less than P3's 30, so it again continues and finishes at time 10. The CPU then switches to P2, and after P2 finishes it switches to P3. Excluding the initial dispatch and the final transition to idle, there are two context switches.

## Key Points

- SRTF preempts only when a newly arrived process has less remaining time than the running process.

## Why the other options are incorrect

Options 1, 3 and 4 assume unnecessary preemptions at arrival times or count the initial/final dispatches that the question explicitly excludes.
