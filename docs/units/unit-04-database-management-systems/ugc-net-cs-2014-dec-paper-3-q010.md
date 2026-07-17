# Question 10

*UGC NET CS · 2014 Dec Paper 3 · Functional Dependencies · Attribute Closure*

Let R = ABCDE is a relational scheme with function al dependency set F = {A → B, B → C, AC → D}. The attribute closures of A and E are

- **A.** ABCD, φ
- **B.** ABCD, E
- **C.** Φ, φ
- **D.** ABC, E

> [!TIP]
> **Correct answer: B. ABCD, E**

## Solution

Start A⁺={A}. Apply A→B to add B, then B→C to add C. With A and C present, AC→D adds D, so A⁺={A,B,C,D}; no dependency produces E. Starting with E, no dependency has a left side contained in {E}, so E⁺={E}. The pair is ABCD, E.

## Key Points

- An attribute closure always starts with the given attributes and repeatedly applies every enabled FD.

## Why the other options are incorrect

A incorrectly treats an attribute's closure as empty when no dependency fires; it always contains the attribute itself. C makes both closures empty. D stops A's closure before applying AC→D.
