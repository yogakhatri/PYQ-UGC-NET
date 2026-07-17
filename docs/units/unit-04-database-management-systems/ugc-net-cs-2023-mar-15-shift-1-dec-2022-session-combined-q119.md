# Question 119

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Normalization for Relational Databases · Transaction Processing*

Match List I with List II List II List I I. As long as the transaction is already running, it will try to obtain the required lock A. Timestamp protocol in the first part Il. Indicates final lock of the schedule B. Strict two-phase locking protocol III. Ensures freedom from deadlock C. Two-phase locking D. Lock point in two phase locking IV. Ensures cascade -less rollback protocol Choose the correct answer from the options given below:

- **1.** A-III, B-IV, C-II, D-I
- **2.** A-IlI, B-IV, C-I, D-I
- **3.** A-IV, B-III, C-II, D-I
- **4.** A-IV, B-II, C-I, D-III

> [!TIP]
> **Correct answer: No listed option — correct matching is A–III, B–IV, C–I, D–II**

## Solution

Timestamp ordering ensures deadlock freedom (A–III). Strict 2PL holds write locks to commit and prevents cascading rollback (B–IV). Ordinary 2PL obtains locks during its growing first phase (C–I). The lock point is the transaction's final lock acquisition (D–II). This exact mapping is absent.

## Key Points

- 2PL lock point = last lock acquired; strictness prevents cascading aborts.

## Why the other options are incorrect

Each offered option swaps the 2PL growing-phase description and lock-point definition or misassigns timestamp/strict 2PL.
