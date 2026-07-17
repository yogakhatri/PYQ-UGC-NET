# Question 147

*UGC NET CS · 2019 Dec Paper 1 And 2 · Relational Database Design · Functional Dependencies, Keys and Normalization*

Identify a primary key of relation R under F.

- **1.** BC
- **2.** AD
- **3.** A
- **4.** AB

> [!TIP]
> **Correct answer: 3. A**

## Solution

Compute A's closure. From A→BC, add B and C. Because B and C are now both present, BC→D adds D. Finally D→E adds E. Thus A+={A,B,C,D,E}, so A is a superkey. It is also minimal because it contains only one attribute; therefore A is a candidate key and may be chosen as the primary key. Option 3 is correct.

## Key Points

- A candidate key is a minimal determinant of all attributes; use attribute closure, then test minimality.

## Why the other options are incorrect

BC+={B,C,D,E}, which lacks A, so BC is not a key. AD and AB both determine all attributes because they contain A, but each is a nonminimal superkey: removing D or B leaves A, which is already a key.
