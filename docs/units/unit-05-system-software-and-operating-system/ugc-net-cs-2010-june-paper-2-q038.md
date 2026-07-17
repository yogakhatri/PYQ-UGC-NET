# Question 38

*UGC NET CS · 2010 June Paper 2 · CPU Scheduling · Multiple-Processor Scheduling*

_____ is a preemptive scheduling algorithm.

- **1.** Round Robin
- **2.** SSN
- **3.** SSF
- **4.** Priority based

> [!TIP]
> **Correct answer: 1. Round Robin**

## Solution

Round-robin is inherently preemptive: a timer interrupts a running process at the end of its quantum and returns it to the ready queue if unfinished.

## Key Points

- The time quantum is the explicit preemption mechanism in round-robin.

## Why the other options are incorrect

Shortest-job/seek-first variants are not inherently preemptive, and priority scheduling may be implemented either preemptively or nonpreemptively, making it less uniquely correct.
