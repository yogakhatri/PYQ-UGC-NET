# Question 51

*UGC NET CS · 2014 Dec Paper 3 · File and Input/Output Systems · SSTF Disk Scheduling*

An imaginary disk has 40 cylinders. A request arrives for cylinder 11. While the seek to 11 is in progress, requests arrive for cylinders 1, 36, 16, 34, 9 and 12 in that order. What is the number of arm movements using shortest-seek-first scheduling?

- **A.** 111
- **B.** 112
- **C.** 60
- **D.** 61

> [!TIP]
> **Correct answer: D. 61**

## Solution

Take cylinder 11 as the position after the in-progress request completes. SSTF always chooses the nearest pending cylinder: 11→12 costs 1, 12→9 costs 3, 9→16 costs 7, 16→1 costs 15, 1→34 costs 33, and 34→36 costs 2. Total arm movement is 1+3+7+15+33+2=61 cylinders.

## Key Points

- For SSTF, recompute the nearest unserved request after every service; do not sort the queue just once.

## Why the other options are incorrect

60 misses one cylinder of movement. 111 and 112 come from schedules that do not repeatedly choose the nearest pending request. The crucial step is 9→16 (distance 7) before 9→1 (distance 8), after which the remaining nearest choices determine the total.
