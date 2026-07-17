# Question 85

*UGC NET CS · 2019 June Paper 1 And 2 · Data Modeling · Foreign Keys and Referential Integrity*

Which of the following key constraints is required for the functioning of a foreign key in the context of relational databases?

- **1.** Unique key
- **2.** Primary key
- **3.** Candidate key
- **4.** Check key

> [!TIP]
> **Correct answer: 2. Primary key**

## Solution

In the conventional relational-database formulation used by this question, a foreign key in the child relation references the primary key of a parent relation. This lets every non-null foreign-key value identify an existing parent tuple and enforces referential integrity. Therefore the expected key constraint is the primary key.

## Key Points

- Exam convention: foreign key -> referenced primary key.
- Broader SQL rule: the referenced columns must be protected by a primary-key or suitable unique constraint.

## Why the other options are incorrect

A check constraint tests a local condition and cannot establish a cross-table reference. Candidate key is the broader logical category from which a primary key is chosen, not the named constraint expected here. A UNIQUE constraint can also be a legal reference target in SQL systems, so option 1 is technically possible in broader SQL practice, but it is not the conventional answer to this wording.

## Additional Information

The precise generalized relational definition permits a foreign key to reference a candidate key; this card preserves that nuance while answering the paper's intended convention.
