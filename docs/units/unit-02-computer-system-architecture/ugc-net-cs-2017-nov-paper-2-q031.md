# Question 31

*UGC NET CS · 2017 Nov Paper 2 · Microprocessor Programming · LOOP Instruction and 16-bit Register Arithmetic*

Consider the following program fragment in assembly language : mov ax, 0h mov cx, 0A h doloop : dec ax loop doloop What is the value of ax and cx registers after the completion of the doloop ?

- **1.** ax=FFF5 h and cx=0 h
- **2.** ax=FFF6 h and cx=0 h
- **3.** ax=FFF7 h and cx=0A h
- **4.** ax=FFF5 h and cx=0A h

> [!TIP]
> **Correct answer: 2. ax=FFF6 h and cx=0 h**

## Solution

`CX` starts at 0Ah=10. Each pass first executes `dec ax`, then the x86 `loop` instruction decrements `CX` and jumps while the new value is nonzero. The body therefore runs exactly 10 times and leaves `CX=0`. Starting with 16-bit `AX=0000h`, ten decrements wrap modulo 2¹⁶ to 0000h−000Ah=FFF6h. Hence option 2 is correct.

## Key Points

- x86 `loop label` performs `CX←CX−1` and branches if CX≠0; 16-bit register arithmetic wraps modulo 65,536.

## Why the other options are incorrect

FFF5h would require 11 decrements, and FFF7h would require only 9. Options 3 and 4 incorrectly leave CX at 0Ah; `loop` itself consumes the count by decrementing CX on every iteration.
