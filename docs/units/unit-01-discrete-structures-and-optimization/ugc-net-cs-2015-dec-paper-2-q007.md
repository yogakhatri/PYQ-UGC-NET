# Question 7

*UGC NET CS · 2015 Dec Paper 2 · Mathematical Logic · Predicates and Quantifiers*

Let P(m,n) mean ‘m divides n’, where both variables range over the positive integers. Determine the truth values of: (a) ∃m ∀n P(m,n), (b) ∀n P(1,n), and (c) ∀m ∀n P(m,n).

- **1.** (a) - True; (b) - True; (c) - False
- **2.** (a) - True; (b) - False; (c) - False
- **3.** (a) - False; (b) - False; (c) - False
- **4.** (a) - True; (b) - True; (c) - True

> [!TIP]
> **Correct answer: 1. (a) - True; (b) - True; (c) - False**

## Solution

For (a), one positive integer must divide every positive integer; choosing m=1 works, so ∃m∀n P(m,n) is true. Statement (b), ∀n P(1,n), says exactly that 1 divides every positive integer, so it is true. Statement (c) says every positive integer divides every positive integer, which is false; for example, 2 does not divide 1. The truth pattern is True, True, False.

## Key Points

- Read quantifiers in order and prove existential claims with a witness; refute universal claims with a counterexample.

## Why the other options are incorrect

Options 2 and 3 incorrectly make (b) false, while option 4 incorrectly makes the universal claim (c) true. Quantifier order matters: (a) needs one suitable m, not every m.
