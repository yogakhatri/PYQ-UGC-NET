# Question 20

*UGC NET CS · 2017 Jan Paper 3 · Regular Language Models · Kleene Star, Union, and Concatenation*

Consider the languages L1 = ∅ and L2 = {1}. Which option represents L1* ∪ L2*L1*?

- **1.** {∈}
- **2.** {∈, 1}
- **3.** φ
- **4.** 1*

> [!TIP]
> **Correct answer: 4. 1***

## Solution

The Kleene star always contains ε, even for the empty language, so L1*=∅*={ε}. Since L2={1}, L2*={1}*=1*. Concatenating with {ε} changes nothing: L2*L1*=1*{ε}=1*. Finally, {ε}∪1*=1* because ε is already in 1*. Therefore option 4 is correct.

## Key Points

- ∅*={ε}; ε is the identity for language concatenation; and {1}*=1*.

## Why the other options are incorrect

Option 1 keeps only ε and loses the positive-length strings. Option 2 keeps only ε and 1, omitting 11, 111, and so on. Option 3 forgets that the star of even the empty language contains ε.
