# Question 101

*UGC NET CS · 2019 Dec Paper 1 And 2 · Unsolvable Problems and Computational Complexity · Turing-Machine Language Equality and Inclusion*

Consider: S1: There is no algorithm that decides whether arbitrary Turing machines M1 and M2 accept the same language. S2: For arbitrary Turing machines M1 and M2, deciding whether L(M1) ⊆ L(M2) is undecidable. Which statement(s) are correct?

- **1.** Only S1
- **2.** Only S2
- **3.** Both S1 and S2
- **4.** Neither S1 nor S2

> [!TIP]
> **Correct answer: 3. Both S1 and S2**

## Solution

Both questions ask nontrivial semantic properties of languages recognized by arbitrary Turing machines. If language equality were decidable, compare M with a fixed machine accepting the empty language; this would decide whether L(M)=∅, an undecidable problem. If inclusion were decidable, test L(M)⊆∅ against that same fixed machine, again deciding emptiness. Thus both equality and inclusion are undecidable, so option 3 is correct.

## Key Points

- To prove a Turing-machine language property undecidable, assume its decider and use a fixed comparison language to decide a known undecidable property.

## Why the other options are incorrect

Options 1 and 2 each deny one of two valid reductions to the undecidable emptiness problem. Option 4 would require algorithms for both properties, contradicting those reductions. The machines being finite descriptions does not make arbitrary properties of their accepted languages decidable.
