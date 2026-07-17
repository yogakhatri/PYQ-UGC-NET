# Question 129

*UGC NET CS · 2019 June Paper 1 And 2 · Theory of Computation · Decidable Problems*

Which of the following problems are decidable on a Turing machine M? (a) G is a CFG with L(G)=empty set. (b) There exist two TMs M1 and M2 such that L(M) is a subset of {L(M1) union L(M2)}, the language of all TMs. (c) M is a TM that accepts string w using at most 2^|w| tape cells.

- **1.** (a) and (b) only
- **2.** (a) only
- **3.** (a), (b) and (c)
- **4.** (c) only

> [!TIP]
> **Correct answer: 3. (a), (b) and (c)**

## Solution

All three predicates are decidable. (a) CFG emptiness is decided by marking variables that can derive terminal strings and checking whether the start variable is marked. (b), as printed, is always satisfiable: for any M choose M1=M (and any M2), so L(M) is contained in L(M1) union L(M2); an always-yes predicate is decidable. (c) imposes a finite tape bound 2^|w|. For fixed M and w this yields finitely many configurations, so simulate while recording configurations; acceptance is found, or a repeated configuration proves no bounded accepting computation will appear.

## Key Points

- A finite resource bound turns reachability among TM configurations into a finite-state decision problem.

## Why the other options are incorrect

Options 1 and 2 omit the decidable bounded-space problem (c). Option 4 omits CFG emptiness and the trivially satisfiable existential condition (b).

## Additional Information

The wording of (b) in the source paper is awkward; the answer follows its literal existential statement.
