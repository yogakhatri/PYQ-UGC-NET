# Question 80

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Regular Language Models · Regular Languages*

In Pumping Lemma for regular languages, to say a language is satisfying pumping lemma, what is the minimum length of 'y' if you consider the string as 'xyz'.

- **1.** n
- **2.** 2
- **3.** 1
- **4.** 0

> [!TIP]
> **Correct answer: 3. 1**

## Solution

The pumping lemma decomposes a sufficiently long string w as xyz with |xy|≤p, |y|≥1, and xy^iz in the language for every i≥0. The condition |y|≥1 prevents the pumped section from being empty. Therefore the minimum possible length of y is 1.

## Key Points

- In the regular-language pumping lemma, the pumpable part must be nonempty: |y|≥1.

## Why the other options are incorrect

Zero is explicitly forbidden. The pumping length n (or p) constrains the original string and the prefix xy, not the minimum length of y; there is no requirement that y have length 2.
