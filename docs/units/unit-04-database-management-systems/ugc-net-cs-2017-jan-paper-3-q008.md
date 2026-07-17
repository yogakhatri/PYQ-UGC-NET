# Question 8

*UGC NET CS · 2017 Jan Paper 3 · Relational Model · Superkeys, Candidate Keys, and Primary Keys*

Which one is correct w.r.t. RDBMS ?

- **1.** primary key ⊆ super key ⊆ candidate key
- **2.** primary key ⊆ candidate key ⊆ super key
- **3.** super key ⊆ candidate key ⊆ primary key
- **4.** super key ⊆ primary key ⊆ candidate key

> [!TIP]
> **Correct answer: 2. primary key ⊆ candidate key ⊆ super key**

## Solution

A superkey is any attribute set that uniquely identifies a tuple. A candidate key is a minimal superkey, and the primary key is one candidate key selected as the relation's main identifier. Treating the terms as classes of allowable keys gives primary key ⊆ candidate key ⊆ superkey, which is option 2.

## Key Points

- Every primary key is a candidate key, and every candidate key is a superkey; the converses need not hold.

## Why the other options are incorrect

The reverse containments fail because many superkeys contain unnecessary attributes and are not candidate keys, while a relation can have candidate keys that were not selected as its primary key.
