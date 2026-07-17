# Question 9

*UGC NET CS · 2017 Nov Paper 2 · Mathematical Logic · Negating Quantifiers*

Negation of the proposition ∃x H(x) is:

- **1.** ∃x ¬H(x)
- **2.** ∀x ¬H(x)
- **3.** ∀x H(x)
- **4.** ¬x H(x)

> [!TIP]
> **Correct answer: 2. ∀x ¬H(x)**

## Solution

The statement ∃x H(x) says that at least one object has property H. Its negation says that no object has property H, which is equivalent to saying every object fails to have H: ¬∃x H(x) ≡ ∀x ¬H(x). Hence option 2 is correct.

## Key Points

- Move negation through a quantifier by switching ∃ and ∀, then negate the predicate.

## Why the other options are incorrect

Option 1 says there exists an object without H; that can be true even when another object has H. Option 3 is the much stronger claim that every object has H. Option 4 is not a well-formed quantified formula because x is left unbound.
