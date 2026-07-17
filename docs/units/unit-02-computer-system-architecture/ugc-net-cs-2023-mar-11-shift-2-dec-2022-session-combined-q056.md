# Question 56

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Digital Logic Circuits and Components · Memory capacity from address and data lines*

. No. BID:18700 The memory size for n address lines and m data lines is given by

- **1.** 2'Ix n
- **2.** m x n
- **3.** 2 x m
- **4.** n x m

> [!TIP]
> **Correct answer: 3. 2 x m**

## Solution

With n address lines, the circuit can select 2^n distinct addresses. Each selected address stores or supplies m data bits because there are m data lines. Hence the organization is 2^n words × m bits, and the total capacity is 2^n·m bits. This is option 3 (whose exponent is faint in the OCR text).

## Key Points

- n binary address lines select 2^n locations; m data lines determine the word width.

## Why the other options are incorrect

Multiplying n by m treats address lines as though each line selected only one word. The address lines encode binary combinations, so the number of addressable words grows exponentially as 2^n, not linearly as n.
