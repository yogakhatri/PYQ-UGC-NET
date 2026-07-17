# Question 131

*UGC NET CS · 2020 Nov With Answers · Control Unit and Addressing Modes · Hardwired Control and Indirect Addressing*

Statement I: A hardwired control unit can be optimized for fast operation. Statement II: Indirect addressing mode needs two memory references to fetch the operand. Choose the correct evaluation.

- **1.** Both Statement I and Statement Il are true
- **2.** Both Statement I and Statement II are false
- **3.** Statement I is correct but Statement Il is false
- **4.** Statement I is incorrect but Statement II is true.

> [!TIP]
> **Correct answer: 1. Both Statement I and Statement Il are true**

## Solution

A hardwired control unit implements control signals with fixed logic rather than fetching and interpreting microinstructions. Its logic can therefore be optimized for high speed, so Statement I is true. In indirect addressing, the address field points to a memory location that contains the effective address; memory is accessed once to obtain that address and again to fetch the operand. Counting operand-fetch accesses after the instruction has been read, this is two memory references, so Statement II is also true. Hence option 1.

## Key Points

- Hardwired control trades flexibility for speed; memory-indirect addressing adds one pointer access before the operand access.

## Why the other options are incorrect

Options 2–4 reject one or both standard properties. Indirect addressing is slower precisely because of the extra pointer lookup; hardwired control is fast but less flexible than microprogrammed control.
