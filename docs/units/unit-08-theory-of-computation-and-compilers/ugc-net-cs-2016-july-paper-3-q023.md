# Question 23

*UGC NET CS · 2016 July Paper 3 · Regular Language Models · Complement of a Restricted a-star-b-star Language*

The regular expression for the complement of the language L = {anbm|n ≥ 4, m ≤ 3} is :

- **1.** (λ + a + aa + aaa) b* + a* bbbb* + (a + b)* ba(a + b)*
- **2.** (λ + a + aa + aaa) b* + a* bbbbb* + (a + b)* ab(a + b)*
- **3.** (λ + a + aa + aaa) + a* bbbbb* + (a + b)* ab(a + b)*
- **4.** (λ + a + aa + aaa)b* + a* bbbbb* + (a + b)* ba(a + b)*

> [!TIP]
> **Correct answer: 4. (λ + a + aa + aaa)b* + a* bbbbb* + (a + b)* ba(a + b)***

## Solution

L contains exactly strings in a*b* with at least four a's and at most three b's. Its complement has three cases: at most three leading a's, represented by (λ+a+aa+aaa)b*; at least four b's, represented by a*bbbbb* (four fixed b's followed by b*); or a string not in a*b*, which must contain the substring ba and is represented by (a+b)*ba(a+b)*. Their union is option 4.

## Key Points

- Complement a constrained a*b* language by covering failed a-count, failed b-count, and failed symbol order (presence of `ba`).

## Why the other options are incorrect

Option 1 starts its long-b case one b too early. Options 2 and 3 use `ab` as the forbidden-order pattern, but every nonempty string in L may contain the a-to-b transition `ab`; it is `ba` that violates a*b*. Option 3 also omits trailing b* from the small-a case.
