# Question 30

*UGC NET CS · 2012 June Paper 2 · CPU Scheduling · Round-Robin Time Quantum*

In round robin CPU scheduling as time quantum is increased the average turn around time

- **A.** increases
- **B.** decreases
- **C.** remains constant
- **D.** varies irregularly

> [!TIP]
> **Correct answer: D. varies irregularly**

## Solution

Increasing the round-robin quantum reduces context switches and makes the policy approach FCFS, but average turnaround time is not monotonic. A larger quantum may let a long process delay several short ones, increasing their completion times; in another workload it may reduce repeated waiting and context-switch effects. As the quantum crosses different CPU-burst lengths, the completion order can change discontinuously. Thus the average varies irregularly with the workload and chosen quantum.

## Key Points

- RR turnaround depends on burst lengths and completion order; changing quantum can help or hurt non-monotonically.

## Why the other options are incorrect

There is no universal always-increasing or always-decreasing rule, and the value is not constant. Those claims can be disproved by choosing different burst-time sets.
