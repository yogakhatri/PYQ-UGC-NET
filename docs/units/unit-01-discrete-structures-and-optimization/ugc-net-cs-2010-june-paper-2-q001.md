# Question 1

*UGC NET CS · 2010 June Paper 2 · Sets and Relations · Equivalence-relation properties*

“x¹ is a clone of x” means x¹ is identical to x in height, weight, and complexion. Given that these form a complete attribute set for the entity, is cloning an equivalence relation?

- **A.** The statement is true
- **B.** The statement is false
- **C.** The truth value of the statement cannot be computed
- **D.** None of these 2. ‘R is a robot of M’ means R can perform some of the tasks that otherwise M would do and R is unable to do anything else. Which of the following is the most appropriate representation to model this situation ? (A) (B) (C) (D) None of these

> [!TIP]
> **Correct answer: A. The statement is true**

## Solution

Represent each entity by the complete tuple (height, weight, complexion). Equality of tuples is reflexive (every tuple equals itself), symmetric (if x¹ equals x, then x equals x¹), and transitive (two tuples equal to the same tuple equal each other). Therefore 'is a clone of' is an equivalence relation under the stated definition.

## Key Points

- Equality on a complete attribute tuple is always an equivalence relation.

## Why the other options are incorrect

The complete attribute set makes the truth value decidable, so C is false. Since all three equivalence properties follow from tuple equality, B and D are also false.
