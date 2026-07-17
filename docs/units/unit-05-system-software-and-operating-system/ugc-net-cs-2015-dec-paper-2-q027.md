# Question 27

*UGC NET CS · 2015 Dec Paper 2 · Memory Management · Page-Fault Rate and Effective Runtime*

Suppose that the number of instructions executed between page fault is directly proportional to the number of page frames allocated to a program. If the available memory is doubled, the mean interval between page faults is also doubled. Further, consider that a normal instruction takes one microsecond, but if a page fault occurs, it takes 2001 microseconds. If a program takes 60 sec to run, during which time it gets 15,000 page faults, how long would it take to run if twice as much memory were available ?

- **1.** 60 sec
- **2.** 30 sec
- **3.** 45 sec
- **4.** 10 sec

> [!TIP]
> **Correct answer: 3. 45 sec**

## Solution

A faulting instruction takes 2001 μs instead of the normal 1 μs, so each fault adds 2000 μs. The original fault overhead is 15,000×2000 μs=30 s. Since total runtime is 60 s, the underlying instruction work takes 30 s. Doubling memory doubles the interval between faults, halving the count to 7,500; the new fault overhead is 7,500×2000 μs=15 s. Total time becomes 30+15=45 s.

## Key Points

- Separate base execution time from page-fault penalty, then change only the fault-frequency component.

## Why the other options are incorrect

60 s assumes no improvement, 30 s incorrectly removes all fault cost, and 10 s has no support. Only the page-fault component is halved; the normal instruction time remains unchanged.
