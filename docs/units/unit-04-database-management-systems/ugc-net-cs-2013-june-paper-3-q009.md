# Question 9

*UGC NET CS · 2013 June Paper 3 · Normalization for Relational Databases · Partial Dependencies and Second Normal Form*

For relation R(a,b,c,d), whose attribute domains contain only atomic values, the functional dependencies a -> c and b -> d hold. The relation is:

- **A.** In 1NF but not in 2NF
- **B.** In 2NF but not in 3NF
- **C.** In 3NF
- **D.** In 1NF

> [!TIP]
> **Correct answer: A. In 1NF but not in 2NF**

## Solution

Atomic attribute values establish 1NF. From a→c and b→d, the pair {a,b} determines all attributes and is the candidate key under the stated dependencies. But c depends on only a and d depends on only b-each is a nonprime attribute depending on a proper subset of the composite key. These partial dependencies violate 2NF. Hence the relation is in 1NF but not 2NF.

## Key Points

- 2NF forbids a nonprime attribute from depending on only part of a composite candidate key.

## Why the other options are incorrect

B and C require 2NF, which the partial dependencies violate. D merely says 1NF and is less precise than A because the information is sufficient to identify the 2NF violation.
