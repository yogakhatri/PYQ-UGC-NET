# Question 102

*UGC NET CS · 2020 Nov With Answers · Complexity Analysis · Theta Bounds Across Best and Worst Cases*

The running time of an algorithm is Θ(g(n)) if and only if which statement holds? (A) Its worst-case running time is O(g(n)) and its best-case running time is Ω(g(n)). (B) Its worst-case running time is Ω(g(n)) and its best-case running time is O(g(n)). (C) O(g(n)) = Ω(g(n)). (D) O(g(n)) ∩ ω(g(n)) is non-empty.

- **1.** (A) only
- **2.** (B) only
- **3.** (C) only
- **4.** (D) only

> [!TIP]
> **Correct answer: 1. (A) only**

## Solution

Let Tbest(n) and Tworst(n) be the minimum and maximum running times over inputs of size n. Every actual running time T(n) satisfies Tbest(n)≤T(n)≤Tworst(n). If Tworst(n)≤c₂g(n) and Tbest(n)≥c₁g(n) for sufficiently large n, then c₁g(n)≤T(n)≤c₂g(n) for every input, exactly the definition of T(n)=Θ(g(n)). Conversely, a uniform Θ(g(n)) bound supplies those worst-case O and best-case Ω bounds. Therefore A only, option 1.

## Key Points

- Worst-case O gives the upper side and best-case Ω gives the lower side; together they squeeze every input into Θ.

## Why the other options are incorrect

B reverses the useful inequalities and need not squeeze every input between constant multiples of g. O(g) and Ω(g) are not equal sets, so C is false. No function can grow strictly faster than g (ω(g)) while also being asymptotically upper-bounded by a constant multiple of g (O(g)); hence the intersection in D is empty.

## References

- [Introduction to Algorithms — asymptotic growth exercises](https://mraabo.dk/ox-hugo/clrs.pdf)
