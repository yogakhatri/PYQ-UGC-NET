# Question 123

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Syntax Analysis · LL and LR parser configurations*

Match List I with List II List Il List I A. Initial Configuration of stack and input in LL Parsing process. I. $ w$ Il. $ $ B. Final Configuration of stack and input in LL Parsing process C. Initial Configuration of stack and input in LR Parsing process III. $S w$ D. Final Configuration of stack and input in LR Parsing process IV. $S $ Choose the correct answer from the options given below:

- **1.** A-III, B-IV, C-I, D-II
- **2.** A-III, B-II, C-I, D-IV
- **3.** А-II, B-III, C-IV, D-I
- **4.** A-II, B-IV, C-I, D-III

> [!TIP]
> **Correct answer: 2. A-III, B-II, C-I, D-IV**

## Solution

LL begins with stack `$S` and input `w$` (A–III), ending `$,$` (B–II). LR begins with stack `$` and input `w$` (C–I), and after acceptance has `$S,$` (D–IV).

## Key Points

- Predictive LL starts with S; bottom-up LR starts with only the end marker.

## Why the other options are incorrect

Other mappings confuse whether the start symbol is initially pushed (LL) or produced by reductions (LR).
