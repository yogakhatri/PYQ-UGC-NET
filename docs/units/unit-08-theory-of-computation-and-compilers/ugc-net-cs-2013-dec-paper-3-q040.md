# Question 40

*UGC NET CS · 2013 Dec Paper 3 · Context-Free Languages · Pumping Lemma*

Pumping lemma for context-free languages states : Let L be an infinite context free language. Then there exists some positive integer m such that any w ∈ L with |w| ≥ m can be decomposed as w = uv xy Z with |v xy| _________ and |vy| _________ such that uv .z xy .z Z ∈ L for all .z = 0, 1, 2, ....... .

- **A.** ≤ m, ≤ 1
- **B.** ≤ m, ≥ 1
- **C.** ≥ m, ≤ 1
- **D.** ≥ m, ≥ 1

> [!TIP]
> **Correct answer: B. ≤ m, ≥ 1**

## Solution

The context-free pumping lemma says that every sufficiently long w in L can be written w=uvxyz so that |vxy|≤m, |vy|≥1, and uv^i xy^i z belongs to L for every i≥0. The first inequality keeps both pumped pieces within a bounded window; the second ensures that at least one of v or y is nonempty, so pumping actually changes the string.

## Key Points

- CFL pumping lemma memory aid: the middle window is at most m, but the total pumped material is at least 1.

## Why the other options are incorrect

Any option with |vxy|≥m reverses the bounded-window condition. Any option with |vy|≤1 permits both pumped portions to be empty and does not state the required non-emptiness. Therefore only B contains both standard inequalities.
