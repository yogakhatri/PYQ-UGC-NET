# Question 20

*UGC NET CS · 2012 Dec Paper 2 · CPU Scheduling · Aging and Starvation*

The problem of indefinite blockage of low-priority jobs in a general priority-scheduling algorithm can be solved using:

- **A.** Parity bit
- **B.** Aging
- **C.** Compaction
- **D.** Timer

> [!TIP]
> **Correct answer: B. Aging**

## Solution

Indefinite blockage in priority scheduling is starvation: a low-priority job may wait forever while higher-priority jobs keep arriving. Aging prevents this by gradually increasing the priority of a process the longer it waits. Eventually its priority becomes high enough for the scheduler to run it.

## Key Points

- Starvation is cured by aging: waiting time is converted into progressively higher scheduling priority.

## Why the other options are incorrect

A parity bit detects certain transmission errors. Compaction combines scattered free memory to reduce external fragmentation. A timer supports preemption and time accounting but, by itself, does not guarantee that a low-priority job's priority will ever overtake newly arriving jobs.
