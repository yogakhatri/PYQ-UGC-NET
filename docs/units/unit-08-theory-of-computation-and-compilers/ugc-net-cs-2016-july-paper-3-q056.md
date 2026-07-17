# Question 56

*UGC NET CS · 2016 July Paper 3 · Context-Free Language · Closure Properties of Language Classes*

Let L = {0ⁿ1ⁿ | n ≥ 0} be a context-free language. Which of the following is correct?

- **1.** L̄ is context-free and Lᵏ is not context-free for any k ≥ 1.
- **2.** L̄ is not context-free and Lᵏ is context-free for any k ≥ 1.
- **3.** Both L̄ and Lᵏ, for every k ≥ 1, are context-free.
- **4.** Both L̄ and Lᵏ, for every k ≥ 1, are not context-free.

> [!TIP]
> **Correct answer: 3. Both L̄ and Lᵏ, for every k ≥ 1, are context-free.**

## Solution

First consider Lᵏ. Context-free languages are closed under concatenation, so concatenating L with itself any fixed positive number k of times still gives a context-free language. Now consider the complement L̄ over {0,1}*. Although CFLs are not closed under complement in general, this particular complement is context-free. A string outside L either is not of the form 0*1* (for example, it contains 10), or it is 0ⁱ1ʲ with i < j, or it is 0ⁱ1ʲ with i > j. The first set is regular and the other two are context-free; their finite union is context-free. Thus both L̄ and every fixed Lᵏ are context-free, so option 3 is correct.

## Key Points

- Closure failure is not a universal negative.
- Prove properties of the particular language: CFLs are closed under finite concatenation, and this specific complement can be decomposed into simple CFLs.

## Why the other options are incorrect

Options 1, 2, and 4 each incorrectly declare one or both of these languages non-context-free. The trap is to use the general statement 'CFLs are not closed under complement' as though it proved that the complement of every CFL is non-context-free; non-closure only says that some counterexamples exist.
