# Question 38

*UGC NET CS · 2013 June Paper 3 · Parsing and Syntax Analysis · Cubic-Time CFG Membership*

For every context-free grammar G, there exists an algorithm that parses any w ∈ L(G) in a number of steps proportional to

- **A.** ln |w|
- **B.** |w|
- **C.** |w|²
- **D.** |w|³

> [!TIP]
> **Correct answer: D. |w|³**

## Solution

A general context-free grammar can be converted to an equivalent Chomsky-normal-form grammar and parsed by the CYK dynamic-programming algorithm. For an input of length n=|w|, CYK considers O(n²) substrings and up to O(n) split positions per substring, giving O(n³) time for a fixed grammar. Hence the stated general parsing bound is proportional to |w|³.

## Key Points

- General CFG membership via CYK uses substring × substring × split-point dynamic programming: O(n³).

## Why the other options are incorrect

Logarithmic and linear bounds are not available for arbitrary context-free grammars. A quadratic table has O(n²) cells, but filling each cell may examine O(n) splits, producing the cubic rather than quadratic bound.
