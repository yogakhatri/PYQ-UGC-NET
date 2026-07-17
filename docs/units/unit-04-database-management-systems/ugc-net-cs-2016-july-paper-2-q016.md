# Question 16

*UGC NET CS · 2016 July Paper 2 · Data Modeling · Entity-integrity constraint*

In RDBMS, the constraint that no key attribute (column) may be NULL is referred to as :

- **1.** Referential integrity
- **2.** Multi-valued dependency
- **3.** Entity Integrity
- **4.** Functional dependency

> [!TIP]
> **Correct answer: 3. Entity Integrity**

## Solution

The entity-integrity rule requires every tuple in a relation to be uniquely identifiable. Consequently, no component of the relation's primary key may be NULL; otherwise the tuple's identity would be unknown or incomplete. This is entity integrity, option 3.

## Key Points

- Entity integrity → primary key is unique and never NULL; referential integrity → valid foreign-key references.

## Why the other options are incorrect

Referential integrity governs foreign-key references to keys in another or the same relation. Functional and multivalued dependencies describe relationships among attribute values and are used in normalization; they are not the rule prohibiting NULL primary-key components.
