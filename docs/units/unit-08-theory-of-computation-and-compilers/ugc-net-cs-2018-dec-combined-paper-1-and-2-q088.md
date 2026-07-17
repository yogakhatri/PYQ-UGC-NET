# Question 88

*UGC NET CS · 2018 Dec Paper 1 And 2 · Unsolvable Problems and Computational Complexity · Decidability for Recursive Languages*

Which problem is decidable for a recursive language L?

- **1.** Is L empty?
- **2.** Is w in L, where w is a string?
- **3.** Is L=Sigma*?
- **4.** Is L=R, where R is a given regular set?

> [!TIP]
> **Correct answer: 2. Is w in L, where w is a string?**

## Solution

A recursive language is, by definition, decided by a Turing machine that halts on every input and answers membership correctly. Therefore, for any specified string w, run that decider: it halts and determines whether w∈L. Membership is decidable, so option 2 is correct.

## Key Points

- ‘Recursive language’ guarantees decidable membership, not decidability of arbitrary whole-language properties.

## Why the other options are incorrect

Given an arbitrary decider as the description of L, global properties such as emptiness, universality L=Σ*, or equality with a fixed regular language are not decidable in general; each quantifies over all strings and is a nontrivial semantic language property. Recursive does not mean every property of the language becomes decidable.
