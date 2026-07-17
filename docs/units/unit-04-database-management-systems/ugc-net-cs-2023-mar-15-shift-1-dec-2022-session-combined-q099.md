# Question 99

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Database System Concepts and Architecture · Database Languages and Interfaces*

Let Ti be a transaction that transfer Rs. 50 from account A to account B. This transaction can be defined as follows: Step Operation 1 Read(A) 2 A:=A - 50 Write(A) 4 Read(B) 5 B: =B + 50 6 Write(B) What will be the status of a database just after 3^ step but before 5" step of transaction execution?

- **1.** Always consistent
- **2.** May be temporarily inconsistent
- **3.** Must be abort
- **4.** Always rollback

> [!TIP]
> **Correct answer: 2. May be temporarily inconsistent**

## Solution

After Write(A), account A is reduced by 50, but B has not yet been increased. The invariant A+B is temporarily 50 too small. Atomic transaction execution permits such an intermediate state internally, provided it is not exposed/committed and is restored on failure.

## Key Points

- Consistency is required at transaction boundaries; intermediate steps may temporarily violate an invariant.

## Why the other options are incorrect

The transaction need not abort or roll back during normal progress, and the intermediate database is not always consistent.
