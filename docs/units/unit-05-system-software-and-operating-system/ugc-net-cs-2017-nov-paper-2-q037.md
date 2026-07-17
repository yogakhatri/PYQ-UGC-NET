# Question 37

*UGC NET CS · 2017 Nov Paper 2 · Secondary Storage · C-SCAN Disk Scheduling*

In __________ disk scheduling algorithm, the disk head moves from one end to other end of the disk, serving the requests along the way. When the head reaches the other end, it immediately returns to the beginning of the disk without serving any requests on the return trip.

- **1.** LOOK
- **2.** SCAN
- **3.** C - LOOK
- **4.** C - SCAN

> [!TIP]
> **Correct answer: 4. C - SCAN**

## Solution

C-SCAN treats the disk as a circular sequence. The head moves in one direction, serving requests until it reaches the physical end, then returns directly to the beginning without serving on the return trip. That exactly matches the description, so option 4 is correct.

## Key Points

- C-SCAN: service one-way to the disk end, jump back empty; C-LOOK: service one-way only as far as the last request, then jump to the first request.

## Why the other options are incorrect

SCAN reverses direction at the end and serves requests on both sweeps. LOOK reverses at the last pending request rather than going to the physical end. C-LOOK also jumps circularly, but between the last and first pending requests rather than necessarily between the disk's physical ends.
