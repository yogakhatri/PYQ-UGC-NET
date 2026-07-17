# Question 103

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · File and Input/Output Systems · Directory and Disk Structure*

stOption 1D=450121 8810-87053 Select the correct order of basic page replacement. A. Page replacement algorithm is used in case there is no free frame B. The process is continued by restarting the instruction caused by TRAP C. Location of desired frame is found from disk D. Desired page is brought into newly freed frame and page & frame tables are updated

- **1.** A, B, D, C
- **2.** C, D, A, B
- **3.** C, A, D, B
- **4.** A, D, B, C

> [!TIP]
> **Correct answer: 3. C, A, D, B**

## Solution

On a page fault, locate the desired page on disk (C). If no free frame exists, invoke replacement to free one (A). Read the page into the frame and update tables (D), then restart the trapped instruction (B). Thus C–A–D–B.

## Key Points

- Locate → select/free frame → load/update → restart.

## Why the other options are incorrect

Other sequences restart before loading or try to load before choosing/freeing a frame.
