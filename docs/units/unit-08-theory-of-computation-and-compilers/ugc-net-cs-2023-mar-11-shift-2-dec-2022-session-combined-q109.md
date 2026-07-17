# Question 109

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Code Generation and Optimization · Control-Flow and Data-Flow Analysis*

I. No.5 BID: 18705 Which of the following statements are correct? A. The first three-address instruction in the intermediate code is a leader. B. The instruction which is exactly at the middle of the given three address code is a leader. C. Any instruction that is the target of a conditional or unconditional jump is a leader: D. Any instruction that immediately follows a conditional or unconditional jump is a leader. Choose the correct answer from the options given below:

- **1.** A. B and C
- **2.** B. C and D
- **3.** A, C and D
- **4.** A, B, C and D

> [!TIP]
> **Correct answer: 3. A, C and D**

## Solution

Basic-block leaders are the first instruction, every jump target, and every instruction immediately following a conditional or unconditional jump. Hence A, C, and D are true. Being physically in the middle of the code has no control-flow significance, so B is false.

## Key Points

- Leaders are determined by control-flow entry points, not list position.

## Why the other options are incorrect

Alternatives containing B invent a leader rule; the remaining alternative omits an actual rule.
