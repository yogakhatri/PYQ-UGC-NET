# Question 65

*UGC NET CS · 2018 July Paper 2 · Transactions and Concurrency Control · Conflict Serializability and Precedence Graphs*

Consider two transaction schedules: S1: r1(X); r1(Y); r2(X); r2(Y); w2(Y); w1(X). S2: r1(X); r2(X); r2(Y); w2(Y); r1(Y); w1(X). Which statement is correct?

- **1.** Both S1 and S2 are conflict serializable.
- **2.** Both S1 and S2 are not conflict serializable.
- **3.** S1 is conflict serializable and S2 is not conflict serializable.
- **4.** S1 is not conflict serializable and S2 is conflict serializable.

> [!TIP]
> **Correct answer: 4. S1 is not conflict serializable and S2 is conflict serializable.**

## Solution

Build a precedence graph. In S1, r1(Y) occurs before w2(Y), giving T1→T2; r2(X) occurs before w1(X), giving T2→T1. The cycle makes S1 not conflict serializable. In S2, the X conflict r2(X) before w1(X) and the Y conflict w2(Y) before r1(Y) both give only T2→T1. That acyclic graph is equivalent to serial order T2 then T1. Therefore option 4 is correct.

## Key Points

- A schedule is conflict serializable exactly when its precedence graph is acyclic.

## Why the other options are incorrect

Options 1 and 3 incorrectly call cyclic S1 serializable. Option 2 overlooks that every cross-transaction conflict in S2 points in the same direction, so S2 has a valid topological order.
