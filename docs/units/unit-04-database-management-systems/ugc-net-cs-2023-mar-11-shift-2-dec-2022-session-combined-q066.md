# Question 66

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Normalization for Relational Databases · Functional Dependencies and Normalization*

Which of the following statement is correct, according to the following instance of the relational schema R(X, Y, Z)? Y 1 1 a - 2 1 2 b

- **1.** X→ Y, Z→X
- **2.** Y→ Z, Z→X
- **3.** X→ Y, X→Z
- **4.** 1 → X, X-L

> [!TIP]
> **Correct answer: 3. X→ Y, X→Z**

## Solution

The instance contains (1,1,a), (1,1,a), (2,1,b), and (3,2,b). For every repeated X value, Y and Z remain the same, so both X→Y and X→Z hold in this instance. By contrast, Y=1 occurs with Z=a and Z=b, so Y→Z fails; Z=b occurs with X=2 and X=3, so Z→X fails.

## Key Points

- An FD A→B is violated as soon as two rows agree on A but disagree on B.

## Why the other options are incorrect

Option 1 contains the false dependency Z→X. Option 2 contains both Y→Z and Z→X, which fail. Option 4 contains Y→X, which fails because Y=1 is paired with multiple X values.
