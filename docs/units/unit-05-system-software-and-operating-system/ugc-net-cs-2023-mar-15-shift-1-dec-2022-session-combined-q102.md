# Question 102

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · CPU Scheduling · Shortest-remaining-time-first scheduling*

Consider the following set of processes that need to be scheduled on a single CPU. All the times are given in milliseconds. Arrival Time Execution Time Process Name A 5 4 7 10 Using the shortest remaining time first scheduling algorithm, the average process turnaround (in milliseconds) is

- **1.** 7.2
- **2.** 8.2
- **3.** 6
- **4.** 9

> [!TIP]
> **Correct answer: 1. 7.2**

## Solution

SRTF schedule: A runs 0–3; B 3–5 and finishes; A 5–8 finishes (D's arrival at 7 leaves A with 1); C 8–12; E 12–15; D 15–21. Turnarounds are A=8, B=2, C=7, D=14, E=5. Average=(8+2+7+14+5)/5=7.2 ms.

## Key Points

- Turnaround = completion−arrival; SRTF always runs the least remaining arrived job.

## Why the other options are incorrect

The other averages result from ignoring preemption/arrival times or using waiting time instead of turnaround.
