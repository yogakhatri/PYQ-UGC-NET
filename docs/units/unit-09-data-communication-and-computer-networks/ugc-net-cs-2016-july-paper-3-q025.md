# Question 25

*UGC NET CS · 2016 July Paper 3 · Multiplexing · TDM Circuit Bit Rate*

If link transmits 4000 frames per second and each slot has 8 bits, the transmission rate of circuit of this TDM is ______.

- **1.** 64 Kbps
- **2.** 32 MbpS
- **3.** 32 Kbps
- **4.** 64 MbpS

> [!TIP]
> **Correct answer: 3. 32 Kbps**

## Solution

One TDM circuit contributes one 8-bit slot to each frame. At 4000 frames per second, its rate is 4000×8=32,000 bit/s=32 Kbps. Therefore option 3 is correct.

## Key Points

- Per-channel synchronous TDM rate = frames per second × bits in that channel's slot.

## Why the other options are incorrect

The 64-Kbps choices double the slot contribution without justification. The Mbps choices confuse thousands with millions. This question asks for one circuit's rate, not the aggregate rate of every slot in a complete frame.
