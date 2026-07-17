# Question 43

*UGC NET CS · 2015 Dec Paper 3 · Knowledge Representation · Horn clauses*

A horn clause is __________.

- **1.** A clause in which no variables occur in the expression
- **2.** A clause that has at least one negative literal
- **3.** A disjunction of a number of literals
- **4.** A clause that has at most one positive literal

> [!TIP]
> **Correct answer: 4. A clause that has at most one positive literal**

## Solution

A Horn clause is a disjunction of literals containing at most one positive (unnegated) literal. A definite Horn clause has exactly one positive literal, while a goal clause may have none. This restricted form supports efficient rule-based inference.

## Key Points

- Horn clause: zero or one positive literal.

## Why the other options are incorrect

Horn clauses may contain variables, so option 1 is false. They need not contain a negative literal, so option 2 is too restrictive. Option 3 describes any clause and omits the defining at-most-one-positive condition.
