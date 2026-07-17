# Question 117

*UGC NET CS · 2019 June Paper 1 And 2 · Complexity Theory · P, NP and co-NP*

Let CO-NP be the set of languages L such that the complement of L is in NP. Consider S1: P is a subset of CO-NP. S2: If NP is not equal to CO-NP, then P is not equal to NP. Which statements are correct?

- **1.** Only S1
- **2.** Only S2
- **3.** Both S1 and S2
- **4.** Neither S1 nor S2

> [!TIP]
> **Correct answer: 3. Both S1 and S2**

## Solution

S1 is true. P is closed under complement, and P is contained in NP; therefore every language in P has its complement in NP and hence belongs to co-NP. S2 is also true. If P=NP, then closure of P under complement would give NP=co-NP. Taking the contrapositive, NP != co-NP implies P != NP. Thus both statements hold.

## Key Points

- Use P's closure under complement and the contrapositive: P=NP would force NP=co-NP.

## Why the other options are incorrect

Options 1 and 2 each discard one valid statement. Option 4 misses both the inclusion P subseteq co-NP and the contrapositive implication used in S2.
