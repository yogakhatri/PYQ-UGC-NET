# Question 79

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Context-Free Language · Chomsky and Greibach Normal Forms*

B 0:87029 In Pumping Lemma for context free languages, to say a language is satisfying pumping lemma, what is the minimum length of 'v' together, if you consider the string as 'unwxy?

- **1.** 0
- **2.** 1
- **3.** 2
- **4.** n

> [!TIP]
> **Correct answer: 2. 1**

## Solution

For the CFL pumping decomposition uvwxy, the two pumped pieces cannot both be empty: |vx|≥1. Therefore their minimum combined length is 1.

## Key Points

- CFL pumping lemma requires |vx|≥1 and |vwx|≤p.

## Why the other options are incorrect

Zero is forbidden; neither 2 nor pumping length n is a required minimum.
