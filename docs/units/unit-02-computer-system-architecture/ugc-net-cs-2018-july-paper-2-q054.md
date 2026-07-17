# Question 54

*UGC NET CS · 2018 July Paper 2 · Input/Output Organization · Protection for Memory-Mapped I/O*

Normally user programs are prevented from handling I/O directly by I/O instructions in them. For CPUs having explicit I/O instructions, such I/O protecti on is ensured by having the I/O instructions privileged. In a CPU with memory mapped I/O, there i s no explicit I/O instruction. Which one of the following is true for a CPU with mem ory mapped I/O ?

- **1.** I/O protection is ensured by operating system routines.
- **2.** I/O protection is ensured by a hardware trap.
- **3.** I/O protection is ensured during system configuration.
- **4.** I/O protection is not possible.

> [!TIP]
> **Correct answer: 2. I/O protection is ensured by a hardware trap.**

## Solution

Memory-mapped I/O registers occupy addresses in the memory address space, so ordinary load/store instructions are used. Protection therefore comes from memory-protection hardware: the OS marks the I/O address range inaccessible to user mode, and an attempted user access causes a protection fault or hardware trap. The trap transfers control to privileged code. Hence option 2 is correct.

## Key Points

- Memory-mapped I/O is protected like privileged memory: unauthorized loads/stores fault in hardware and trap to the OS.

## Why the other options are incorrect

OS routines configure and handle protection, but software alone cannot check every arbitrary user load/store; hardware must enforce the access permission. Protection is not merely a one-time configuration claim, and it is certainly possible through privilege and address-space protection.

## References

- [University of Pennsylvania CSE 240 — Input/Output: Connecting to the Outside World](https://acg.cis.upenn.edu/milom/cse240-Fall06/lectures/Ch08.pdf)
