# Question 41

*UGC NET CS · 2018 July Paper 2 · Data Communication · Slotted ALOHA Throughput*

A slotted ALOHA network transmits 200-bit frames over a 200 kbps shared channel. If all stations together produce 250 frames per second, what is the successful throughput in frames per second?

- **1.** 49
- **2.** 368
- **3.** 149
- **4.** 151

> [!TIP]
> **Correct answer: No valid option: correct slotted-ALOHA throughput is about 195 successful frames per second; option 1 (49) results from multiplying by the offered load twice.**

## Solution

A 200-bit frame on a 200,000-bit/s channel occupies 0.001 s, so there are 1000 slots/s. The offered load is G=250×0.001=0.25 attempts/slot. Slotted ALOHA throughput is S=G e^(−G)=0.25e^(−0.25)≈0.1947 successful frames/slot. Multiplying by 1000 slots/s gives about 194.7 successful frames/s. Equivalently, each offered frame succeeds with probability e^(−0.25), so 250e^(−0.25)=194.7.

## Key Points

- S=G e^(−G) is successful frames per slot; convert to frames/s by multiplying by slots/s, not by offered frames/s.

## Why the other options are incorrect

Option 1's 49 is obtained by incorrectly calculating 250×S: S already includes G=0.25, so this counts the offered-load factor twice. 368 is the maximum normalized slotted-ALOHA result at G=1 expressed per 1000 slots; 149 and 151 do not match the stated load.
