# Question 50

*UGC NET CS · 2017 Jan Paper 3 · File and Input/Output Systems · SCAN Disk Scheduling*

Consider a disk queue with I/O requests on the following cylinders in their arriving order : 6, 10, 12, 54, 97, 73, 128, 15, 44, 110, 34, 45 The disk head is assumed to be at cylinder 23 and moving in the direction of decreasing number of cylinders. Total number of cylinders in the disk is 150. The disk head movement using SCAN-scheduling algorithm is :

- **1.** 172
- **2.** 173
- **3.** 227
- **4.** 228

> [!TIP]
> **Correct answer: 1. 172**

## Solution

SCAN moves like an elevator to a physical end before reversing. Starting at 23 and moving downward, the head services 15,12,10,6 and continues to cylinder 0, a movement of 23. It then reverses, services 34,44,45,54,73,97,110,128, and continues to the far end, cylinder 149, adding 149. Total movement is 23+149=172 cylinders, so option 1 is correct.

## Key Points

- SCAN reaches disk endpoints; with 150 cylinders, endpoints are 0 and 149.
- LOOK reverses at the last pending request instead.

## Why the other options are incorrect

Stopping at the last request 128 would be LOOK, not full SCAN, and would total 151. The 173/228-type answers typically arise from treating 150 as a cylinder label even though 150 cylinders are numbered 0 through 149 or from adding an unnecessary extra movement.
