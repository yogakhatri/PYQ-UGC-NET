# Question 7

*UGC NET CS · 2017 Jan Paper 3 · Transaction Processing · Conflict Serializability and Precedence Graphs*

Consider following schedules involving two transactions : S1 : r1(X); r1(Y); r2(X); r2(Y); w2(Y); w1(X) S2 : r1(X); r2(X); r2(Y); w2(Y); r1(Y); w1(X) Which of the following statement is true ?

- **1.** Both S1 and S2 are conflict serializable.
- **2.** S1 is conflict serializable and S2 is not conflict serializable.
- **3.** S1 is not conflict serializable and S2 is conflict serializable.
- **4.** Both S1 and S2 are not conflict serializable.

> [!TIP]
> **Correct answer: 3. S1 is not conflict serializable and S2 is conflict serializable.**

## Solution

Build a precedence graph from conflicting operations. In S1, `r1(Y)` occurs before `w2(Y)`, giving T1→T2, while `r2(X)` occurs before `w1(X)`, giving T2→T1. The cycle means S1 is not conflict serializable. In S2, both conflicts point T2→T1: `r2(X)` precedes `w1(X)` and `w2(Y)` precedes `r1(Y)`. Its graph is acyclic and is equivalent to the serial order T2 then T1. Therefore option 3 is correct.

## Key Points

- A schedule is conflict serializable exactly when its transaction-precedence graph is acyclic.

## Why the other options are incorrect

Options 1 and 2 incorrectly call S1 serializable despite its two-way cycle. Option 4 overlooks that S2 has only one edge direction and is therefore conflict serializable.
