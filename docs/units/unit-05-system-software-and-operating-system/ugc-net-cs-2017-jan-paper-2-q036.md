# Question 36

*UGC NET CS · 2017 Jan Paper 2 · Process Synchronization · Semaphore Values and Waiting Processes*

There are three processes P1, P2 and P3 sharing a semaphore for synchronizing a variable. Initial value of semaphore is one. Assume that negative value of semaphore tells us how many processes are waiting in queue. Processes access the semaphore in following order : (a) P2 needs to access (b) P1 needs to access (c) P3 needs to access (d) P2 exits critical section (e) P1 exits critical section The final value of semaphore will be :

- **1.** 0
- **2.** 1
- **3.** –1
- **4.** −2

> [!TIP]
> **Correct answer: 1. 0**

## Solution

Start at semaphore value 1. P2 performs wait: 1→0 and enters. P1 performs wait: 0→−1 and blocks. P3 performs wait: −1→−2 and blocks. When P2 exits it performs signal: −2→−1 and wakes one waiter, P1. When P1 later exits, signal changes −1→0 and wakes P3. The final semaphore value is 0, option 1.

## Key Points

- With the stated convention, wait decrements first and a negative value counts waiters; signal increments and wakes one waiter when needed.

## Why the other options are incorrect

A final value 1 would mean the critical section is free with nobody admitted, but P3 has just been awakened/admitted. Values −1 or −2 would mean one or two processes remain queued, whereas both signals have removed the two waiters from the queue.
