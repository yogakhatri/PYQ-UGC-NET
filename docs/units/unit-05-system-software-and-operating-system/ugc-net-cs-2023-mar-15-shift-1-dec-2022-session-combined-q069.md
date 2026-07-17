# Question 69

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Memory Management · Page Replacement*

How many page faults occur for optimal algorithm for the following reference string, with four frames? 1,2,3,4,5,3,4,1,6,7,8,7,8

- **1.** 8
- **2.** 7
- **3.** 6
- **4.** 5

> [!TIP]
> **Correct answer: 1. 8**

## Solution

With four empty frames, 1,2,3,4 cause four faults. 5 causes a fifth, optimally evicting 2 because it is never reused. Then 3,4,1 hit. References 6,7,8 each introduce a new page and cause faults 6,7,8; the final 7,8 hit. Total: 8.

## Key Points

- OPT evicts the page whose next use is farthest away, or never occurs.

## Why the other options are incorrect

Counts 5–7 omit one or more compulsory/new-page faults.
