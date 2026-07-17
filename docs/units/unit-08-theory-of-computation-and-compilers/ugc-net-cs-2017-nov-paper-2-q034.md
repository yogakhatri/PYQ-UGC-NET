# Question 34

*UGC NET CS · 2017 Nov Paper 2 · Context-Free Grammars · Grammar Ambiguity and String Derivation*

Which statements are true? (a) The grammar S → SS | a is ambiguous. (b) The grammar S → 0S1 | 01S | ε is ambiguous. (c) The grammar S → T | U, T → xSy | xy | ε, U → yT generates the string yxxyy. In every grammar, S is the start symbol.

- **1.** Only (a) and (b) are TRUE.
- **2.** Only (a) and (c) are TRUE.
- **3.** Only (b) and (c) are TRUE.
- **4.** All of (a), (b) and (c) are TRUE.

> [!TIP]
> **Correct answer: 4. All of (a), (b) and (c) are TRUE.**

## Solution

All three statements are true. For (a), `aaa` has different parse structures, such as `(aa)a` and `a(aa)`, under S→SS|a, so the grammar is ambiguous. For (b), `01` can be derived either by S→0S1→01 or by S→01S→01, again giving two parse trees. For (c), derive S⇒U⇒yT⇒yxSy⇒yxT y⇒yxxyy using S⇒T⇒xy for the inner S. Therefore option 4 is correct.

## Key Points

- To prove ambiguity, exhibit the same terminal string with two distinct parse trees/derivations; to prove membership, give one complete derivation.

## Why the other options are incorrect

Options 1–3 each reject one statement despite an explicit witness: `aaa` proves (a), the two derivations of `01` prove (b), and the shown derivation of `yxxyy` proves (c). One string with two parse trees is sufficient to establish ambiguity.
