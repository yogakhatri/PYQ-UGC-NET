# Question 11

*UGC NET CS · 2013 Dec Paper 2 · Data Modeling · Domain and CHECK Constraints*

The student marks should not be greater than 100. This is

- **A.** Integrity constraint
- **B.** Referential constraint
- **C.** Over-defined constraint
- **D.** Feasible constraint

> [!TIP]
> **Correct answer: A. Integrity constraint**

## Solution

The rule marks <= 100 restricts the allowed values of the marks attribute and preserves valid database state. It is a domain/check integrity constraint and can be enforced with a CHECK condition, usually together with a lower bound such as marks >= 0.

## Key Points

- A range rule on one attribute is a domain integrity constraint; a relationship between table keys is referential integrity.

## Why the other options are incorrect

Referential integrity concerns foreign-key values matching referenced keys. 'Over-defined' and 'feasible' are not the standard database constraint types that describe this upper-bound rule.
