# Question 68

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Data Structures · Priority Queues*

S. 0:87018 Process in memory also contain the heap section. What is the use of heap section?

- **1.** Contains temporary data
- **2.** Dynamically allocate the memory during process run time
- **3.** Contains Process priority and pointers to scheduling queues
- **4.** Contains amount of CPU and real time use

> [!TIP]
> **Correct answer: 2. Dynamically allocate the memory during process run time**

## Solution

The heap stores memory obtained and released dynamically while the process runs, such as objects created by malloc/new.

## Key Points

- Stack: automatic call data; heap: runtime dynamic allocation.

## Why the other options are incorrect

Temporary automatic data normally uses the stack; priority, queue pointers, and CPU accounting belong in the process control block.
