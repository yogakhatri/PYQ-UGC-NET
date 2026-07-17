# Question 5

*UGC NET CS · 2012 Dec Paper 2 · File and Input/Output Systems · FCFS Disk Scheduling*

If the disk head is initially at cylinder 32, how many disk moves are required by FCFS for the request queue 98, 37, 14, 124, 65, 67?

- **1.** 239
- **2.** 310
- **3.** 321
- **4.** 325

> [!TIP]
> **Correct answer: 3. 321**

## Solution

FCFS services requests in their arrival order. Starting at 32, the head movements are |98-32|=66, |37-98|=61, |14-37|=23, |124-14|=110, |65-124|=59, and |67-65|=2. Adding them gives 66+61+23+110+59+2=321 cylinder moves.

## Key Points

- For FCFS disk scheduling, preserve queue order and sum the absolute difference between every pair of consecutive head positions.

## Why the other options are incorrect

The other totals do not equal the sum of all six consecutive movements. A common error is to measure every request from the initial cylinder or to omit one transition; FCFS requires measuring from the head's new position after each service.
