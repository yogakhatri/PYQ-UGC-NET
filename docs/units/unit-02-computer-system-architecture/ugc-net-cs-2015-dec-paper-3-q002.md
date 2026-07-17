# Question 2

*UGC NET CS · 2015 Dec Paper 3 · Microprocessor Programming · 8085 Data Transfer and Output Instructions*

What is output at PORT1 after this 8085 program: `MVI B,82H`; `MOV A,B`; `MOV C,A`; `MVI D,37H`; `OUT PORT1`; `HLT`?

- **1.** 37H
- **2.** 82H
- **3.** B9H
- **4.** 00H

> [!TIP]
> **Correct answer: 2. 82H**

## Solution

`MVI B,82H` loads B with 82H. `MOV A,B` copies that value to the accumulator, so A=82H; `MOV C,A` copies it again without changing A. `MVI D,37H` changes only D. In the 8085, `OUT port` sends the accumulator's contents to the selected output port, so PORT1 receives 82H.

## Key Points

- 8085 `OUT` writes the accumulator to the addressed I/O port.

## Why the other options are incorrect

37H is in D, not A. No addition produces B9H, and nothing clears the accumulator to 00H. Always trace the accumulator before an 8085 `OUT` instruction.
