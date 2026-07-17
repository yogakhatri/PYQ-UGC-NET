# Question 38

*UGC NET CS · 2009 Dec Paper 2 · Distributed Systems · Communication and Protocol Structures*

A semaphore count of negative n means (s = – n) that the queue cont ains ________ waiting processes.

- **A.** n + 1
- **B.** n
- **C.** n – 1
- **D.** 0

> [!TIP]
> **Correct answer: B. n**

## Solution

In the conventional semaphore interpretation, a negative value records how many wait operations could not proceed. If s=−n, its magnitude n is the number of processes blocked in the semaphore's waiting queue.

## Key Points

- For a counting semaphore, a negative magnitude represents queued waiters.

## Why the other options are incorrect

n+1 and n−1 introduce unsupported offsets, and zero would contradict the negative count.
