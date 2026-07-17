# Question 22

*UGC NET CS · 2014 Dec Paper 3 · Pushdown Automata · Equal-Count Language and Empty String*

The pushdown automaton M = ({q₀,q₁,q₂}, {a,b}, {0,1}, δ, q₀, 0, {q₀}) has δ(q₀,a,0)={(q₁,10)}, δ(q₁,a,1)={(q₁,11)}, δ(q₁,b,1)={(q₂,λ)}, δ(q₂,b,1)={(q₂,λ)}, and δ(q₂,λ,0)={(q₀,λ)}. Which language does it accept?

- **A.** L = {aⁿbᵐ | n,m ≥ 0}
- **B.** L = {aⁿbⁿ | n ≥ 0}
- **C.** L = {aⁿbᵐ | n,m > 0}
- **D.** L = {aⁿbⁿ | n > 0}

> [!TIP]
> **Correct answer: B. L = {aⁿbⁿ | n ≥ 0}**

## Solution

The first a replaces bottom marker 0 by 10, placing one 1 above it. Every later a replaces top 1 by 11, adding one more 1. The first b moves to q₂ and pops one 1; each later b pops another. The ε-transition back to final state q₀ is possible only after all 1s are gone, so the numbers of a's and b's must be equal and all a's must precede the b's. Also, q₀ is the initial and a final state, so ε is accepted. Hence L={aⁿbⁿ | n≥0}.

## Key Points

- One stack marker is pushed per a and popped per b; an accepting initial state decides whether the empty string is included.

## Why the other options are incorrect

A and C allow unequal counts, which leave unmatched stack symbols or attempt to pop too many. D has the equal-count structure but excludes n=0, overlooking that the automaton begins in the accepting state q₀ and therefore accepts ε.
