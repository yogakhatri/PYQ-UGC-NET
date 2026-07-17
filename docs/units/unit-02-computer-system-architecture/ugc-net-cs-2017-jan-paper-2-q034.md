# Question 34

*UGC NET CS · 2017 Jan Paper 2 · Assembly Language · Subtraction, Borrow, and Sign Flags*

The contents of Register (BL) and Register (AL) of 8085 microprocessor are 49H and 3AH respectively. The contents of AL, the status of carry flag (CF) and sign flag (SF) after executing ‘SUB AL, BL’ assembly language instruction, are

- **1.** AL = 0FH; CF = 1; SF = 1
- **2.** AL = F0H; CF = 0; SF = 0
- **3.** AL = F1H; CF = 1; SF = 1
- **4.** AL = 1FH; CF = 1; SF = 1

> [!TIP]
> **Correct answer: 3. AL = F1H; CF = 1; SF = 1**

## Solution

Compute the 8-bit subtraction AL−BL=3Ah−49h. Since 3Ah<49h, a borrow occurs and CF becomes 1. The difference is −0Fh; in 8-bit two's-complement arithmetic, 100h−0Fh=F1h. The most significant bit of F1h is 1, so SF=1. Thus AL=F1h, CF=1, SF=1, which is option 3.

## Key Points

- For 8-bit subtraction, wrap a negative result modulo 256; CF records unsigned borrow and SF copies the result's top bit.

## Why the other options are incorrect

0Fh is the unsigned magnitude of the difference but ignores the negative two's-complement result. F0h is off by one. 1Fh reverses or otherwise miscomputes the operands. A borrow must set CF in x86 SUB semantics.

## Additional Information

The source incorrectly calls this an 8085 question even though AL, BL, CF, SF, and the two-operand SUB syntax are x86/8086 conventions. The calculation follows the registers and instruction actually printed.
