# Question 9

*UGC NET CS · 2016 July Paper 3 · Relational Algebra · Join, Projection and Semijoin Equivalences*

For R(A,B) and S(B,C), compare these relational-algebra queries: I. π_{A,B}(R ⋈ S); II. R ⋈ π_B(S); III. R ∩ (π_A(R) × π_B(S)); IV. π_{A,R.B}(R × S), where R.B is column B of R. Which queries are equivalent?

- **1.** I, III and IV are the same query.
- **2.** II, III and IV are the same query.
- **3.** I, II and IV are the same query.
- **4.** I, II and III are the same query.

> [!TIP]
> **Correct answer: 4. I, II and III are the same query.**

## Solution

Query I projects A and B after the natural join, so it keeps exactly those R tuples whose B value appears in S. Query II joins R with π_B(S), producing the same filter. In III, π_A(R)×π_B(S) contains every R-side A paired with every B occurring in S; intersecting with R again keeps exactly the R tuples whose B occurs in S. Thus I, II, and III are equivalent.

## Key Points

- Natural-join then project R's attributes is a semijoin; intersecting R with compatible A×B values expresses the same filter.

## Why the other options are incorrect

Query IV projects A and R.B from R×S. If S is nonempty, every R tuple participates in the product, so IV reduces to R under set semantics even when its B has no match in S. Therefore any choice containing IV is not generally equivalent to the first three.
