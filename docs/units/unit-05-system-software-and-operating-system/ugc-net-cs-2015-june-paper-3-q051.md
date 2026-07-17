# Question 51

*UGC NET CS · 2015 June Paper 3 · Memory Management · MMU Address Translation*

What is the most appropriate function of Memory Management Unit (MMU) ?

- **1.** It is an associative memory to store TLB
- **2.** It is a technique of supporting multiprogramming by creating dynamic partitions
- **3.** It is a chip to map virtual address to physical address
- **4.** It is an algorithm to allocate and deallocate main memory to a process

> [!TIP]
> **Correct answer: 3. It is a chip to map virtual address to physical address**

## Solution

The memory-management unit is hardware in the address path that translates each CPU-generated virtual address into a physical address, while also enforcing protection and access permissions. It consults page/segment tables and usually a TLB. Thus the most appropriate description is a chip or hardware unit that maps virtual to physical addresses.

## Key Points

- OS builds translation tables; MMU hardware applies them on memory references; TLB caches recent translations.

## Why the other options are incorrect

A TLB is associative memory used by the MMU, not the MMU itself. Dynamic partitioning is one allocation technique, and allocation/deallocation policies are operating-system algorithms. Neither defines the hardware translation unit.
