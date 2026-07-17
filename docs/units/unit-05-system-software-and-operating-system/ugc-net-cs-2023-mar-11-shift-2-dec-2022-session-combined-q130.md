# Question 130

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Memory Management · Contiguous Allocation*

Select the correct order of events after power is initialized on a system. A. Bootstrap loader is loaded from the disk B. Kernel is loaded onto the memory C. Firmware ROM loads boot block Choose the correct answer from the options given below:

- **1.** B. C, A
- **2.** C,A, B
- **3.** A, B, C
- **4.** A, C, B

> [!TIP]
> **Correct answer: 2. C,A, B**

## Solution

After power-on, firmware in ROM runs and loads the boot block (C). That loads the bootstrap loader from disk (A), which loads the OS kernel into memory (B). Thus C–A–B.

## Key Points

- Firmware starts the chain; bootloader locates and loads the kernel.

## Why the other options are incorrect

Other sequences require disk or kernel code before firmware has initialized the boot process.
