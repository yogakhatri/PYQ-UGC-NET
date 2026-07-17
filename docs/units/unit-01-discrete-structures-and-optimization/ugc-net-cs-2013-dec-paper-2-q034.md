# Question 34

*UGC NET CS · 2013 Dec Paper 2 · Mathematical Logic · Quantifiers and Divisibility*

Let P(m, n) be the statement “m divides n” where the universe of discourse for both the variables is the set of positive integers. Determine the truth values of each of the following propositions : I. ∀m ∀n P(m, n), II. ∃m ∀n P(m, n)

- **A.** Both I and II are true
- **B.** Both I and II are false
- **C.** I – false & II – true
- **D.** I – true & II – false

> [!TIP]
> **Correct answer: C. I – false & II – true**

## Solution

Statement I says every positive integer m divides every positive integer n, which is false; for example, 2 does not divide 1. Statement II asks whether one positive integer divides every positive integer. Choosing m=1 makes P(1,n) true for every n, so II is true.

## Key Points

- Quantifier strategy: refute ∀ with a counterexample; prove ∃ by giving a witness.
- Here 2∤1, but 1 divides all positive integers.

## Why the other options are incorrect

A and D incorrectly make the universal statement I true. B overlooks the witness m=1 for the existential statement II. One counterexample disproves a universal claim, while one valid witness proves an existential claim.
