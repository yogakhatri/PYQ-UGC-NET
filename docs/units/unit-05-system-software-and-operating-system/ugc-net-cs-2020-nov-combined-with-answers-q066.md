# Question 66

*UGC NET CS · 2020 Nov With Answers · File and Input/Output Systems · SSTF Disk Scheduling*

A disk has 60 cylinders and receives requests for cylinders 10, 22, 20, 2, 40, 6, and 38. The head starts at cylinder 20, movement between adjacent cylinders takes 2 ms, and SSTF scheduling is used. How long does it take to satisfy all requests?

- **1.** 240 milliseconds
- **2.** 96 milliseconds
- **3.** 120 milliseconds
- **4.** 112 milliseconds

> [!TIP]
> **Correct answer: 3. 120 milliseconds**

## Solution

SSTF always serves the pending request nearest the current head. The request at 20 is served immediately with zero movement. The remaining service order is 22, 10, 6, 2, 38, 40. The movements are |22−20|=2, |10−22|=12, |6−10|=4, |2−6|=4, |38−2|=36, and |40−38|=2, totalling 60 cylinders. At 2 ms per cylinder, the time is 60×2=120 ms, option 3.

## Key Points

- For SSTF, repeatedly select the smallest absolute distance from the current head and sum all head movements.

## Why the other options are incorrect

The other values come from preserving arrival order, skipping the zero-distance request incorrectly, or choosing a nonnearest cylinder at some step. SSTF must be reevaluated after every service because the head position changes.
