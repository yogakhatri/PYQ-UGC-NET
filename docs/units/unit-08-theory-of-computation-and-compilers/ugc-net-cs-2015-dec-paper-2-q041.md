# Question 41

*UGC NET CS · 2015 Dec Paper 2 · Code Generation and Optimization · Loop and Peephole Optimization*

Loop unrolling is a code optimization technique :

- **1.** that avoids tests at every iteration of the loop.
- **2.** that improves performance by decreasing the number of instructions in a basic block.
- **3.** that exchanges inner loops with outer loops.
- **4.** that reorders operations to allow multiple computations to happen in parallel.

> [!TIP]
> **Correct answer: 1. that avoids tests at every iteration of the loop.**

## Solution

Loop unrolling duplicates the loop body so one loop-control test covers several original iterations. Unrolling by a factor of four, for example, performs four body instances before the next branch, reducing index updates and tests. Thus it avoids a test at every original iteration.

## Key Points

- Unrolling trades larger code size for fewer loop-control operations.

## Why the other options are incorrect

Unrolling usually increases, not decreases, the number of instructions in the enlarged basic block. Exchanging inner and outer loops is loop interchange. Reordering operations for parallel execution is instruction scheduling, although unrolling may expose opportunities for it.
