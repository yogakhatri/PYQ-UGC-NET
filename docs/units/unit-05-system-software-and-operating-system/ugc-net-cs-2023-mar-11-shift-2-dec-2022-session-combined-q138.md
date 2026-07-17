# Question 138

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · CPU Scheduling · Round-robin maximum waiting time*

atoption 10-30471 l. No.8 BID:187081 An OS follows round-robin scheduling with time quantum of 4ms. Assuming that the CPU is free now and there are 20 processes waiting in the ready queue, the maximum amount of time that a process waits before getting into the CPU is

- **1.** 80ms
- **2.** 76ms
- **3.** 84ms
- **4.** None of the above

> [!TIP]
> **Correct answer: 2. 76ms**

## Solution

A process at the back of a queue of 20 waits while the other 19 processes each receive one 4 ms quantum. Maximum wait before its first CPU turn is 19×4=76 ms, ignoring context-switch overhead as the question does.

## Key Points

- Initial round-robin wait with N ready processes is at most (N−1)q.

## Why the other options are incorrect

80 ms counts the waiting process's own quantum; 84 ms adds an extra quantum.
