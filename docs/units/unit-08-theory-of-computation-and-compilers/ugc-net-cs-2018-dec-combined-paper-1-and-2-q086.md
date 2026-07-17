# Question 86

*UGC NET CS · 2018 Dec Paper 1 And 2 · Context-Free Language · Closure Properties of Context-Free Languages*

Let R be any regular language and L₁,L₂ any context-free languages. Which statement is guaranteed to be correct?

- **1.** complement(L₁) is context-free
- **2.** complement(L₁∪L₂)−R is context-free
- **3.** L₁∩L₂ is context-free
- **4.** L₁−R is context-free

> [!TIP]
> **Correct answer: 4. L₁−R is context-free**

## Solution

Language difference satisfies L₁−R=L₁∩complement(R). Regular languages are closed under complement, and context-free languages are closed under intersection with a regular language. Therefore L₁−R is always context-free, so option 4 is correct.

## Key Points

- CFL-safe operations include union and intersection with a regular language; complement and CFL–CFL intersection are not closed in general.

## Why the other options are incorrect

CFLs are not closed under complement, so option 1 is not guaranteed. They are not closed under intersection with another CFL, so option 3 fails. In option 2, L₁∪L₂ is context-free, but complementing it is not guaranteed to remain context-free; subtracting a regular language does not repair that general failure.
