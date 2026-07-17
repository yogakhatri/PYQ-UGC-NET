# Question 34

*UGC NET CS · 2015 June Paper 2 · Compiler Design · LL, LR, and LALR Parsing*

Which statement is false?

- **1.** LALR parser is a bottom-up parser
- **2.** A parsing algorithm that scans left to right and produces a rightmost derivation is RL(1)
- **3.** LR parser is a bottom-up parser
- **4.** In LL(1), 1 indicates one-symbol look-ahead

> [!TIP]
> **Correct answer: 2. A parsing algorithm that scans left to right and produces a rightmost derivation is RL(1)**

## Solution

`LR(1)` means the input is scanned Left to right, a Rightmost derivation is constructed in reverse, and one lookahead symbol is used. Option 2 incorrectly calls this `RL(1)` and omits the essential `in reverse` qualification, so it is the false statement.

## Key Points

- LR(k) = left-to-right scan, rightmost derivation in reverse, k-symbol lookahead.

## Why the other options are incorrect

LR parsing is bottom-up, and LALR is an LR-family bottom-up method, making statements 1 and 3 true. In `LL(1)`, the final 1 does denote one lookahead symbol, so statement 4 is also true.
