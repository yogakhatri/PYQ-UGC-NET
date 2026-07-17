# Question 63

*UGC NET CS · 2015 June Paper 3 · Context-Free Grammars · Demonstrating Grammar Ambiguity*

Given G1: S → AB | aaB; A → aA | ε; B → bB | ε. Given G2: S → A | B; A → aAb | ab; B → abB | ε. Which statement about ambiguity is correct?

- **1.** G1 is ambiguous and G2 is unambiguous grammars
- **2.** G1 is unambiguous and G2 is ambiguous grammars
- **3.** both G1 and G2 are ambiguous grammars
- **4.** both G1 and G2 are unambiguous grammars

> [!TIP]
> **Correct answer: 3. both G1 and G2 are ambiguous grammars**

## Solution

G1 is ambiguous because, for example, `aab` has two derivations: `S⇒AB` with `A⇒aa` and `B⇒b`, or `S⇒aaB` with `B⇒b`. G2 is also ambiguous: `ab` follows `S⇒A⇒ab`, and independently `S⇒B⇒abB⇒ab` with the final B⇒ε. Since each grammar has a string with two distinct parse choices, both are ambiguous.

## Key Points

- To prove a CFG ambiguous, exhibit one terminal string with two different parse trees or leftmost derivations.

## Why the other options are incorrect

Options 1, 2, and 4 claim at least one grammar is unambiguous, contradicted by the explicit duplicate derivations above. One counterexample string per grammar is enough to prove ambiguity.
