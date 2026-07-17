# Question 4

*UGC NET CS · 2015 Dec Paper 3 · Memory Organization · DRAM Refresh Overhead*

A dynamic RAM is refreshed 32 times per millisecond. Each refresh takes 100 ns and a memory cycle takes 250 ns. What percentage of the memory's total operating time is required for refreshes?

- **1.** 0.64
- **2.** 0.96
- **3.** 2.00
- **4.** 0.32

> [!TIP]
> **Correct answer: 4. 0.32**

## Solution

In one millisecond the RAM performs 32 refresh operations, each occupying 100 ns. Total refresh time is 32×100=3,200 ns=3.2 μs. One millisecond is 1,000 μs, so the fraction is 3.2/1000=0.0032; as a percentage this is 0.32%.

## Key Points

- Refresh overhead percentage = refreshes per interval × time per refresh ÷ interval length × 100.

## Why the other options are incorrect

0.64%, 0.96%, and 2.00% overcount the refresh occupancy. The 250 ns ordinary memory-cycle time is not needed when total elapsed time and refresh duration are already given; it would only confirm the number of possible cycles per millisecond.
