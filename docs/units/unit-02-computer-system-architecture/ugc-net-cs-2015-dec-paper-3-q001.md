# Question 1

*UGC NET CS · 2015 Dec Paper 3 · Digital Logic · Priority Encoders and Interrupt Vectors*

The outputs x1x2x3 of an 8×3 priority encoder form the vector address 101x1x2x300. If vector codes start with the highest-priority input, what is the second-highest-priority vector address in hexadecimal?

- **1.** BC
- **2.** A4
- **3.** BD
- **4.** AC

> [!TIP]
> **Correct answer: 2. A4**

## Solution

Under the ordering stated in the question, the highest-priority input is assigned encoder code 000 and the second-highest code 001. Substitute x1x2x3=001 into 101x1x2x300: the address is 10100100₂. Grouping into nibbles gives 1010 0100₂=A4₁₆, so option 2 is correct.

## Key Points

- Insert the three-bit priority code into the fixed vector template, then convert the resulting eight bits to hexadecimal.

## Why the other options are incorrect

BC corresponds to code 111, AC to code 011, and BD does not even end in the fixed 00 bits required by the address format. The calculation relies on the paper's convention that codes start at 000 for the highest priority.
