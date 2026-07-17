# Question 30

*UGC NET CS · 2014 Dec Paper 2 · Network Security · DES Structure and Rounds*

How many distinct stages are there in the DES algorithm, which is parameterized by a 56-bit key?

- **A.** 16
- **B.** 17
- **C.** 18
- **D.** 19

> [!TIP]
> **Correct answer: D. 19**

## Solution

In the stage-count convention used by this question, DES has an initial fixed permutation, 16 Feistel rounds driven by round keys derived from the effective 56-bit key, a 32-bit left/right swap, and the inverse final permutation. That is 1+16+1+1=19 distinct stages.

## Key Points

- DES stage count here is IP + 16 rounds + swap + IP⁻¹ = 19.

## Why the other options are incorrect

16 counts only the Feistel rounds. 17 or 18 includes only one or two of the initial permutation, final swap and inverse permutation. The stated 'distinct stages' convention counts all three around the 16 rounds.
