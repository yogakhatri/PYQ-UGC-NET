# Question 125

*UGC NET CS · 2018 Dec Paper 1 And 2 · Process Management · Ready and Waiting Queues*

A process residing in main memory and ready and waiting for execution is kept on:

- **1.** Execution Queue
- **2.** Job Queue
- **3.** Ready Queue
- **4.** Wait Queue

> [!TIP]
> **Correct answer: 3. Ready Queue**

## Solution

A process that is resident in main memory, has everything needed to run, and is waiting only for CPU time is in the ready state. The scheduler keeps such processes in the ready queue and selects one for dispatch. Hence option 3 is correct.

## Key Points

- Ready queue = in memory and runnable, waiting for CPU; wait queue = blocked for an event; job queue = awaiting admission or all submitted jobs.

## Why the other options are incorrect

A job queue broadly includes submitted processes and may include jobs not yet admitted to memory. A wait/device queue contains processes blocked for an event or I/O, so they are not ready to execute. ‘Execution queue’ is not the standard queue for ready-but-not-running processes.
