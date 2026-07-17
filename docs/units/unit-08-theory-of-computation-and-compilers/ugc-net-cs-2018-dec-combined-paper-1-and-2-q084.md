# Question 84

*UGC NET CS · 2018 Dec Paper 1 And 2 · Regular Language Models · Length-Constrained Quotients of Regular Languages*

Let L be regular. Define L₁={x | for some y with |y|=2^|x|, xy∈L} and L₂={x | for some y with |x|=|y|, xy∈L}. Which statement is correct?

- **1.** Only L1 is regular
- **2.** Only L2 is regular
- **3.** Both L1 and L2 are regular
- **4.** Neither L1 nor L2 is regular

> [!TIP]
> **Correct answer: 3. Both L1 and L2 are regular**

## Solution

Let a DFA for L have finite state set Q. After reading x, only the reached state q and the length |x| matter. From q, whether some continuation of exactly ℓ symbols can reach a final state is determined by the finite transition relation raised to length ℓ. Powers of a relation on finite Q are ultimately periodic. For L₂ use ℓ=|x|; for L₁ use ℓ=2^|x|. Both resulting sequences are ultimately periodic in |x|, so a finite automaton can store q together with a finite prefix/period class of |x|. Consequently both L₁ and L₂ are regular, option 3.

## Key Points

- Exact-length reachability in a finite transition graph is ultimately periodic, so length-constrained right quotients of this form remain regular.

## Why the other options are incorrect

Options 1, 2, and 4 assume that comparing the lengths of x and an existential continuation automatically creates a nonregular equality language. It does not: y is not a second visible input block that must be compared; only the existence of a path of a prescribed length in a finite DFA is tested.
