# Question 69

*UGC NET CS · 2017 Jan Paper 3 · Optimization · Degeneracy in Transportation Problems*

At which of the following stage(s), the degeneracy do not occur in transportation problem ? (m, n represents number of sources and destinations respectively) (a) While the values of dual variables ui and vj cannot be computed. (b) While obtaining an initial solution, we may have less than m + n – 1 allocations. (c) At any stage while moving towards optimal solution, when two or more occupied cells with the same minimum allocation become unoccupied simultaneously. (d) At a stage when the no. of +ve allocation is exactly m + n – 1.

- **1.** (a), (b) and (c)
- **2.** (a), (c) and (d)
- **3.** (a) and (d)
- **4.** (a), (b), (c) and (d)

> [!TIP]
> **Correct answer: 3. (a) and (d)**

## Solution

Degeneracy is defined by having fewer than m+n−1 independent positive allocations. It can arise initially as in (b), or during a pivot when tied minimum allocations cause multiple occupied cells to leave simultaneously as in (c). Statement (a)—inability to compute all dual potentials—is a consequence or diagnostic difficulty after degeneracy, not a stage at which degeneracy arises. In (d), exactly m+n−1 positive independent allocations means the solution is nondegenerate. Thus degeneracy does not occur in (a) and (d), giving option 3.

## Key Points

- Transportation degeneracy occurs when the basic positive allocation count drops below m+n−1, initially or after a tied pivot.

## Why the other options are incorrect

Every other option includes (b) or (c), the two recognized occurrence stages. The question distinguishes causes/stages from consequences and from the defining nondegenerate allocation count.
