# Question 129

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Big Data Systems · Characteristics and Types of Big Data*

Consider the following schedule S. T1 T2 T4 Timestamp t1 R(Y) W(X) WM R(X) R(Y) W(Y) W(X) t5 R(X) t6 W(X) R(X) denotes read operation on data item X by transaction Ti. W[X) denotes write operation on data item X by transaction Ti. Choose the correct execution order for the above schedule S.

- **1.** T3-T2-T1-T4
- **2.** T2-T3-T1-T4
- **3.** T2-T4-T3-T1
- **4.** T4-T2-T3-T1

> [!TIP]
> **Correct answer: 3. T2-T4-T3-T1**

## Solution

Conflict edges are T2→T4 and T2→T3 on X; T4→T3 on X; and T3→T1 on Y. The precedence order forced by this acyclic graph is T2,T4,T3,T1.

## Key Points

- Build a precedence edge Ti→Tj when Ti's conflicting operation occurs first.

## Why the other options are incorrect

Other serial orders violate at least one observed conflicting-operation order.
