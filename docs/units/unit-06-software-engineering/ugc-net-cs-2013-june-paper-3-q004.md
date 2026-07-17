# Question 4

*UGC NET CS · 2013 June Paper 3 · Software Testing · Equivalence Partitioning*

Equivalence partitioning is a __________ method that divides the input domain of a program into classes of data from which test cases can be derived.

- **A.** White-box testing
- **B.** Black-box testing
- **C.** Orthogonal array testing
- **D.** Stress testing

> [!TIP]
> **Correct answer: B. Black-box testing**

## Solution

Equivalence partitioning derives tests from the externally visible input domain, without requiring knowledge of the program's internal code. Inputs expected to behave similarly are grouped into valid and invalid equivalence classes, and one or a few representatives are tested from each class. That makes it a black-box test-design method.

## Key Points

- Equivalence partitioning reduces black-box tests by choosing representatives from behaviorally equivalent input classes.

## Why the other options are incorrect

White-box testing derives cases from control flow or code structure. Orthogonal-array testing systematically samples combinations of factors and is a separate technique. Stress testing pushes a system beyond normal resource or workload limits rather than partitioning its input domain.
