# Question 22

*UGC NET CS · 2016 July Paper 3 · Regular Language Models · Closure under Symmetric Difference and NOR*

The symmetric difference of two sets S1 and S2 is defined as S1 s S2 = {x|x ∈ S1 or x ∈ S2, but x is not in both S1 and S2} The nor of two languages is defined as nor (L1, L2) = {w|w |∈L1 and w |∈ L2}. Which of the following is correct ?

- **1.** The family of regular languages is closed under symmetric difference but not closed under nor.
- **2.** The family of regular languages is closed under nor but not closed under symmetric difference.
- **3.** The family of regular languages are closed under both symmetric difference and nor.
- **4.** The family of regular languages are not closed under both symmetric difference and nor. J-87-16 5 Paper-III

> [!TIP]
> **Correct answer: 3. The family of regular languages are closed under both symmetric difference and nor.**

## Solution

For languages L₁ and L₂, symmetric difference is (L₁∪L₂)−(L₁∩L₂), constructed from union, intersection, and complement. NOR is the complement of their union: Σ*−(L₁∪L₂). Regular languages are closed under union, intersection, complement, and difference, so both results are regular. Option 3 is correct.

## Key Points

- Regular languages are closed under every Boolean combination, including XOR (symmetric difference) and NOR.

## Why the other options are incorrect

Options 1, 2, and 4 each deny a closure property that follows from the Boolean closure of regular languages. A DFA construction can track the pair of component states and choose accepting pairs according to XOR or NOR.
