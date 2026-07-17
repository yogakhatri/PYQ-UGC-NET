# Question 28

*UGC NET CS · 2015 Dec Paper 2 · Secondary Storage · Disk Access Time*

Consider a disk with 16384 bytes per track having a rotation time of 16 msec and average seek time of 40 msec. What is the time in msec to read a block of 1024 bytes from this disk ?

- **1.** 57 msec
- **2.** 49 msec
- **3.** 48 msec
- **4.** 17 msec

> [!TIP]
> **Correct answer: 2. 49 msec**

## Solution

Average disk access time is seek time + average rotational latency + transfer time. Seek is 40 ms. Average rotational latency is half a 16 ms rotation, or 8 ms. A 1024-byte block is 1/16 of a 16,384-byte track, so transfer takes 16/16=1 ms. Total=40+8+1=49 ms.

## Key Points

- Disk read time = seek + half-rotation on average + proportional transfer time.

## Why the other options are incorrect

57 ms uses a full rotation rather than average half-rotation. 48 ms omits transfer time, and 17 ms omits the 40 ms seek.
