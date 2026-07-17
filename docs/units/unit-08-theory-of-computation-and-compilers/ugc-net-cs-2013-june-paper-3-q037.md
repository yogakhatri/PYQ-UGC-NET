# Question 37

*UGC NET CS · 2013 June Paper 3 · Pushdown Automata · Deterministic PDA Conditions*

A pushdown automation M = (Q, Σ, Γ, δ, q 0, z, F) is set to be deterministic subject to which of the following condition(s), for every q ∈ Q, a ∈ Σ ∪ {λ} and b ∈ Γ (s1) δ(q, a, b) contains at most one element (s2) if δ(q, λ, b) is not empty then δ(q, c, b) must be empty for every c ∈ Σ

- **A.** only s1
- **B.** only s2
- **C.** both s1 and s2
- **D.** neither s1 nor s2

> [!TIP]
> **Correct answer: C. both s1 and s2**

## Solution

A deterministic PDA must have at most one possible move for a fixed state, input choice and stack top, which is statement s1. It must also avoid a choice between consuming input and taking an ε-move: if δ(q,ε,b) exists, every δ(q,c,b) for c in the input alphabet must be empty. That is statement s2. Both restrictions are needed to make the next move unique.

## Key Points

- DPDA determinism requires a unique transition and no ε/input transition conflict for the same state and stack top.

## Why the other options are incorrect

Using only s1 can still leave an ε-move and an input-consuming move simultaneously enabled. Using only s2 does not prevent multiple outcomes for the same transition argument. Therefore neither single statement alone is sufficient, and 'neither' is false.
