# Question 4

*UGC NET CS · 2014 Dec Paper 3 · 8085 Microprocessor · Instruction Flag Effects*

Match the following 8085 instructions with the flags : List – I List – II a. XCHG i. only carry flag is affected. b. SUB ii. no flags are affected. c. STC iii. all flags other than carry flag are affected. d. DCR iv. all flags are affected. Codes : a b c d

- **A.** iv i iii ii
- **B.** iii ii i iv
- **C.** ii iii i iv
- **D.** ii iv i iii

> [!TIP]
> **Correct answer: D. ii iv i iii**

## Solution

XCHG merely swaps HL and DE and affects no flags, so a→ii. SUB updates all five condition flags, including carry/borrow, so b→iv. STC sets only carry, so c→i. DCR changes sign, zero, auxiliary carry and parity but preserves carry, so d→iii. The sequence is ii, iv, i, iii.

## Key Points

- 8085 cues: XCHG none; SUB all; STC carry only; DCR all condition flags except carry.

## Why the other options are incorrect

A assigns all flags to XCHG and none to DCR. B says SUB affects no flags. C incorrectly says DCR affects carry as well. Only D matches all 8085 flag rules.
