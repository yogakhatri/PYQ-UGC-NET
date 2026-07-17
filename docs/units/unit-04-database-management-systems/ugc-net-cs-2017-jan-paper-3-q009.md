# Question 9

*UGC NET CS · 2017 Jan Paper 3 · Data Modeling · Functional Dependency in Many-to-One Relationships*

Let pk(R) denotes primary key of relation R. A many-to-one relationship that exists between two relations R1 and R2 can be expressed as follows :

- **1.** pk(R2) → pk(R1)
- **2.** pk(R1) → pk(R2)
- **3.** pk(R2) → R1 ∩ R2
- **4.** pk(R1) → R1 ∩ R2

> [!TIP]
> **Correct answer: 2. pk(R1) → pk(R2)**

## Solution

Read the relationship as many R1 entities mapping to one R2 entity. Each R1 primary-key value identifies one R1 tuple and therefore determines the single related R2 primary-key value. Thus pk(R1) → pk(R2), which is option 2. Different R1 keys may determine the same R2 key, exactly expressing the many-to-one direction.

## Key Points

- For many-side R1 → one-side R2, the key of the many side functionally determines the key of the one side.

## Why the other options are incorrect

pk(R2) → pk(R1) would force each R2 entity to determine only one R1 entity, contradicting the 'many R1 to one R2' reading. The intersection expressions do not directly encode the cardinality between the entity identifiers.
