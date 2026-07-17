# Question 23

*UGC NET CS · 2014 Dec Paper 3 · Regular Language Models · Pumping-Lemma Nonregularity*

Given L₁ = {(ab)ⁿaᵏ | n > k, k ≥ 0} and L₂ = {aⁿbᵐ | n ≠ m}, what can be shown using the pumping lemma for regular languages?

- **A.** L 1 is regular and L 2 is not regular.
- **B.** L 1 is not regular and L 2 is regular.
- **C.** L 1 is regular and L 2 is regular.
- **D.** L 1 is not regular and L 2 is not regular.

> [!TIP]
> **Correct answer: D. L 1 is not regular and L 2 is not regular.**

## Solution

Both languages compare two unbounded counts. For L₁, encode each block `ab` as x and the trailing a as y. If L₁ were regular, inverse homomorphism and intersection with x*y* would make {xⁿyᵏ | n>k} regular, but pumping a string such as xᵖy^(p−1) destroys the strict inequality. Thus L₁ is not regular. For L₂, suppose it were regular. Since a*b* is regular, subtracting L₂ from a*b* would produce {aⁿbⁿ | n≥0}, contradicting the known nonregularity of the equal-count language. Therefore L₂ is also not regular.

## Key Points

- A fixed repeated block can still participate in a nonregular count comparison; use closure properties to reduce the language to a standard nonregular form.

## Why the other options are incorrect

A and C incorrectly call L₁ regular merely because `(ab)` is a fixed block; the comparison n>k still requires unbounded memory. B and C incorrectly call L₂ regular; using n≠m instead of n=m does not remove the unbounded comparison because regular languages are closed under relative complement.
