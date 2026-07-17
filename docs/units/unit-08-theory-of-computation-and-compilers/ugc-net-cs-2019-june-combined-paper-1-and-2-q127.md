# Question 127

*UGC NET CS · 2019 June Paper 1 And 2 · Context-Free Language · CFL Finiteness Decision*

How can a decision algorithm be constructed for deciding whether a context-free language L is finite? (a) By constructing a redundant CFG G in CNF generating L. (b) By constructing a non-redundant CFG G in CNF generating L. (c) By constructing a non-redundant CFG G in CNF generating L-{epsilon}. Which is correct?

- **1.** (a) only
- **2.** (b) only
- **3.** (c) only
- **4.** None of (a), (b) and (c)

> [!TIP]
> **Correct answer: 3. (c) only**

## Solution

First remove epsilon and construct a non-redundant grammar in Chomsky normal form for L-{epsilon}. Non-redundant means every variable is both reachable and productive, so irrelevant cycles cannot mislead the test. In such a grammar, L is infinite exactly when some useful variable can derive a sentential form containing itself with additional generated material; otherwise derivation-tree height is bounded and only finitely many strings can be generated. Thus construction (c) supports the decision procedure.

## Key Points

- For CFL finiteness, remove epsilon, eliminate useless symbols, convert to CNF and test for a productive reachable recursive variable.

## Why the other options are incorrect

A redundant grammar can contain useless recursive variables even when its language is finite, so (a) is unsuitable. Statement (b) does not explicitly handle the epsilon exception in the strict CNF construction used by this procedure. Therefore the intended precise construction is (c).
