# Question 32

*UGC NET CS · 2017 Jan Paper 2 · Assembly Language · x86 Register, Shift, and Carry Arithmetic*

Execute the assembly instructions in order: mov al,15; mov ah,15; xor al,al; mov cl,3; shr ax,cl; add al,90H; adc ah,0. What hexadecimal value remains in AX?

- **1.** 0270H
- **2.** 0170H
- **3.** 01E0H
- **4.** 0370H

> [!TIP]
> **Correct answer: 1. 0270H**

## Solution

The first two moves make AX=0F0Fh because decimal 15 is 0Fh. xor al,al clears AL, so AX=0F00h. Shifting right by 3 gives AX=01E0h and CF=0 because the three discarded low bits were zero. add al,90h computes E0h+90h=170h, leaving AL=70h and setting carry. Finally adc ah,0 adds that carry to AH=01h, making AH=02h. Therefore AX=0270h, option 1.

## Key Points

- Track AX as AH:AL after every instruction, and remember that ADC adds both its explicit operand and CF.

## Why the other options are incorrect

0170h omits the carry added into AH. 01E0h is the intermediate value immediately after the shift. 0370h adds an extra, nonexistent carry or miscomputes the shift result.
