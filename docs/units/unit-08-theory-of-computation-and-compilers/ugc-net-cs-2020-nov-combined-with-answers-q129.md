# Question 129

*UGC NET CS · 2020 Nov With Answers · Regular Language Models · Language Inclusion for Regular Expressions*

Consider the regular expressions r = a(b+a)*, s = a(a+b)+, and t = aa*b. Which relation holds among their languages?

- **1.** L(r) ⊆ L(s) ⊆ L(t)
- **2.** L(r) ⊇ L(s) ⊇ L(t)
- **3.** L(r) ⊇ L(t) ⊇ L(s)
- **4.** L(s) ⊇ L(t) ⊇ L(r)

> [!TIP]
> **Correct answer: 2. L(r) ⊇ L(s) ⊇ L(t)**

## Solution

The expression r=a(a+b)* describes every nonempty binary string beginning with a, including the one-symbol string a. The expression s=a(a+b)+ describes the same kind of string but requires at least one further symbol, so L(s) is a proper subset of L(r). Finally, t=aa*b describes strings a^k b with k≥1; every such string begins with a and has length at least two, so L(t) is a proper subset of L(s). Therefore L(r) ⊇ L(s) ⊇ L(t), option 2.

## Key Points

- Translate each regular expression into a plain-language shape, then use short witness strings to test each containment.

## Why the other options are incorrect

The reverse containments fail immediately: a belongs to L(r) but not L(s), while ab or aa belongs to L(s) but not every such string belongs to L(t). Options 3 and 4 incorrectly place the restricted a^k b language above the general beginning-with-a language.
