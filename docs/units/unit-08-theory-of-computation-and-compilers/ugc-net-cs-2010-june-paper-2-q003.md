# Question 3

*UGC NET CS · 2010 June Paper 2 · Regular Language Models · Grammars and Expressions*

“My Lafter Machin (MLM) recognizes the following strings : (i) a (ii) aba (iii) abaabaaba (iv) abaabaabaabaabaabaabaabaaba Using this as an information, how would you compare the following regular expressions ? (i) (aba) 3x (ii) a.(baa)3 x–1. ba (iii) ab.(aab). 3x–1.a

- **A.** (ii) and (iii) are same, (i) is different.
- **B.** (ii) and (iii) are not same.
- **C.** (i), (ii) and (iii) are different.
- **D.** (i), (ii) and (iii) are same.

> [!TIP]
> **Correct answer: D. (i), (ii) and (iii) are same.**

## Solution

Let n=3^x. Expression (i) is (aba)^n. The identity (aba)^n = a(baa)^(n−1)ba gives (ii): adjacent copies concatenate as aba|aba = a|baa|ba. Similarly, regrouping yields (aba)^n = ab(aab)^(n−1)a, which is (iii). Hence all three denote the same strings for the intended positive values of x.

## Key Points

- Cyclic regrouping of repeated 'aba' blocks produces both alternative forms without changing the string.

## Why the other options are incorrect

Options A–C deny at least one of these direct concatenation/regrouping identities.
