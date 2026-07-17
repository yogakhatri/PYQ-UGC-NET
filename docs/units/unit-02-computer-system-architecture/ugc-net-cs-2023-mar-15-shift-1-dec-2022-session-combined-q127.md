# Question 127

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Basic Computer Organization and Design · Register-transfer sequence for instruction fetch*

The sequence of events that happen during a typical fetch operation is/are: A. Memory B. MBR C. MAR D.PC E. IR Choose the correct order from the options given below:

- **1.** A, B, C, D, E
- **2.** D, C, A, B, E
- **3.** E, D, C, B, A
- **4.** D, C, A, E, B

> [!TIP]
> **Correct answer: 2. D, C, A, B, E**

## Solution

A fetch copies PC to MAR (D,C), reads Memory (A), places the word in MBR (B), then transfers it to IR (E). Order D,C,A,B,E.

## Key Points

- PC→MAR; memory→MBR; MBR→IR.

## Why the other options are incorrect

Other sequences access memory before establishing MAR or load IR before MBR.
