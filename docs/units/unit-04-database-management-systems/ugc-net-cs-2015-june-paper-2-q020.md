# Question 20

*UGC NET CS · 2015 June Paper 2 · Data Modeling · Weak Entities and Owner Entity Sets*

For a weak entity set to be meaningful, it must be associated with another entity set in combination with some of their attribute values, is called as :

- **1.** Neighbour Set
- **2.** Strong Entity Set
- **3.** Owner Entity Set
- **4.** Weak Set

> [!TIP]
> **Correct answer: 3. Owner Entity Set**

## Solution

A weak entity lacks enough attributes to form a complete key by itself. It is identified through an identifying relationship with another entity set, using the owner's key together with the weak entity's partial key. That supporting set is called the owner entity set, so option 3 is correct.

## Key Points

- Weak-entity identity = owner entity's key + weak entity's partial key.

## Why the other options are incorrect

`Neighbour set` and `weak set` are not the ER-model terms for the supporting entity set. An owner is normally a strong entity set, so option 2 describes a common property but not the specific relationship role asked for; `owner entity set` is the precise term.
