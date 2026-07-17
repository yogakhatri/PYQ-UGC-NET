# Question 19

*UGC NET CS · 2017 Nov Paper 2 · Normalization for Relational Databases · Normal Forms and Modification Anomalies*

In RDBMS, different classes of relations are created using __________ technique to prevent modification anomalies.

- **1.** Functional Dependencies
- **2.** Data integrity
- **3.** Referential integrity
- **4.** Normal Forms

> [!TIP]
> **Correct answer: 4. Normal Forms**

## Solution

Normalization organizes a relation into successively stricter normal forms and, when needed, decomposes it into smaller relations. The purpose is to reduce redundancy and prevent insertion, deletion, and update anomalies. Therefore 'Normal Forms' is the intended technique, giving option 4.

## Key Points

- Functional dependencies diagnose redundancy; normalization uses them to produce relations satisfying 1NF, 2NF, 3NF, BCNF, and higher forms.

## Why the other options are incorrect

Functional dependencies are the facts used to test and derive normal forms, not the name of the resulting classes of relations. Data integrity and referential integrity are constraint goals; neither is the decomposition/classification technique asked for.
