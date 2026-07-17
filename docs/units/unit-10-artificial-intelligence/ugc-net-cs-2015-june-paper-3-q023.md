# Question 23

*UGC NET CS · 2015 June Paper 3 · Logic Programming · Prolog Variables, Scope, and Typing*

Which of the following is false for the programming language PROLOG ?

- **1.** A PROLOG variable can only be assigned to a value once
- **2.** PROLOG is a strongly typed language
- **3.** The scope of a variable in PROLOG is a single clause or rule
- **4.** The scope of a variable in PROLOG is a single query

> [!TIP]
> **Correct answer: 2. PROLOG is a strongly typed language**

## Solution

Standard Prolog variables are logical variables that become bound through unification; they do not carry fixed declared types in the conventional strongly typed language sense. Terms are tagged and type errors can be detected by predicates at run time, but Prolog is dynamically typed rather than statically strongly typed. Thus statement 2 is the false textbook claim.

## Key Points

- Prolog variables are scoped to a clause/query and bound by unification; standard Prolog has no static declared variable types.

## Why the other options are incorrect

Within one proof branch, a logical variable is single-assignment, though backtracking can undo a binding. A variable's identity is local to its clause, and variables written in a query belong to that query. These make statements 1, 3, and 4 valid in the intended operational model.
