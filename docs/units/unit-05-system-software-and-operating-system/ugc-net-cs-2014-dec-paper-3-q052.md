# Question 52

*UGC NET CS · 2014 Dec Paper 3 · Deadlocks · Banker's Safety Sequence*

An operating system has 13 tape drives. The maximum requirements of P1, P2, and P3 are 11, 5, and 8 drives; their current allocations are 6, 3, and 2 drives, respectively. Which sequence is safe?

- **A.** P2 P1 P3
- **B.** P2 P3 P1
- **C.** P1 P2 P3
- **D.** P1 P3 P2

> [!TIP]
> **Correct answer: A. P2 P1 P3**

## Solution

The current allocation is 6+3+2=11, leaving 13−11=2 drives available. Remaining needs are P1:11−6=5, P2:5−3=2, and P3:8−2=6. Only P2 can finish with 2 drives; after it releases its 3 allocated drives, available becomes 5. P1 can then finish and release 6, making 11 available, after which P3 can finish. The safe sequence is P2, P1, P3.

## Key Points

- A safe sequence repeatedly finds a process whose remaining need is no more than current available resources, then adds back its allocation.

## Why the other options are incorrect

B tries P3 after P2, but only 5 drives are then available while P3 still needs 6. C and D begin with P1, whose remaining need is 5 when only 2 are available. Only A passes every Banker's safety check.
