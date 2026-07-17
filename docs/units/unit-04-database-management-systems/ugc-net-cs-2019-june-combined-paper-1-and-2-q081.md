# Question 81

*UGC NET CS · 2019 June Paper 1 And 2 · Data Modeling · Relational algebra and calculus*

Which pairs have the same expressive power as relational query languages? (a) Relational algebra and unrestricted domain relational calculus. (b) Relational algebra and unrestricted tuple relational calculus. (c) Relational algebra and domain relational calculus restricted to safe expressions. (d) Relational algebra and tuple relational calculus restricted to safe expressions.

- **A.** (a) and (b) only
- **B.** (c) and (d) only
- **C.** (a) and (c) only
- **D.** (b) and (d) only

> [!TIP]
> **Correct answer: B. (c) and (d) only**

## Solution

Codd's theorem establishes equivalence between relational algebra and the safe, or domain-independent, forms of relational calculus. Safety prevents a calculus expression from producing an unbounded result based on values outside the active database domain. Consequently both safe domain relational calculus and safe tuple relational calculus have the expressive power of relational algebra, making (c) and (d) correct.

## Key Points

- Relational algebra is expressively equivalent to safe tuple relational calculus and safe domain relational calculus.

## Why the other options are incorrect

Statements (a) and (b) omit the safety restriction. Unrestricted calculus can describe non-domain-independent results and is therefore not equivalent to ordinary relational algebra.
