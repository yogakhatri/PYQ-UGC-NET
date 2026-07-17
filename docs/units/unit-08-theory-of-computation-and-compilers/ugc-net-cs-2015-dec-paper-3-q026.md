# Question 26

*UGC NET CS · 2015 Dec Paper 3 · Context-Free Language · Grammar Languages and Regular Expressions*

The grammar S→XYX, X→aX | bX | λ, Y→bbb generates which regular expression?

- **1.** (a+b)*bbb
- **2.** abbb(a+b)*
- **3.** (a+b)*(bbb)(a+b)*
- **4.** (a+b)(bbb)(a+b)*

> [!TIP]
> **Correct answer: 3. (a+b)*(bbb)(a+b)***

## Solution

From X→aX | bX | λ, X generates every string over {a,b}, including the empty string; hence L(X)=(a+b)*. Y generates exactly `bbb`. Since S→XYX, concatenate these languages to obtain (a+b)*·bbb·(a+b)*, which is option 3.

## Key Points

- Find the language of each nonterminal, then substitute into the start production and concatenate.

## Why the other options are incorrect

Option 1 omits the arbitrary suffix, option 2 wrongly requires a leading `a`, and option 4 requires at least one symbol before `bbb`. Both X occurrences may independently generate λ.
