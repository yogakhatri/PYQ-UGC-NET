# Question 34

*UGC NET CS · 2013 June Paper 3 · Knowledge Representation and Reasoning · Horn Clauses*

Horn clauses are special kinds of propositions which can be described as

- **A.** Single atomic proposition on left side.
- **B.** Single or multiple atomic proposition on left side.
- **C.** A single atomic proposition on left side and a single atomic proposition on right side.
- **D.** A single atomic proposition on left side or an empty left side.

> [!TIP]
> **Correct answer: D. A single atomic proposition on left side or an empty left side.**

## Solution

A Horn clause contains at most one positive literal. In logic-programming notation it is written with one head atom on the left of the rule arrow and a conjunction of body atoms on the right; a goal clause may have no head at all. Thus the left side is either a single atomic proposition or empty, matching D.

## Key Points

- Horn means at most one positive literal: one rule head or an empty head for a goal clause.

## Why the other options are incorrect

A excludes valid goal clauses with an empty head. B permits several head atoms, which would create several positive literals and cease to be Horn. C unnecessarily restricts the body to a single atom, whereas a Horn rule may have a conjunction of many body atoms.
