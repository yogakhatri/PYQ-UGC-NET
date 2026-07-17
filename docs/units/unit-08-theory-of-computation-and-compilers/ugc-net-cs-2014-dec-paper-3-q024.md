# Question 24

*UGC NET CS · 2014 Dec Paper 3 · Regular Language Models · Complement over the Full Alphabet*

Over the alphabet {a,b}, which option is a regular expression for the complement of L = {aⁿbᵐ | n ≥ 4, m ≤ 3}?

- **A.** (a+b)*ba(a+b)*
- **B.** a*bbbbb*
- **C.** (λ+a+aa+aaa)b* + (a+b)*ba(a+b)*
- **D.** None of the above

> [!TIP]
> **Correct answer: D. None of the above**

## Solution

L contains exactly the ordered strings aⁿbᵐ with at least four a's and at most three b's. Its complement over {a,b}* has three parts: strings with at most three initial a's, strings with at least four b's, and strings not in a*b* (equivalently, containing `ba`). One complete expression is `(λ+a+aa+aaa)b* + a*bbbbb* + (a+b)*ba(a+b)*`, where `bbbbb*` means four mandatory b's followed by any further b's. No listed expression contains all three parts, so D is correct.

## Key Points

- When complementing a patterned language inside Σ*, include both failed numeric bounds and strings that fail the required symbol order.

## Why the other options are incorrect

A includes only strings containing `ba`. B includes only the ordered strings with at least four b's. C combines the short-a and `ba` cases but omits strings such as `aaaabbbb`, which are outside L solely because m>3. Therefore A–C are each incomplete complements.
