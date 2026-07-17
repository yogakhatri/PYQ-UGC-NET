# Question 28

*UGC NET CS · 2015 Dec Paper 3 · Context-Free Language · Context-Free Language Classification*

Let L1={a^n b a^n | n>0} and L2={a^n b a^n b^(n+1) | n>0}. Which statement is correct?

- **1.** L1 is context free language and L2 is not context free language
- **2.** L1 is not context free language and L2 is context free language
- **3.** Both L1 and L2 are context free languages
- **4.** Both L1 and L2 are not context free languages

> [!TIP]
> **Correct answer: 1. L1 is context free language and L2 is not context free language**

## Solution

L1 is context-free; for example, S→aSa | aba generates exactly a^n b a^n for n>0. L2 requires the same n to control the first a-block, the second a-block, and the final b-block (up to the fixed +1), which a single pushdown stack cannot enforce. A CFL pumping-lemma argument on a^p b a^p b^(p+1) shows that pumping changes at most two adjacent regions while leaving a third count fixed, breaking the required equalities. Thus L2 is not context-free.

## Key Points

- One mirrored equality is context-free; three separated counts tied to the same n generally require more than one stack.

## Why the other options are incorrect

Options 2 and 4 wrongly reject the explicit CFG for L1. Option 3 assumes one stack can preserve two independent comparisons after its information has already been used, which it cannot for L2.
