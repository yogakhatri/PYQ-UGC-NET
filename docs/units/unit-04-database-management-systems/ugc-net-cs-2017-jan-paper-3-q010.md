# Question 10

*UGC NET CS · 2017 Jan Paper 3 · Relational Database Design · Partial Dependencies and Second Normal Form*

For a database relation R(A, B, C, D) where the domains of A, B, C and D include only atomic values, only the following functional dependencies and those that can be inferred from them are : A→C B→D The relation R is in _______.

- **1.** First normal form but not in second normal form.
- **2.** Both in first normal form as well as in second normal form.
- **3.** Second normal form but not in third normal form.
- **4.** Both in second normal form as well as in third normal form.

> [!TIP]
> **Correct answer: 1. First normal form but not in second normal form.**

## Solution

Because every domain contains atomic values, R satisfies first normal form. From A→C and B→D, neither A nor B alone determines all four attributes, but (AB)+ = {A,B,C,D}; hence AB is the candidate key. The non-prime attribute C depends on the proper subset A of AB, and D depends on the proper subset B. These partial dependencies violate second normal form. R is therefore in 1NF but not 2NF, so option 1 is correct.

## Key Points

- For a composite key, 2NF forbids a non-prime attribute from depending on only a proper subset of that key.

## Why the other options are incorrect

Options 2–4 all require 2NF, which is impossible while non-prime attributes C and D depend on only parts of the composite key AB. Since 2NF already fails, claims about 3NF are unnecessary.
