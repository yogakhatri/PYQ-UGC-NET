# Question 92

*UGC NET CS · 2020 Nov With Answers · Digital Logic · Boolean-Function Simplification*

For the Boolean function F(A,B,C,D) = Σm(0,1,2,3,6,12,13,14,15), which of the following are simplified expressions? (A) A'B' + AB + A'C'D'; (B) A'B' + AB + A'CD'; (C) A'B' + AB + BC'D'; (D) A'B' + AB + BCD'.

- **1.** (A) only
- **2.** (B) only
- **3.** (A) and (B) only
- **4.** (B) and (D) only

> [!TIP]
> **Correct answer: 4. (B) and (D) only**

## Solution

The common terms A'B' and AB cover minterms {0,1,2,3} and {12,13,14,15}. The only uncovered required minterm is 6=0110. In expression B, A'CD' covers minterms 2 and 6, both in F, so B is valid. In expression D, BCD' covers 6 and 14, again both in F, so D is valid. Thus B and D are equivalent simplified covers of F, giving option 4.

## Key Points

- Check each added implicant: it must cover the missing minterm 6 without introducing any zero-minterm.

## Why the other options are incorrect

Expression A adds A'C'D', which covers minterms 0 and 4; minterm 4 is not in F, and minterm 6 remains uncovered. Expression C adds BC'D', which likewise includes the unwanted minterm 4 and does not cover 6. Therefore A and C are invalid.
