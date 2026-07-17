# Question 137

*UGC NET CS · 2020 Nov With Answers · Decidability · Context-Sensitive Language Decision Problems*

Statement I: The problem "Is L1∩L2=∅?" is undecidable for context-sensitive languages L1 and L2. Statement II: The membership problem "Is w∈L?" is decidable for a context-sensitive language L. Choose the correct evaluation.

- **1.** Both Statement I and Statement Il are true
- **2.** Both Statement I and Statement II are false
- **3.** Statement I is correct but Statement II is false
- **4.** Statement I is incorrect but Statement Il is true.

> [!TIP]
> **Correct answer: 1. Both Statement I and Statement Il are true**

## Solution

The emptiness problem for a context-sensitive language is undecidable. If an algorithm could decide whether L1∩L2 is empty for arbitrary context-sensitive L1 and L2, set L2=Σ*: it would then decide whether L1 itself is empty, which is impossible. Thus Statement I is true. A context-sensitive language is accepted by a linear-bounded automaton. For a fixed input, the machine has only finitely many bounded-tape configurations, so its reachability/acceptance question can be decided; membership is decidable (indeed PSPACE-complete in general). Statement II is also true. Hence option 1.

## Key Points

- For context-sensitive languages, membership is decidable but emptiness—and therefore general intersection-emptiness—is undecidable.

## Why the other options are incorrect

Options 2–4 deny one of the two standard decision results. Closure of context-sensitive languages under intersection does not make intersection emptiness decidable; closure and decidability of an associated property are different questions.

## References

- [Uniform vs. Nonuniform Membership for Mildly Context-Sensitive Languages: A Brief Survey](https://www.mdpi.com/1999-4893/9/2/32)
- [Formal languages and automata — Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Formal_languages_and_automata)
