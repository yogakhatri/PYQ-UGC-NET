# Question 24

*UGC NET CS · 2012 June Paper 2 · Software Design · Cohesion and Coupling*

In a function oriented design, we

- **A.** minimize cohesion and maximize coupling
- **B.** maximize cohesion and minimize coupling
- **C.** maximize cohesion and maximize coupling
- **D.** minimize cohesion and minimize coupling

> [!TIP]
> **Correct answer: B. maximize cohesion and minimize coupling**

## Solution

Function-oriented design decomposes a system into modules that perform coherent functions. Good modules have high cohesion—their elements work toward one focused purpose—and low coupling—modules depend on each other through small, clear interfaces. This localizes change and simplifies testing and reuse.

## Key Points

- Good modular design maximizes cohesion within modules and minimizes coupling between them.

## Why the other options are incorrect

Low cohesion mixes unrelated responsibilities. High coupling spreads the effect of changes across modules. Any option containing either undesirable property fails the design goal.
