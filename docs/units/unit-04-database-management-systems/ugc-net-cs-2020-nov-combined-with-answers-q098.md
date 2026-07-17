# Question 98

*UGC NET CS · 2020 Nov With Answers · Transaction Processing and Concurrency Control · Conflicting Operations*

In concurrency control, a pair of operations in a schedule conflict if: (A) at least one operation is a write; (B) both operations access the same data item; (C) the operations belong to different transactions; (D) the operations access different data items. Which conditions are required?

- **1.** (A) and (B) only
- **2.** (A), (B) and (C) only
- **3.** (A), (C) and (D) only
- **4.** (C) and (D) only

> [!TIP]
> **Correct answer: 2. (A), (B) and (C) only**

## Solution

Two schedule operations conflict exactly when all three conditions hold: they belong to different transactions, access the same data item, and at least one is a write. Their relative order can then affect the value read or the final database state. Thus A, B, and C are required, while D states the opposite of B. The answer is option 2.

## Key Points

- Conflict test: different transactions + same item + at least one write.

## Why the other options are incorrect

Two reads never conflict because swapping them changes nothing. Operations on different items do not conflict, and operations within one transaction are not the inter-transaction pairs used to construct a precedence graph. Options 1, 3, and 4 omit a required condition or include D.
