# Question 6

*UGC NET CS · 2010 June Paper 2 · Mathematical Logic · Propositional and Predicate Logic*

The logic expression for the output of the circuit shown in the figure is

- **A.** – A – C + – B – C + CD
- **B.** A – C + B – C + – CD
- **C.** ABC + – C – D
- **D.** – A – B + – B – C + – C – D

> [!TIP]
> **Correct answer: No listed option — the shown circuit simplifies to C + A̅B̅D**

## Solution

All four gates are NOR gates. Let p=(A+B)̅, q=(p+C)̅, and r=(C+D)̅. The output is F=(q+r)̅=q̅r̅=(p+C)(C+D). Using (X+C)(C+D)=C+XD gives F=C+pD=C+A̅B̅D. Direct truth-table checking confirms this expression, but it matches none of A–D.

## Key Points

- Label each NOR output and apply De Morgan's law from the final gate backward.

## Why the other options are incorrect

Each listed expression has a different truth table. For example, when C=1 the actual output is always 1, whereas several choices still depend on A, B, or D.
