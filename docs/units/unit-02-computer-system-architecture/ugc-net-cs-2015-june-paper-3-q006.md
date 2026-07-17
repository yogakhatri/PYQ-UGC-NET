# Question 6

*UGC NET CS · 2015 June Paper 3 · Digital Logic Circuits and Components · Modulo Counters and Flip-Flop Count*

The number of flip-flops required to design a modulo - 272 counter is :

- **1.** 8
- **2.** 9
- **3.** 27
- **4.** 11

> [!TIP]
> **Correct answer: 2. 9**

## Solution

A counter with `k` flip-flops has at most `2^k` distinct binary states. We need the smallest `k` with `2^k ≥ 272`. Since `2^8 = 256 < 272` but `2^9 = 512 ≥ 272`, nine flip-flops are required; unused states can be redirected to a valid state.

## Key Points

- Minimum flip-flops for a modulo-M counter = `ceil(log₂ M)`.

## Why the other options are incorrect

Eight flip-flops provide only 256 states, which is insufficient. Twenty-seven and eleven flip-flops provide far more states than needed and are not minimal.
