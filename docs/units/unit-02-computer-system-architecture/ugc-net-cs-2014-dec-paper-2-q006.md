# Question 6

*UGC NET CS · 2014 Dec Paper 2 · Arithmetic Circuits · BCD Adder Hardware*

The BCD adder to add two decimal digits needs minimum of

- **A.** 6 full adders and 2 half adders
- **B.** 5 full adders and 3 half adders
- **C.** 4 full adders and 3 half adders
- **D.** 5 full adders and 2 half adders

> [!TIP]
> **Correct answer: D. 5 full adders and 2 half adders**

## Solution

The initial addition of two 4-bit BCD digits and the input carry uses four full adders. If the binary result exceeds 9 or produces a carry, the correction circuit adds 0110. The least significant bit passes unchanged; adding the conditional correction bit at bit 1 needs a half adder, bit 2 needs one full adder because it also receives a carry, and bit 3 needs another half adder. Total: 5 full adders and 2 half adders.

## Key Points

- BCD addition = 4-bit binary addition plus a conditional +0110 correction optimized to 1 FA and 2 HAs.

## Why the other options are incorrect

A uses one extra full adder, while B and C use three half adders even though the correction path needs only two. The optimized correction stage is one full plus two half adders beyond the four-full-adder binary stage.
