# Question 98

*UGC NET CS · 2019 June Paper 1 And 2 · Deadlocks · Deadlock-free resource bounds*

A computer has six tape drives with n processes competing for them. Each process may need two drives. What is the maximum value of n for the system to be deadlock free?

- **1.** 5
- **2.** 4
- **3.** 3
- **4.** 6

> [!TIP]
> **Correct answer: 1. 5**

## Solution

For n processes, each needing at most k=2 identical drives, deadlock is impossible if the six drives can give every process k-1=1 drive and still leave one drive to let some process finish. Thus 6≥n(2-1)+1, so n≤5. With five processes, after one drive is held by each process, one drive remains to complete one process and release its drives.

## Key Points

- For m identical resources and maximum claim k, n processes are guaranteed deadlock-free when m≥n(k-1)+1.

## Why the other options are incorrect

Values 3 and 4 are safe but are not the maximum. With 6 processes, all six can hold one drive and wait forever for a second, creating deadlock.
