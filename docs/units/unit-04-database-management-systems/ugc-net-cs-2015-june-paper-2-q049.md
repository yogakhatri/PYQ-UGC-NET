# Question 49

*UGC NET CS · 2015 June Paper 2 · Data Modeling · Weak Entities and Existence Dependency*

Which of the following statements is FALSE about weak entity set ?

- **1.** Weak entities can be deleted automatically when their strong entity is deleted.
- **2.** Weak entity set avoids the data duplication and consequent possible inconsistencies caused by duplicating the key of the strong entity.
- **3.** A weak entity set has no primary keys unless attributes of the strong entity set on which it depends are included.
- **4.** Tuples in a weak entity set are not partitioned according to their relationship with tuples in a strong entity set.

> [!TIP]
> **Correct answer: 4. Tuples in a weak entity set are not partitioned according to their relationship with tuples in a strong entity set.**

## Solution

Every weak entity is existence-dependent on an owner in a strong entity set and participates totally in the identifying relationship. Grouping weak entities by their owner therefore partitions them into owner-specific subsets. Statement 4 denies this partitioning and is false.

## Key Points

- A weak entity has a partial key, is totally dependent on one owner, and is identified by owner key + partial key.

## Why the other options are incorrect

Deleting an owner can cascade to its existence-dependent weak entities, so statement 1 is valid. Modeling the owner through the identifying relationship avoids redundantly treating its key as an independent descriptive attribute, supporting statement 2's conceptual point. A weak entity's relational primary key must combine its partial key with the owner's key, so statement 3 is also valid. The owner's key is still stored as a foreign-key component when the ER model is mapped to relations.
