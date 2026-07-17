# Question 38

*UGC NET CS · 2016 July Paper 2 · File and Input/Output Systems · FCFS Disk Scheduling*

If the Disk head is located initially at track 32, find the number of disk moves required with FCFS scheduling criteria if the disk queue of I/O blocks requests are : 98, 37, 14, 124, 65, 67

- **1.** 320
- **2.** 322
- **3.** 321
- **4.** 319

> [!TIP]
> **Correct answer: 3. 321**

## Solution

FCFS services requests in the listed order. Total head movement is |32−98|+|98−37|+|37−14|+|14−124|+|124−65|+|65−67| =66+61+23+110+59+2=321 tracks. Therefore option 3 is correct.

## Key Points

- FCFS disk movement is the sum of absolute differences along the exact request sequence, starting at the initial head position.

## Why the other options are incorrect

The other totals result from omitting a transition or making a one-track arithmetic error. FCFS does not reorder requests to reduce movement; every consecutive absolute difference must be included.
