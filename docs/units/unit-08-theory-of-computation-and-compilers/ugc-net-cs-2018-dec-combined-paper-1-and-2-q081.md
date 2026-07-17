# Question 81

*UGC NET CS · 2018 Dec Paper 1 And 2 · Regular Language Models · Language Inclusion from Regular Expressions*

Let r=a(a+b)*, s=aa*b, and t=a*b. Consider: (i) L(s)⊆L(r) and L(s)⊆L(t); (ii) L(r)⊆L(s) and L(s)⊆L(t). Which statements are correct?

- **1.** Only (i) is correct.
- **2.** Only (ii) is correct.
- **3.** Both (i) and (ii) are correct.
- **4.** Neither (i) nor (ii) is correct.

> [!TIP]
> **Correct answer: 1. Only (i) is correct.**

## Solution

The languages are L(r)={all strings over {a,b} that start with a}, L(s)={a^k b | k≥1}, and L(t)={a^k b | k≥0}. Every string in L(s) starts with a, so L(s)⊆L(r); it also has the form allowed by t, so L(s)⊆L(t). Thus statement (i) is true. However L(r) is not contained in L(s): for example, `aa` belongs to L(r) but not to L(s), which must end in b. Therefore statement (ii) is false and option 1 is correct.

## Key Points

- Translate each regular expression into a plain structural description, then disprove a proposed inclusion with one counterexample.

## Why the other options are incorrect

Options 2 and 3 accept the false inclusion L(r)⊆L(s). Option 4 rejects statement (i), although both of its inclusions follow directly from the three expression forms.
