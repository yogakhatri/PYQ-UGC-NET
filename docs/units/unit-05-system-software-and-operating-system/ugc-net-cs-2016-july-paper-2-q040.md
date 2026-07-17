# Question 40

*UGC NET CS · 2016 July Paper 2 · CPU Scheduling · Waiting-Time Priority and Round Robin*

A scheduling Algorithm assigns priority proportional to the waiting time of a process. Every process starts with priority zero (lowest priority). The scheduler reevaluates the process priority for every ‘T’ time units and decides next process to be scheduled. If the process have no I/O operations and all arrive at time zero, then the scheduler implements _________ criteria.

- **1.** Priority scheduling
- **2.** Round Robin Scheduling
- **3.** Shortest Job First
- **4.** FCFS

> [!TIP]
> **Correct answer: 2. Round Robin Scheduling**

## Solution

At time zero all processes have equal priority. Suppose one process runs for T units. During that interval the others wait, so at the next reevaluation they have higher priority than the process that just ran. Successive T-unit reevaluations give every waiting process a turn before returning to the earlier one. This is round-robin behavior with time quantum T.

## Key Points

- Periodic preemption plus priority proportional to waiting time produces cyclic service—Round Robin with quantum T.

## Why the other options are incorrect

Although priority values select the next process internally, the observable scheduling discipline under the stated assumptions is Round Robin. Burst lengths are never consulted, so it is not SJF. One process does not run to completion before the next, so it is not FCFS.
