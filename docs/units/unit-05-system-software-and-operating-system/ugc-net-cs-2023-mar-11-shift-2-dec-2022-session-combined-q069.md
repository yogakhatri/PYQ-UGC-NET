# Question 69

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · File and Input/Output Systems · Directory and Disk Structure*

Consider an operating system capable of loading and executing a single sequential user process at a time. The disk head scheduling algorithm used is first come first served (FCFS). If FCFS is replaced by shortest seek time first (SSTF) and the vendor claims 50 % better benchmark results. What is the expected improvement in the I/O performance of user programs?

- **1.** 50%
- **2.** 100%
- **3.** 25%
- **4.** 0%

> [!TIP]
> **Correct answer: 4. 0%**

## Solution

Only one sequential user process can execute. When it issues a synchronous disk request, it blocks until that request completes; there is no second user process generating another outstanding request for the scheduler to choose. With a queue containing at most one request, FCFS and SSTF select exactly the same request. The scheduling replacement therefore gives 0% expected improvement for these user programs.

## Key Points

- A disk scheduling policy can reorder requests only when more than one request is waiting.

## Why the other options are incorrect

The vendor’s 50% benchmark claim depends on workloads with a useful queue of competing requests. Doubling or halving that claim cannot overcome the stated single-sequential-process constraint, so 50%, 100%, and 25% are unsupported.
