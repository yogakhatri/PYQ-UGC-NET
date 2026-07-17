# Question 50

*UGC NET CS · 2015 June Paper 3 · CPU Scheduling · Multilevel Feedback Queue Scheduling*

Which of the following statements is not true for Multi Level Feedback Queue processor scheduling algorithm ?

- **1.** Queues have different priorities
- **2.** Each queue may have different scheduling algorithm
- **3.** Processes are permanently assigned to a queue
- **4.** This algorithm can be configured to match a specific system under design

> [!TIP]
> **Correct answer: 3. Processes are permanently assigned to a queue**

## Solution

The `feedback` in multilevel feedback queue means a process can move between queues according to its observed behavior, waiting time, or CPU usage. Short interactive jobs tend to stay high; CPU-bound jobs can be demoted, and aging can promote waiting jobs. Therefore processes are not permanently assigned to one queue.

## Key Points

- Multilevel queue fixes membership; multilevel feedback queue allows promotion and demotion.

## Why the other options are incorrect

MLFQ normally uses queues with different priorities, can use different algorithms or time quanta per queue, and is highly configurable. Permanent queue assignment describes an ordinary multilevel queue scheduler, not a feedback queue.
