# Question 2

*UGC NET CS · 2016 July Paper 3 · Input-Output Organization · 8085 Hardware Interrupt Lines*

8085 microprocessor has _____ hardware interrupts.

- **1.** 2
- **2.** 3
- **3.** 4
- **4.** 5

> [!TIP]
> **Correct answer: 4. 5**

## Solution

The 8085 has five hardware interrupt inputs: TRAP, RST 7.5, RST 6.5, RST 5.5, and INTR. Hence the required count is 5, option 4.

## Key Points

- 8085 hardware interrupts: TRAP, RST 7.5, RST 6.5, RST 5.5, INTR—five in total.

## Why the other options are incorrect

Counts 2, 3, and 4 omit one or more interrupt pins. Do not confuse the five hardware inputs with the eight software `RST 0` through `RST 7` instructions or with only the vectored interrupts.
