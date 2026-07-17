# Question 36

*UGC NET CS · 2015 June Paper 2 · File and Input/Output Systems · SSTF Disk Scheduling*

A disk drive has 100 cylinders, numbered 0 to 99. Disk requests arrive for cylinders 12, 26, 24, 4, 42, 8, and 50, in that order. The driver is currently serving a request at cylinder 24. A seek takes 6 ms per cylinder moved. How much seek time is needed using shortest seek time first (SSTF)?

- **1.** 0.984 sec
- **2.** 0.396 sec
- **3.** 0.738 sec
- **4.** 0.42 sec

> [!TIP]
> **Correct answer: 4. 0.42 sec**

## Solution

Start at cylinder 24. SSTF always chooses the pending request nearest the current head: `24 → 26` costs 2 cylinders, `26 → 12` costs 14, `12 → 8` costs 4, `8 → 4` costs 4, `4 → 42` costs 38, and `42 → 50` costs 8. Total head movement is `2 + 14 + 4 + 4 + 38 + 8 = 70` cylinders. At 6 ms per cylinder, seek time is `70 × 6 = 420 ms = 0.42 s`.

## Key Points

- For SSTF, repeatedly choose the closest pending cylinder; here 70 cylinders × 6 ms = 0.42 s.

## Why the other options are incorrect

The other times correspond to different or incorrectly accumulated head movements. SSTF must be recalculated after every service; it does not simply preserve arrival order or continue in one fixed direction.
