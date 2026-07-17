# Question 86

*UGC NET CS · 2019 June Paper 1 And 2 · Data Modeling · Candidate keys*

In relational database management, which of the following is/are properties of a candidate key? P: Uniqueness. Q: Irreducibility.

- **1.** P only
- **2.** Q only
- **3.** Both P and Q
- **4.** Neither P nor Q

> [!TIP]
> **Correct answer: 3. Both P and Q**

## Solution

A candidate key must uniquely identify every tuple, so uniqueness is required. It must also be minimal: if any attribute is removed, it must cease to be a superkey. This minimality is the stated irreducibility property. Hence both P and Q are true.

## Key Points

- A candidate key is a minimal superkey: unique and irreducible.

## Why the other options are incorrect

- **Options 1 and 2:** each omits one necessary property.
- **Option 4:** rejects both defining properties of a candidate key.
