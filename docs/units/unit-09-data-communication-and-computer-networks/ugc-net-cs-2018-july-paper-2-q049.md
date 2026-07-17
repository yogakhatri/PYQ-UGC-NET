# Question 49

*UGC NET CS · 2018 July Paper 2 · Error Detection and Correction · Minimum Distance and Error-Correction Capacity*

To guarantee correction of upto t errors, the minimum Hamming distan ce d min in a block code must be ________.

- **1.** t+1
- **2.** t−2
- **3.** 2t−1
- **4.** 2t+1

> [!TIP]
> **Correct answer: 4. 2t+1**

## Solution

A code can correct every pattern of at most t errors only when radius-t Hamming balls around distinct codewords do not overlap. If two codewords were at distance 2t or less, a received word could lie within t changes of both and decoding would be ambiguous. Hence d_min must satisfy d_min≥2t+1. The required minimum is 2t+1, option 4.

## Key Points

- Error correction needs disjoint radius-t Hamming balls, giving d_min≥2t+1.

## Why the other options are incorrect

t+1 is sufficient for detecting t errors, not correcting them. t−2 is smaller still. 2t−1 fails because two radius-t neighborhoods can overlap. The paired rules are: detect s errors when d_min≥s+1; correct t errors when d_min≥2t+1.
