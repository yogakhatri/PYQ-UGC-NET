# Question 150

*UGC NET CS · 2019 Dec Paper 1 And 2 · Relational Database Design · Functional Dependencies, Keys and Normalization*

Suppose R is decomposed into R1(A,B,C), with f1={A→B, A→C}, and R2(A,D,E), with f2={A→D, D→E}. Which statement best describes this decomposition?

- **1.** The decomposition preserves all dependencies in F
- **2.** R1 and R2 both have 2NF as their highest normal form
- **3.** R1 has 2NF as its highest normal form and R2 has 3NF as its highest normal form
- **4.** R1 is in 3NF (indeed BCNF) and R2 has 2NF as its highest normal form

> [!TIP]
> **Correct answer: 4. R1 is in 3NF (indeed BCNF) and R2 has 2NF as its highest normal form**

## Solution

In R1(A,B,C), A determines B and C, so A is a key and every nontrivial projected dependency has a superkey determinant. R1 is therefore in BCNF, and consequently also in 3NF. In R2(A,D,E), A is the key and D→E creates no partial dependency because the key has one attribute, so R2 is in 2NF. But D is not a superkey and E is nonprime, so D→E violates 3NF; 2NF is R2's highest normal form. Thus option 4 gives the precise highest-normal-form description.

## Key Points

- Assess each component using projected FDs and report its highest normal form; also test preservation by closure under the union of projections.

## Why the other options are incorrect

The decomposition does not preserve BC→D: under the union of the projected dependencies, (BC)+ remains BC, so option 1 is false. Option 3 reverses the normal forms. Option 2 is only loosely true in the hierarchy because BCNF implies 2NF; the exam's mutually exclusive wording uses ‘in 2NF’ to mean highest normal form, under which R1 is BCNF/3NF and option 4 is the intended precise answer.
