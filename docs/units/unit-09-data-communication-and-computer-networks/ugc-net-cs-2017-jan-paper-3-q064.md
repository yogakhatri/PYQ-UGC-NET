# Question 64

*UGC NET CS · 2017 Jan Paper 3 · Error Detection and Correction · Minimum Distance and Error-Correction Capacity*

Let C be a binary linear code with minimum distance 2t + 1 then it can correct upto _____ bits of error.

- **1.** t + 1
- **2.** t
- **3.** t – 2
- **4.** t/2

> [!TIP]
> **Correct answer: 2. t**

## Solution

To correct every pattern of t errors, the Hamming balls of radius t around distinct codewords must not overlap. Two such balls remain disjoint when the minimum distance is at least 2t+1. Equivalently, the correction capacity is floor((d_min−1)/2)=floor(2t/2)=t. Therefore option 2 is correct.

## Key Points

- A code with minimum distance d corrects floor((d−1)/2) errors and detects up to d−1 errors.

## Why the other options are incorrect

t+1 may produce received words closer to another codeword, while t−2 and t/2 understate the guaranteed capability. The exact bounded-distance correction radius for d_min=2t+1 is t.
