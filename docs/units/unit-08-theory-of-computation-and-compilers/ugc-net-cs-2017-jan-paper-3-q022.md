# Question 22

*UGC NET CS · 2017 Jan Paper 3 · Context-Free Language · Height Bounds for K-ary Derivation Trees*

Let G = (V, T, S, P) be a context-free grammar in which every production has the form A → v with |v| = K > 1. Which bounds hold for the height h of a derivation tree for W ∈ L(G)?

- **1.** log_K|W| ≤ h ≤ log_K((|W|−1)/(K−1))
- **2.** log_K|W| ≤ h ≤ log_K(K|W|)
- **3.** log_K|W| ≤ h ≤ K log_K|W|
- **4.** log_K|W| ≤ h ≤ (|W|−1)/(K−1)

> [!TIP]
> **Correct answer: 4. log_K|W| ≤ h ≤ (|W|−1)/(K−1)**

## Solution

Every internal derivation-tree node has exactly K children. A tree of height h can have at most K^h leaves, so |W|≤K^h and h≥log_K|W|. In a full K-ary tree with I internal nodes and L leaves, L=(K−1)I+1. Here L=|W|, hence I=(|W|−1)/(K−1). A root-to-leaf path cannot contain more internal nodes than exist in the entire tree, so h≤(|W|−1)/(K−1). These are precisely the bounds in option 4.

## Key Points

- Maximum branching gives the logarithmic lower height bound; the full K-ary leaf/internal-node identity gives the linear upper bound.

## Why the other options are incorrect

Options 1–3 propose logarithmic upper bounds. A highly unbalanced full K-ary derivation tree can have a path whose length is linear in its number of internal nodes, so no such logarithmic upper bound holds in general.
