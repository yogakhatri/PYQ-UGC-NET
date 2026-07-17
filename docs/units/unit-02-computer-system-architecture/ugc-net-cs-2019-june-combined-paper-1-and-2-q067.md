# Question 67

*UGC NET CS · 2019 June Paper 1 And 2 · Input-Output Organization · Bus arbitration*

The parallel bus arbitration technique uses an external priority encoder and a decoder. Suppose a parallel arbiter has 5 bus arbiters. What will be the sizes of the priority encoder and decoder respectively?

- **1.** 4x2, 2x4
- **2.** 2x4, 4x2
- **3.** 3x8, 8x3
- **4.** 8x3, 3x8

> [!TIP]
> **Correct answer: 4. 8x3, 3x8**

## Solution

Five request lines require at least three encoded bits because 2^2<5≤2^3. A standard parallel arbiter therefore uses an 8-input, 3-output priority encoder. The three-bit encoded winner is then expanded by a 3-to-8 decoder to generate the individual grant line. Hence the sizes are 8×3 and 3×8.

## Key Points

- For n requesters, use k=ceil(log2 n) encoded bits: a 2^k-to-k encoder followed by a k-to-2^k decoder.

## Why the other options are incorrect

- **Options 1 and 2:** a two-bit code distinguishes only four requesters.
- **Option 3:** reverses the roles of the encoder and decoder.
