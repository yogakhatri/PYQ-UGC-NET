# Question 23

*UGC NET CS · 2017 Jan Paper 3 · Context-Free Language · Closure Arguments for Context-Free Languages*

Given the following two languages : L1 = {an bn | n ≥ 0, n ≠ 100} L2 = {w ∈ {a, b, c}*| na(w) = nb(w) = nc(w)} Which of the following options is correct ?

- **1.** Both L1 and L2 are not context free language
- **2.** Both L1 and L2 are context free language.
- **3.** L1 is context free language, L2 is not context free language.
- **4.** L1 is not context free language, L2 is context free language.

> [!TIP]
> **Correct answer: 3. L1 is context free language, L2 is not context free language.**

## Solution

{a^n b^n | n≥0} is context-free. Removing the single string a^100b^100 preserves context-freeness—for example, intersect with the regular language that excludes exactly that string—so L1 is context-free. If L2 were context-free, then intersecting it with the regular language a*b*c* would also be context-free. That intersection is {a^n b^n c^n | n≥0}, a standard non-context-free language, giving a contradiction. Thus L2 is not context-free and option 3 is correct.

## Key Points

- Use closure with regular languages: CFL∩regular is CFL, which can both remove a finite exception and expose a known non-CFL contradiction.

## Why the other options are incorrect

Options 1 and 4 misclassify L1; deleting one exceptional string does not destroy its context-free structure. Option 2 misclassifies L2, whose three equal symbol counts can expose a^n b^n c^n through regular intersection.
