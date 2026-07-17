# Question 125

*UGC NET CS · 2020 Nov With Answers · Parallel Computer Architecture · Flynn’s Taxonomy*

Arrange the following types of machine in descending order of complexity. (A) SISD (B) MIMD (C) SIMD Choose the correct answer from the options given below:

- **1.** A, B, C
- **2.** C, B, A
- **3.** B, C, A
- **4.** C, A, B

> [!TIP]
> **Correct answer: 3. B, C, A**

## Solution

In Flynn’s taxonomy, SISD has one instruction stream and one data stream: a conventional sequential machine. SIMD applies one instruction stream to many data elements, requiring multiple processing lanes but common control. MIMD supports multiple independent instruction streams operating on multiple data streams, demanding the richest control, coordination, and interconnection. Descending architectural complexity is therefore MIMD>SIMD>SISD, or B,C,A: option 3.

## Key Points

- More independent instruction streams mean more control complexity: MIMD highest, SIMD middle, SISD lowest.

## Why the other options are incorrect

Any order placing SISD above a parallel organization reverses the increase in hardware/control complexity. SIMD is less general than MIMD because its processing elements execute the same instruction in lockstep.
