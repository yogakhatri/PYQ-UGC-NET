# Question 33

*UGC NET CS · 2015 June Paper 3 · Algorithm Analysis · Logarithm and Iterated-Log Growth Rates*

Which of the following is asymptotically smaller ?

- **1.** lg(lg* n)
- **2.** lg*(lg n)
- **3.** lg(n!)
- **4.** lg*(n!)

> [!TIP]
> **Correct answer: 1. lg(lg* n)**

## Solution

Let `lg* n` be the number of repeated base-2 logarithms needed to reduce n to at most 1. Then `lg*(lg n) = lg* n − 1` up to threshold conventions, and `lg*(n!) = lg* n + O(1)`; both grow on the iterated-log scale. In contrast, `lg(lg* n)` applies an ordinary logarithm to that already tiny quantity, so it is asymptotically smaller. `lg(n!) = Θ(n lg n)` is vastly larger.

## Key Points

- Be careful about operator placement: `lg(lg* n)` is much smaller than `lg*(lg n)`.

## Why the other options are incorrect

Options 2 and 4 differ from `lg* n` only by an additive constant and therefore share its asymptotic order. Option 3 grows nearly linearly times a logarithm. Only option 1 grows like the logarithm of the iterated logarithm.
