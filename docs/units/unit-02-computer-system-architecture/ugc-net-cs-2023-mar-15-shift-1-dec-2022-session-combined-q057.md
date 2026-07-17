# Question 57

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Programming the Basic Computer · Input-Output Programming*

0:37007 Consider a 3-bit counter, designed using T flip flops as shown below: Q Clk Assume the initial state of the counter given by PQR as 000, what are the next three states?

- **1.** 011, 101, 000
- **2.** 001, 010, 111
- **3.** 011, 101, 111
- **4.** 001, 010,000

> [!TIP]
> **Correct answer: 1. 011, 101, 000**

## Solution

For a T flip-flop, Q+=T⊕Q. From the diagram Tp=R, Tq=¬P, and Tr=¬Q. Starting 000 gives 011; applying the equations again gives 101; once more gives 000. Thus the next states are 011,101,000.

## Key Points

- Evaluate all synchronous flip-flop next states from the old state, not sequentially.

## Why the other options are incorrect

The other sequences do not satisfy the simultaneous next-state equations from the feedback wiring.

## References

- [Official GATE 2021 Computer Science paper](https://gate2026.iitg.ac.in/doc/download/2021/cs_2021.pdf)
