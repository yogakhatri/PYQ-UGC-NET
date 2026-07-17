# Question 42

*UGC NET CS · 2015 Dec Paper 2 · Assembly Language · Register Operations and Logical Shifts*

What hexadecimal value remains in AX after: `mov al,15`; `mov ah,15`; `xor al,al`; `mov cl,3`; `shr ax,cl`? (The source calls AX 32-bit, although AX is the 16-bit register.)

- **1.** 0F00 h
- **2.** 0F0F h
- **3.** 01E0 h
- **4.** FFFF h

> [!TIP]
> **Correct answer: 3. 01E0 h**

## Solution

After `mov al,15` and `mov ah,15`, AX=0x0F0F because decimal 15 is 0x0F. `xor al,al` clears only AL, producing AX=0x0F00. Then CL=3 and `shr ax,cl` logically shifts AX right three bits: 0x0F00/8=0x01E0. Therefore option 3 is correct.

## Key Points

- AL and AH are the low and high bytes of AX; logical right shift inserts zeros.

## Why the other options are incorrect

0x0F00 is the value before the shift; 0x0F0F is the value before AL is cleared; 0xFFFF is never produced. The source's ‘AX (32-bit)’ wording is inaccurate—AX is 16-bit—but it does not change this computation.
