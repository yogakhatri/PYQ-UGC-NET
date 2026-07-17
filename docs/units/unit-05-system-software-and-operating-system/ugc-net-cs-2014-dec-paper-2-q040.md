# Question 40

*UGC NET CS · 2014 Dec Paper 2 · Memory Management · Page-Fault Service Time*

In a demand-paging system, servicing a page fault takes 8 ms if an empty frame is available or the replaced page is unmodified, and 20 ms if the replaced page is modified. What is the average page-fault service time if the replaced page is modified 70% of the time?

- **A.** 11.6 ms
- **B.** 16.4 ms
- **C.** 28 ms
- **D.** 14 ms

> [!TIP]
> **Correct answer: B. 16.4 ms**

## Solution

The replaced page is modified with probability 0.70, giving a 20 ms service, and unmodified with probability 0.30, giving an 8 ms service. The expected time is 0.70×20+0.30×8=14+2.4=16.4 ms.

## Key Points

- Expected service time is the probability-weighted average of the two mutually exclusive fault paths.

## Why the other options are incorrect

11.6 reverses or miscombines the weights. 28 adds the two service times instead of averaging mutually exclusive cases. 14 includes only the modified-case weighted contribution and omits the unmodified contribution.
