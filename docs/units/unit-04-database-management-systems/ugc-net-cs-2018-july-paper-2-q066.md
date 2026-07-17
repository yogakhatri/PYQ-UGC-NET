# Question 66

*UGC NET CS · 2018 July Paper 2 · Normalization · Partial Dependencies and Second Normal Form*

For a relation R(a,b,c,d), all attribute domains contain only atomic values. The only nontrivial functional dependencies, and those inferred from them, are a→c and b→d. The relation is in ________.

- **1.** First normal form but not in second normal form
- **2.** Second normal form but not in third normal form
- **3.** Third normal form
- **4.** BCNF

> [!TIP]
> **Correct answer: 1. First normal form but not in second normal form**

## Solution

All values are atomic, so R is in 1NF. Neither a nor b alone determines all attributes, but (ab)+={a,b,c,d}; hence ab is the candidate key. The dependencies a→c and b→d make nonprime attributes c and d depend on proper subsets of the composite key. These partial dependencies violate 2NF. Thus R is in 1NF but not 2NF, option 1.

## Key Points

- 2NF forbids a nonprime attribute from depending on only part of a composite candidate key.

## Why the other options are incorrect

Because 2NF already fails, the relation cannot be claimed to be in 3NF or BCNF. Option 2 is also impossible: the explicit partial dependencies prevent the relation from reaching 2NF in the first place.
