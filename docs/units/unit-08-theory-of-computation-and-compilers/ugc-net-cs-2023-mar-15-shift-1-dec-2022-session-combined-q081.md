# Question 81

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Code Generation and Optimization · Control-Flow and Data-Flow Analysis*

10-37031 While processing a string by an LR parser, the reading of the given string by the parser is..........

- **1.** From right to left
- **2.** From left to right
- **3.** Can be either from left to right or right to left
- **4.** From the centre of the given string

> [!TIP]
> **Correct answer: 2. From left to right**

## Solution

The L in LR means the input is scanned from left to right. The R describes constructing a rightmost derivation in reverse, not reading from the right.

## Key Points

- LR = Left-to-right scan, Rightmost derivation in reverse.

## Why the other options are incorrect

Options 1,3,4 contradict the definition of LR parsing.
