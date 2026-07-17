# Question 63

*UGC NET CS · 2014 Dec Paper 3 · Context-Free Language · Pumping Lemma for Context-Free Languages*

For an infinite context-free language L, the pumping lemma says that there is an m>0 such that any w∈L with |w|≥m can be written w=uvxyz. Which option gives the required conditions?

- **A.** |vxy|≤m and uvⁱxyⁱz∈L for i=0,1,2 only
- **B.** |vxy|≤m, |vy|≥1, and uvⁱxyⁱz∈L for every i≥0
- **C.** |vxy|≥m, |vy|≤1, and uvⁱxyⁱz∈L for every i≥0
- **D.** |vxy|≥m, |vy|≥1, and uvⁱxyⁱz∈L for every i≥0

> [!TIP]
> **Correct answer: B. |vxy|≤m, |vy|≥1, and uvⁱxyⁱz∈L for every i≥0**

## Solution

For a sufficiently long string w in a context-free language, the CFL pumping lemma provides w=uvxyz such that the pumpable window is bounded, |vxy|≤m; at least one pumped part is nonempty, |vy|≥1; and uvⁱxyⁱz remains in L for every integer i≥0. Option B states all three conditions.

## Key Points

- CFL pumping: a short window contains two jointly nonempty pumped pieces, and both are pumped together for every i≥0.

## Why the other options are incorrect

A omits the requirement that v and y are not both empty and restricts i to only three values. C and D reverse the window bound to |vxy|≥m; C also permits both pumped parts to be empty. Those changes destroy the lemma's guarantee.
