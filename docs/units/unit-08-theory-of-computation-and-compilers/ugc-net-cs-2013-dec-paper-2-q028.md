# Question 28

*UGC NET CS · 2013 Dec Paper 2 · Regular Languages and Finite Automata · Closure Properties and Palindromes*

Given the following statements : S 1 : If L is a regul ar language then the language {uv | u ∈ L, v ∈ LR} is also regular. S 2 : L = {ww R} is regular language. Which of the following is true ?

- **A.** S 1 is not correct and S 2 is not correct.
- **B.** S 1 is not correct and S2 is correct.
- **C.** S 1 is correct and S2 is not correct.
- **D.** S 1 is correct and S2 is correct.

> [!TIP]
> **Correct answer: C. S 1 is correct and S2 is not correct.**

## Solution

S1 is true. Regular languages are closed under reversal, so L^R is regular when L is regular; they are also closed under concatenation, so L L^R={uv | u in L, v in L^R} is regular. S2 is false: {ww^R} is the language of even-length palindromes, which requires unbounded comparison between the first half and its reverse and is not regular.

## Key Points

- Regular languages are closed under reversal and concatenation, but the language of arbitrary palindromes is not regular.

## Why the other options are incorrect

A and B incorrectly reject the closure argument in S1. D incorrectly accepts the palindrome language as regular. A finite automaton cannot remember an arbitrarily long first half to verify the second half.
