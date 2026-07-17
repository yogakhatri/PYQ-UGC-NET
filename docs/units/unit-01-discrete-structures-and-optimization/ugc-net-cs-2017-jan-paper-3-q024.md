# Question 24

*UGC NET CS · 2017 Jan Paper 3 · Recurrence Relations · Solving from Initial Values*

A recursive function is defined by h(0)=k, h(1)=1, and h(m)=2h(m−1)+4h(m−2) for m≥2. If h(4)=88, what is k?

- **1.** 0
- **2.** 1
- **3.** 2
- **4.** −1

> [!TIP]
> **Correct answer: 3. 2**

## Solution

Start with h(0)=k and h(1)=1. Then h(2)=2h(1)+4h(0)=2+4k. Next h(3)=2(2+4k)+4(1)=8+8k. Finally h(4)=2(8+8k)+4(2+4k)=24+32k. Setting this equal to 88 gives 32k=64, so k=2. Therefore option 3 is correct.

## Key Points

- Expand the recurrence carefully from the two base cases; here h(4)=24+32k.

## Why the other options are incorrect

Substituting k=0, 1, or −1 gives h(4)=24, 56, or −8, respectively, not 88. The recurrence must use both previous values at each step.
