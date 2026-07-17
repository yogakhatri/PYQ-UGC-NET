# Question 86

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Data Communication · Hamming distance and error detection*

What is the minimum Hamming Distance in a block code if we want to be able to detect up to S errors?

- **1.** 5
- **2.** S+1
- **3.** 1
- **4.** 0

> [!TIP]
> **Correct answer: 2. S+1**

## Solution

A code with minimum distance d_min can detect up to d_min−1 bit errors. To detect S errors, require d_min≥S+1; the minimum is S+1.

## Key Points

- Detection capability = d_min−1.

## Why the other options are incorrect

Distances S or smaller cannot guarantee detecting all S-error patterns.
