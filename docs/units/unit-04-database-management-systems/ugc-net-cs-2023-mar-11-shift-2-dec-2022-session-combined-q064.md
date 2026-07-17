# Question 64

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Normalization for Relational Databases · Functional Dependencies and Normalization*

Identity the incorrect statements).

- **1.** A candidate key is minimal set of one or more attributes that, taken collectively, allows us to uniquely identify any entity in the entity set.
- **2.** A candidate key for which no proper subset is also a candidate key is called a super key.
- **3.** A super key is a set of one or more attributes that, taken collectively, allows us to uniquely identify any entity in the entity set.
- **4.** A super key for which no proper subset is also a super key is called a candidate key.

> [!TIP]
> **Correct answer: 2. A candidate key for which no proper subset is also a candidate key is called a super key.**

## Solution

A superkey is any attribute set that uniquely identifies an entity or tuple. A candidate key is a minimal superkey—removing any attribute destroys uniqueness. Statement 2 reverses this logic by saying that a minimal candidate key is called a superkey; candidate keys are already minimal, while minimality is the property used to select candidate keys from superkeys. Hence statement 2 is the incorrect statement.

## Key Points

- Every candidate key is a superkey, but not every superkey is a candidate key; candidate key = minimal superkey.

## Why the other options are incorrect

Statements 1 and 4 give the intended minimal-uniqueness definition of a candidate key. Statement 3 correctly defines a superkey without imposing minimality.
