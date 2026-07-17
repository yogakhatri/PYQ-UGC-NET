# Question 33

*UGC NET CS · 2013 Dec Paper 2 · Boolean Algebra · Canonical Sum of Products*

The canonical sum-of-products expansion for F(x,y,z)=(x+y)z̄ is:

- **A.** x̄ȳz + xyz̄ + x̄yz̄
- **B.** xyz + xyz̄ + xȳz̄
- **C.** xȳz̄ + x̄ȳz̄ + xyz̄
- **D.** xyz̄ + xȳz̄ + x̄yz̄

> [!TIP]
> **Correct answer: D. xyz̄ + xȳz̄ + x̄yz̄**

## Solution

F=(x+y)z̄ is 1 exactly when z=0 and at least one of x,y is 1. The satisfying assignments are (x,y,z)=(1,1,0),(1,0,0),(0,1,0). Their minterms are xyz̄, xȳz̄ and x̄yz̄, whose sum is option D.

## Key Points

- For canonical SOP, list every input row making F=1 and write one minterm containing all variables for each row.

## Why the other options are incorrect

Any term containing uncomplemented z represents a row where z=1, but F must then be 0. Option C includes x̄ȳz̄, where x+y=0. The other options likewise include a false row or omit a required true row.
