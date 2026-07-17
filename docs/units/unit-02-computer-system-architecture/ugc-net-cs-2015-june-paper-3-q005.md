# Question 5

*UGC NET CS · 2015 June Paper 3 · Input-Output Organization · Programmed-I/O Transfer Rate*

The CPU of a system having 1 MIPS execution rate needs 4 machine cycles on an average for executing an instruction. The fifty percent of the cycles use memory bus. A memory read/ write employs one machine cycle. For execution of the programs, the system utilizes 90 percent of the CPU time. For block data transfer, an IO device is attached to the system while CPU executes the background programs continuously. What is the maximum IO data transfer rate if programmed IO data transfer technique is used ?

- **1.** 500 Kbytes/sec
- **2.** 2.2 Mbytes/sec
- **3.** 125 Kbytes/sec
- **4.** 250 Kbytes/sec

> [!TIP]
> **Correct answer: The data given do not determine a unique programmed-I/O rate. The exam-intended choice is option 4 (250 Kbytes/s), but it requires an unstated transfer-loop cost or a nonstandard interpretation of MIPS.**

## Solution

`1 MIPS` already means one million instructions per second; with four machine cycles per instruction, the machine-cycle rate is four million per second. Background execution at 90% and 50% memory-bus use tells us about CPU and bus availability, but programmed I/O also needs a specified sequence—poll/status test, input, memory store, address/count updates, and branch—and the question never states how many instructions or bytes each transfer uses. Different legitimate assumptions produce different rates. The commonly keyed 250 Kbytes/s effectively assumes one byte per four instruction-times (or mistakenly divides 1 MIPS by the four-cycle CPI), neither of which follows from the stem.

## Key Points

- For programmed-I/O throughput, you must know CPU work and bus transactions per byte; MIPS, CPI, utilization, and bus occupancy alone are insufficient.

## Why the other options are incorrect

No option can be proved uniquely from the supplied facts. `2.2 Mbytes/s` is the unused bus-cycle rate after subtracting background memory-bus use, but that is a DMA-style bus bound, not automatically a programmed-I/O throughput. The 500, 250, and 125 Kbytes/s choices correspond to different unstated CPU work per byte.
