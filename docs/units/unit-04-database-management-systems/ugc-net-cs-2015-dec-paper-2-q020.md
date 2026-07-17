# Question 20

*UGC NET CS · 2015 Dec Paper 2 · Relational Model · Attribute Closure and Candidate Keys*

For relation R={A,B,C,D,E,F,G}, the functional dependencies are F={AD→E, BE→F, B→C, AF→G}. Which option is a candidate key?

- **1.** A
- **2.** AB
- **3.** ABC
- **4.** ABD

> [!TIP]
> **Correct answer: 4. ABD**

## Solution

Attributes A, B, and D never occur on the right-hand side of any dependency, so every candidate key must contain all three. Compute (ABD)+: AD→E adds E; B→C adds C; BE→F adds F; and then AF→G adds G. Thus (ABD)+={A,B,C,D,E,F,G}. It is minimal because removing A, B, or D leaves an attribute that cannot be derived. Therefore ABD is a candidate key.

## Key Points

- Find mandatory attributes from those absent on all RHSs, then compute closure and test minimality.

## Why the other options are incorrect

A alone derives nothing. AB cannot derive D, and ABC still cannot derive D; without D it cannot activate AD→E. Although a superset of a key may be a superkey, a candidate key must be minimal.
