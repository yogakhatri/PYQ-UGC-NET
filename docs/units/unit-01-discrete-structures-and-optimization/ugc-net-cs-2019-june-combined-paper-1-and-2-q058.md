# Question 58

*UGC NET CS · 2019 June Paper 1 And 2 · Mathematical Logic · Propositional Equivalences*

Match each formula in List I with its logically equivalent formula in List II. List I: (a) p -> q; (b) p OR q; (c) p AND q; (d) NOT(p -> q). List II: (i) NOT(q -> NOT p); (ii) p AND NOT q; (iii) NOT p -> q; (iv) NOT p OR q.

- **A.** a-ii, b-iii, c-i, d-iv
- **B.** a-ii, b-i, c-iii, d-iv
- **C.** a-iv, b-i, c-iii, d-ii
- **D.** a-iv, b-iii, c-i, d-ii

> [!TIP]
> **Correct answer: D. a-iv, b-iii, c-i, d-ii**

## Solution

Eliminate implications one by one. (a) p->q is NOT p OR q, so (a)-(iv). For (b), NOT p->q becomes NOT(NOT p) OR q=p OR q, so (b)-(iii). For (c), q->NOT p is NOT q OR NOT p; negating it and applying De Morgan gives q AND p, so (c)-(i). Finally, NOT(p->q)=NOT(NOT p OR q)=p AND NOT q, so (d)-(ii). The complete match is a-iv, b-iii, c-i, d-ii.

## Key Points

- Use p->q equivalent to NOT p OR q, then apply double negation and De Morgan's laws.

## Why the other options are incorrect

Options A-C mismatch at least one implication identity. A fast check is that p->q must pair with NOT p OR q and its negation must pair with p AND NOT q; only option D contains both.
