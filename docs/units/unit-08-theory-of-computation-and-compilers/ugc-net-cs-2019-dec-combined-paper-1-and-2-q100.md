# Question 100

*UGC NET CS · 2019 Dec Paper 1 And 2 · Context-Free Language · Language-Family Inclusion Hierarchy*

Let L1 be the context-free languages, L2 the context-sensitive languages, L3 the recursively enumerable languages, and L4 the recursive languages. Which inclusion chain is correct?

- **1.** L1 ⊆ L2 ⊆ L3 ⊆ L4
- **2.** L2 ⊆ L1 ⊆ L3 ⊆ L4
- **3.** L1 ⊆ L2 ⊆ L4 ⊆ L3
- **4.** L2 ⊆ L1 ⊆ L4 ⊆ L3

> [!TIP]
> **Correct answer: 3. L1 ⊆ L2 ⊆ L4 ⊆ L3**

## Solution

Every context-free language is context-sensitive, so L1⊆L2. A linear-bounded automaton always halts because it has only finitely many configurations on a fixed input; hence every context-sensitive language is recursive, giving L2⊆L4. Every decider is also a recognizer, so every recursive language is recursively enumerable: L4⊆L3. The correct chain is L1⊆L2⊆L4⊆L3, option 3.

## Key Points

- Remember the relevant Chomsky/decidability chain: CFL ⊆ CSL ⊆ recursive ⊆ recursively enumerable.

## Why the other options are incorrect

Options 1 and 2 place recursively enumerable languages inside recursive languages, reversing the final inclusion. Options 2 and 4 also place context-sensitive languages inside context-free languages, reversing the first two families.
