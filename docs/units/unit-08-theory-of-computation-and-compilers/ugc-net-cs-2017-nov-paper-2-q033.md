# Question 33

*UGC NET CS · 2017 Nov Paper 2 · Regular Languages · Regular Expressions for Odd and Even Binary Values*

Which of the following regular expressions, each describing a language of binary numbers (MSB to LSB) that represents non-negative decimal values, does not include even values ?

- **1.** 0*1+0*1*
- **2.** 0*1*0+1*
- **3.** 0*1*0*1+
- **4.** 0+1*0*1*

> [!TIP]
> **Correct answer: 3. 0*1*0*1+**

## Solution

A non-negative binary integer is even exactly when its least-significant bit—the final bit—is 0. Expression 3, `0*1*0*1+`, requires one or more 1s at the end, so every nonempty represented value it accepts ends in 1 and is odd. It therefore does not include even values, making option 3 correct.

## Key Points

- For binary integers written MSB-to-LSB, parity depends only on the final symbol: 0 means even and 1 means odd.

## Why the other options are incorrect

Expression 1 can end in its `0*` part, expression 2 explicitly contains a nonempty `0+` block and may end there when the final `1*` is empty, and expression 4 can generate strings ending in 0. Each of those therefore includes at least one even binary value.
