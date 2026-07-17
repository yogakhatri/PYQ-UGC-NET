# Question 2

*UGC NET CS · 2017 Jan Paper 3 · Memory Management · Virtual Memory Benefits and Overheads*

Which of the following is incorrect for virtual memory ?

- **1.** Large programs can be written
- **2.** More I/O is required
- **3.** More addressable memory available
- **4.** Faster and easy swapping of process

> [!TIP]
> **Correct answer: 4. Faster and easy swapping of process**

## Solution

Virtual memory lets a process use an address space larger than the currently available main memory, so large programs can run and more memory is addressable. The price is extra disk traffic when nonresident pages must be fetched, so more I/O can be required. It does not make process swapping inherently faster; disk transfers, page faults, and bookkeeping add overhead. Therefore the incorrect statement is option 4.

## Key Points

- Virtual memory increases usable address space and flexibility, but page faults and backing-store transfers cost time rather than automatically speeding swapping.

## Why the other options are incorrect

Options 1 and 3 are principal benefits of virtual memory. Option 2 states a real possible cost: demand paging may generate additional I/O. Option 4 reverses that performance tradeoff.
