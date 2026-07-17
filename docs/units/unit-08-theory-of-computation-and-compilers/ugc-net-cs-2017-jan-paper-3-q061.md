# Question 61

*UGC NET CS · 2017 Jan Paper 3 · Context-Free Language · Chomsky and Greibach Normal Forms*

Consider two statements. A. L={w | n_a(w)=n_b(w)} is deterministic context-free but not linear. B. L={a^n b^n | n≥0} ∪ {a^n b^(2n) | n≥0} is linear but not deterministic context-free. Which option is correct?

- **1.** Both (A) and (B) are false.
- **2.** Both (A) and (B) are true.
- **3.** (A) is true, (B) is false.
- **4.** (A) is false, (B) is true.

> [!TIP]
> **Correct answer: 2. Both (A) and (B) are true.**

## Solution

A is true: the language of all strings with equal numbers of a's and b's is deterministic context-free—a DPDA can keep the signed excess on its stack—but it is a standard example of a non-linear CFL. B is also true: each branch has a linear grammar, and linear languages are closed under finite union, so the union is linear; however, a DPDA cannot deterministically postpone the choice between accepting after n b's and after 2n b's, and this language is a standard non-DCFL example. Therefore both A and B are true, giving option 2.

## Key Points

- Linear and deterministic context-free languages are incomparable; these two languages witness the two opposite set differences.

## Why the other options are incorrect

Options 1, 3, and 4 reject one or both of two classic examples used to show that linear CFLs and deterministic CFLs are incomparable families: neither class contains the other.

## References

- [Formal Languages notes — Linear and deterministic context-free languages](https://people.cs.nycu.edu.tw/~rjchen/Formal-2018/Chap-11.4.pdf)
