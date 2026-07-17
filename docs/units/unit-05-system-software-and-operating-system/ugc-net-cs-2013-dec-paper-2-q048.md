# Question 48

*UGC NET CS · 2013 Dec Paper 2 · File and Input/Output Systems · SSTF and SCAN Disk Scheduling*

A disk queue has requests for cylinders 98, 183, 37, 122, 14, 124, 65 and 67 in that order. The head starts at cylinder 53 and is moving toward cylinder 0. What are the total head movements under SSTF and SCAN respectively?

- **A.** 236 and 252 cylinders
- **B.** 640 and 236 cylinders
- **C.** 235 and 640 cylinders
- **D.** 235 and 252 cylinders

> [!TIP]
> **Correct answer: A. 236 and 252 cylinders**

## Solution

SSTF services the nearest pending cylinder in the order 53→65→67→37→14→98→122→124→183. The movements 12+2+30+23+84+24+2+59 total 236. For SCAN moving downward, the head goes from 53 to cylinder 0, then reverses and continues to the far end cylinder 199; total movement is 53+199=252 cylinders while servicing requests along the path.

## Key Points

- SSTF repeatedly chooses the closest request.
- SCAN travels to a disk end before reversing; LOOK reverses at the last pending request.

## Why the other options are incorrect

235 is an arithmetic error in the SSTF path. 640 is far too large and typically results from repeatedly measuring from the initial position. A SCAN total of 236 would stop at the last request 183, which is LOOK behavior; standard SCAN continues to the physical end of the disk.
