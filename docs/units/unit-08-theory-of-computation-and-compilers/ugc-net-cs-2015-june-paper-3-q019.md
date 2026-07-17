# Question 19

*UGC NET CS · 2015 June Paper 3 · Finite Automata · Minimal DFA for a Unary Exception Language*

A minimal deterministic finite automaton for L = {0^n | n ≥ 0 and n ≠ 4} will have:

- **1.** 1 final state among 5 states
- **2.** 4 final states among 5 states
- **3.** 1 final state among 6 states
- **4.** 5 final states among 6 states

> [!TIP]
> **Correct answer: 4. 5 final states among 6 states**

## Solution

On the unary alphabet, the DFA must distinguish lengths 0, 1, 2, 3, 4, and at least 5. After reaching length 5, every further zero remains accepted, so all lengths ≥5 share one state. This gives six states. Every state is accepting except the state for exactly four zeros, so five of the six states are final.

## Key Points

- To reject exactly one unary length k, track 0 through k and combine all lengths above k into one accepting sink: k+2 states.

## Why the other options are incorrect

Five states cannot distinguish all six necessary residual cases: each prefix length through 4 behaves differently, and lengths ≥5 need an accepting sink. Options 1 and 3 also reverse the acceptance pattern by proposing only one final state.
