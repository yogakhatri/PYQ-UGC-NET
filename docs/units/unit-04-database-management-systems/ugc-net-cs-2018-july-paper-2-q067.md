# Question 67

*UGC NET CS · 2018 July Paper 2 · Data Modeling · Many-to-One Relationships as Functional Dependencies*

A many-to-one relationship exists from entity set r1 to entity set r2. How is it represented using functional dependencies if Pk(r) denotes the primary-key attribute of relation r?

- **1.** Pk(r1) → Pk(r2)
- **2.** Pk(r2) → Pk(r1)
- **3.** Pk(r2) → Pk(r1) and Pk(r 1) → Pk(r2)
- **4.** Pk(r2) → Pk(r1) or Pk(r 1) → Pk(r2)

> [!TIP]
> **Correct answer: 1. Pk(r1) → Pk(r2)**

## Solution

`many-to-one from r1 to r2` means each r1 entity is associated with at most one r2 entity, although many r1 entities may share that same r2. Therefore the key of an r1 entity uniquely determines the key of its related r2 entity: Pk(r1)→Pk(r2). This is option 1.

## Key Points

- In a many-to-one relationship A→B, each A chooses one B, so key(A) functionally determines key(B).

## Why the other options are incorrect

Pk(r2)→Pk(r1) would say one r2 entity determines a single r1 entity, contradicting the `many` side. Having both directions describes one-to-one behavior. The disjunction in option 4 does not state the specific dependency implied by the given direction.
