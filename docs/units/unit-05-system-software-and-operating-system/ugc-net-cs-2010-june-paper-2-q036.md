# Question 36

*UGC NET CS · 2010 June Paper 2 · CPU Scheduling · Multiple-Processor Scheduling*

Match the following. A. Disk scheduling; B. Batch processing; C. Time sharing; D. Interrupt processing. 1. Round-robin; 2. SCAN; 3. LIFO; 4. FIFO.

- **A.** 3,4,2,1
- **B.** 4,3,2,1
- **C.** 2,4,1,3
- **D.** 1,4,3,2

> [!TIP]
> **Correct answer: C. 2,4,1,3**

## Solution

Disk scheduling uses SCAN (A-2). Traditional batch jobs are served FIFO (B-4). Time-sharing CPU service uses round-robin (C-1). Nested interrupt servicing follows a LIFO return/priority stack (D-3). Thus 2,4,1,3.

## Key Points

- SCAN→disk, FIFO→batch, RR→time sharing, LIFO→nested interrupts.

## Why the other options are incorrect

Other mappings attach CPU round-robin to disk/interrupt work or swap the standard FIFO, SCAN, and LIFO roles.
