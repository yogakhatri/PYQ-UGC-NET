# Question 7

*UGC NET CS · 2015 Dec Paper 3 · Language Design and Translation Issues · Logic Programming and Prolog Backtracking*

Given `father(X,Y) :- parent(X,Y), male(X).` and the facts `parent(sally,bob)`, `parent(jim,bob)`, `parent(alice,jane)`, `parent(thomas,jane)`, `male(bob)`, `male(jim)`, `female(salley)`, and `female(alice)`, how many atoms are matched to X before `father(X,jane)` reports a result?

- **1.** 1
- **2.** 2
- **3.** 3
- **4.** 4

> [!TIP]
> **Correct answer: No listed answer — the query never reports a result from the printed facts**

## Solution

Using the intended lowercase constants, `parent(X,jane)` first binds X=alice, but `male(alice)` is absent, so Prolog backtracks. It next binds X=thomas, but `male(thomas)` is also absent. No further parent of jane exists, so `father(X,jane)` fails rather than reporting a result. Therefore the requested number ‘before a result’ is undefined and none of 1–4 is correct.

## Key Points

- Trace Prolog left to right and follow backtracking; a parent match must also satisfy `male(X)`.

## Why the other options are incorrect

Every numeric option presupposes a successful derivation. The facts declare only bob and jim male, and neither is listed as a parent of jane. Strict Prolog would introduce another source defect because the printed capitalized names are variables, not atoms; normalizing them to atoms still leaves the query unsatisfied.
