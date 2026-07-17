# Question 97

*UGC NET CS · 2019 June Paper 1 And 2 · Memory Management · Minimum frame allocation*

The minimum number of page frames that must be allocated to a running process in a virtual-memory environment is determined by:

- **1.** page size
- **2.** physical size of memory
- **3.** the instruction-set architecture
- **4.** number of processes in memory

> [!TIP]
> **Correct answer: 3. the instruction-set architecture**

## Solution

A process must have enough frames to execute any single machine instruction. Some instruction-set architectures allow one instruction to access several memory locations, including the instruction bytes and multiple operands that may cross page boundaries. The architecture's maximum simultaneous page requirement therefore determines the minimum frame allocation.

## Key Points

- The minimum frames per process are constrained by the maximum number of pages one machine instruction can reference.

## Why the other options are incorrect

Page size and physical-memory size affect capacity, but they do not define how many distinct pages one instruction may need. The number of resident processes is an allocation-policy concern, not the architectural minimum for one process.
