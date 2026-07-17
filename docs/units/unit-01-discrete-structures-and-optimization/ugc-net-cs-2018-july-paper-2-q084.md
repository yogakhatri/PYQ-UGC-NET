# Question 84

*UGC NET CS · 2018 July Paper 2 · Counting, Mathematical Induction and Discrete Probability · Discrete Probability Mass Functions*

Digital sensor data can fill 0 to 32 buffers. Let S={0,1,2,…,32}, where outcome i means i buffers are full and p(i)=(33−i)/561. If A is the event that an even number of buffers are full, find p(A).

- **1.** 0.515
- **2.** 0.785
- **3.** 0.758
- **4.** 0.485

> [!TIP]
> **Correct answer: 1. 0.515**

## Solution

Even outcomes are i=0,2,…,32. Therefore p(A)=[(33−0)+(33−2)+⋯+(33−32)]/561=(33+31+⋯+1)/561. These are the first 17 odd positive integers in reverse order, and their sum is 17²=289. Hence p(A)=289/561≈0.51515, which rounds to 0.515, option 1.

## Key Points

- Sum the PMF only over the event; 1+3+⋯+(2n−1)=n².

## Why the other options are incorrect

The other decimals do not match the normalized even-outcome sum. A useful check is Σ(i=0 to 32)(33−i)=33+32+⋯+1=561, so the printed p(i) is a valid probability mass function.
