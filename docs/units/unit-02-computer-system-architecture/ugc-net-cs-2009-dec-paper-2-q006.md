# Question 6

*UGC NET CS · 2009 Dec Paper 2 · Boolean Algebra · Duality Principle*

The simplified form of the Boolean expression (X + Y + XY) ( X + Z) is

- **A.** X + Y + ZX + Y
- **B.** XY – YZ
- **C.** X + YZ
- **D.** XZ + Y

> [!TIP]
> **Correct answer: C. X + YZ**

## Solution

First use absorption: X+Y+XY = X+Y because Y+XY=Y. Then apply (A+B)(A+C)=A+BC: (X+Y)(X+Z)=X+YZ. Hence the simplified expression is X+YZ.

## Key Points

- Absorption followed by (X+Y)(X+Z)=X+YZ gives the result in two steps.

## Why the other options are incorrect

The other expressions either retain redundant terms, introduce subtraction (not Boolean OR/AND simplification), or omit required minterms.
