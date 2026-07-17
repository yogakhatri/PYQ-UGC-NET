# Question 64

*UGC NET CS · 2018 July Paper 2 · Data Modeling and Normalization · ER-to-Relational Mapping and First Normal Form*

Relations produced from an E-R model will always be in ________.

- **1.** 1 NF
- **2.** 2 NF
- **3.** 3 NF
- **4.** 4 NF

> [!TIP]
> **Correct answer: 1. 1 NF**

## Solution

In the standard ER-to-relational mapping, composite attributes are broken into their components and each multivalued attribute is represented in a separate relation. The resulting table cells therefore contain atomic single values, which guarantees first normal form. Higher normal forms depend on functional and multivalued dependencies and are not guaranteed merely by performing the mapping. Thus option 1 is the safest always-true answer.

## Key Points

- ER mapping guarantees atomic relation cells (1NF); normalization beyond 1NF requires dependency analysis.

## Why the other options are incorrect

Second, third, and fourth normal forms impose progressively stronger dependency conditions. A good conceptual design may yield 3NF or BCNF tables, but the phrase `will always` requires only the property guaranteed by the mechanical mapping: atomic values and hence 1NF.

## References

- [University of Jyväskylä — Introduction to normalization](https://tim.jyu.fi/view/kurssit/tie/itka2004/course/sections/5/03_ex51_normalisointi_johdatus/en-US)
