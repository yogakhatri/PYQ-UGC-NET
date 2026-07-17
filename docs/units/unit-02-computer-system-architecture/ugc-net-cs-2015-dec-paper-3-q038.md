# Question 38

*UGC NET CS · 2015 Dec Paper 3 · Memory Hierarchy · Memory Management Unit and Address Translation*

Function of memory management unit is :

- **1.** Address translation
- **2.** Memory allocation
- **3.** Cache management
- **4.** All of the above

> [!TIP]
> **Correct answer: 1. Address translation**

## Solution

The memory management unit is hardware on the processor's memory path whose defining job is translating CPU-generated virtual/logical addresses into physical addresses, while also enforcing relevant access permissions. Therefore address translation is the correct choice.

## Key Points

- MMU performs address translation and protection; the OS decides allocation.

## Why the other options are incorrect

Choosing which regions/pages to allocate is an operating-system policy, not the MMU's job. Cache management belongs primarily to cache hardware and system policies. Since option 2 is false, ‘all of the above’ is also false.
