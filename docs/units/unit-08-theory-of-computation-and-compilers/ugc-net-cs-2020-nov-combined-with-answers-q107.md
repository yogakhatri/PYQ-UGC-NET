# Question 107

*UGC NET CS · 2020 Nov With Answers · Context-Free Grammars · Ambiguous Grammar Counterexamples*

Which grammars are ambiguous? (A) S→SS | aSb | bSa | ε. (B) S→aSbS | bSaS | ε. (C) S→aAB, A→bBb, B→A | ε.

- **1.** (A) and (C) only
- **2.** (B) only
- **3.** (B) and (C) only
- **4.** (A) and (B) only

> [!TIP]
> **Correct answer: All three grammars (A), (B), and (C) are ambiguous; the scanned question contains no option expressing this correct combination.**

## Solution

Grammar A is ambiguous immediately: ε has the direct derivation S⇒ε and also S⇒SS⇒εε. Grammar B is ambiguous for abab. One parse uses S⇒aεb(aεbε), while another uses S⇒a(bεaε)bε; these place the recursive substring in different S children. Grammar C is ambiguous for abbbb: either the first A produces bbbb and the final B produces ε, or the first A produces bb and the final B⇒A produces bb. Each case gives a distinct parse tree. Therefore A, B, and C are all ambiguous.

## Key Points

- One counterexample string with two parse trees proves ambiguity; ε, abab, and abbbb witness A, B, and C respectively.

## Why the other options are incorrect

Options 1, 3, and 4 each omit one grammar that has an explicit ambiguity witness; option 2 omits two. Since the source lists only pairwise combinations or B alone, none of its four option texts is mathematically complete.
