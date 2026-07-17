# Question 88

*UGC NET CS · 2020 Nov With Answers · Knowledge Representation and Logic · Conjunctive Normal Form*

What kind of clauses are available in conjunctive normal form?

- **1.** Disjunction of literals
- **2.** Disjunction of variables
- **3.** Conjunction of literals
- **4.** Conjunction of variables

> [!TIP]
> **Correct answer: 1. Disjunction of literals**

## Solution

Conjunctive normal form is a conjunction of clauses, and each clause is a disjunction of literals. A literal is either an atomic proposition or its negation. For example, (p∨¬q)∧(r∨s∨¬t) is in CNF: the parenthesized groups are disjunctions of literals. Therefore option 1.

## Key Points

- CNF has AND between clauses and OR inside each clause; the clause elements are literals.

## Why the other options are incorrect

Variables alone exclude negated occurrences and are too narrow. A conjunction of literals may be one special CNF formula, but it is not the general structure of each CNF clause; conjunction connects the clauses to one another.
