# Question 18

*UGC NET CS · 2014 Dec Paper 2 · Entity-Relationship Model · Converting Weak Entities to Strong Entities*

What kind of mechanism is to be taken into account for converting a weak entity set into strong entity set in entity-relationship diagram ?

- **A.** Generalization
- **B.** Aggregation
- **C.** Specialization
- **D.** Adding suitable attributes

> [!TIP]
> **Correct answer: D. Adding suitable attributes**

## Solution

A weak entity lacks a complete key of its own and is identified using its partial key together with the owner's key through an identifying relationship. To make it strong, give it suitable identifying attribute(s) that form an independent primary key. It can then be identified without relying on an owner entity.

## Key Points

- Weak→strong requires an independent key, created by adding suitable identifying attributes.

## Why the other options are incorrect

Generalization and specialization organize superclass/subclass relationships. Aggregation treats a relationship set as a higher-level entity. None of those supplies the missing independent identifier.
