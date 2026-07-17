# Question 46

*UGC NET CS · 2013 Dec Paper 2 · CPU Scheduling · Dynamic Priority Scheduling*

Consider a preemptive priority based scheduling algorithm based on dynamically changing priority. Larger priority number implies higher priority. When the process is waiting for CPU in the ready queue (but not yet started execution), its priority changes at a rate a = 2. When it starts running, its priority changes at a rate b = 1. A ll the processes are assigned priority value 0 when they enter ready queue. Assume that the following processes want to execute : Process ID Arrival Time Service Time P1 0 4 P2 1 1 P3 2 2 P4 3 1 The time quantum q = 1. When two processes want to join ready queue simultaneously, the process which has not executed recently is given priority. The finish time of processes P1, P2, P3 and P4 will respectively be

- **A.** 4, 5, 7 and 8
- **B.** 8, 2, 7 and 5
- **C.** 2, 5, 7 and 8
- **D.** 8, 2, 5 and 7

> [!TIP]
> **Correct answer: B. 8, 2, 7 and 5**

## Solution

At each one-unit quantum, a process returning to the ready queue competes with new and waiting processes; waiting priority grows faster (rate 2) than running priority (rate 1), and ties favor the least recently executed. The resulting CPU sequence is P1, P2, P1, P3, P4, P1, P3, P1. P2 completes at time 2, P4 at 5, P3 at 7 and P1 at 8. In the requested P1,P2,P3,P4 order, the finish times are 8,2,7,5.

## Key Points

- For dynamic-priority scheduling, build a one-quantum timeline and update ready-queue priorities at every boundary; report completion times in process-ID order.

## Why the other options are incorrect

A is simple arrival-order completion and ignores dynamic priority/preemption. C gives an impossible finish time 2 for P1, which needs four CPU units. D swaps the completion order of P3 and P4; P4's single quantum completes at time 5, while P3 needs its second quantum at time 7.
