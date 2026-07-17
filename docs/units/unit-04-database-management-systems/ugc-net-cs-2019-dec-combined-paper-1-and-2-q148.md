# Question 148

*UGC NET CS · 2019 Dec Paper 1 And 2 · Relational Database Design · Functional Dependencies, Keys and Normalization*

What is the highest normal form satisfied by relation R?

- **1.** 1NF
- **2.** 2NF
- **3.** 3NF
- **4.** BCNF

> [!TIP]
> **Correct answer: 2. 2NF**

## Solution

All attributes are atomic, so R is in 1NF. Its only candidate key is the single attribute A. Because a one-attribute key has no proper nonempty subset, no nonprime attribute can be partially dependent on part of the key; therefore R is in 2NF. It is not in 3NF: dependencies BC→D and D→E have determinants that are not superkeys, while D and E are nonprime attributes. In particular A→D→E is a transitive dependency from the key to E. Hence the highest normal form is 2NF, option 2.

## Key Points

- Single-attribute keys make 2NF automatic; 3NF still fails when a nonkey determinant determines a nonprime attribute.

## Why the other options are incorrect

Option 1 understates the relation because a single-attribute key rules out partial dependency. Options 3 and 4 fail on D→E (and BC→D): the determinants are not superkeys and the right-side attributes are not prime.
