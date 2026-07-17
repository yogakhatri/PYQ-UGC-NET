# Question 58

*UGC NET CS · 2013 June Paper 3 · CPU Scheduling · Round-Robin Turnaround Time*

Consider the following processes with time slice of 4 milliseconds (I/O requests are ignored) : Process A B C D Arrival time 0 1 2 3 CPU cycle 8 4 9 5 The average turn around time of these processes will be

- **A.** 19.25 milliseconds
- **B.** 18.25 milliseconds
- **C.** 19.5 milliseconds
- **D.** 18.5 milliseconds

> [!TIP]
> **Correct answer: B. 18.25 milliseconds**

## Solution

With quantum 4, the round-robin timeline is A:0–4, B:4–8, C:8–12, D:12–16, A:16–20, C:20–24, D:24–25, C:25–26. Completion times are A=20, B=8, C=26 and D=25. Subtracting arrivals gives turnaround times 20, 7, 24 and 22 ms. Their average is (20+7+24+22)/4 = 73/4 = 18.25 ms.

## Key Points

- Turnaround time = completion time − arrival time; first build the exact round-robin timeline.

## Why the other options are incorrect

The other numerical choices result from ignoring arrival times, using completion time directly for every process, or reordering the ready queue incorrectly after a quantum. Round robin appends an unfinished process behind all processes already waiting.
