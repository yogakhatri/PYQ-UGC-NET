# Question 37

*UGC NET CS · 2015 June Paper 2 · Process Management · Bernstein Conditions for Concurrent Execution*

Let Pi and Pj be two processes, R be the set of variables read from memory, and W be the set of variables written to memory. For the concurrent execution of two processes Pi and Pj which of the following conditions is not true ?

- **1.** R(P_i) ∩ W(P_j) = ∅
- **2.** W(P_i) ∩ R(P_j) = ∅
- **3.** R(P_i) ∩ R(P_j) = ∅
- **4.** W(P_i) ∩ W(P_j) = ∅

> [!TIP]
> **Correct answer: 3. R(P_i) ∩ R(P_j) = ∅**

## Solution

Bernstein's independence conditions forbid a value written by one process from being read or written by the other: `R(P_i) ∩ W(P_j) = ∅`, `W(P_i) ∩ R(P_j) = ∅`, and `W(P_i) ∩ W(P_j) = ∅`. Two processes may safely read the same variable because neither read changes it. Therefore requiring `R(P_i) ∩ R(P_j) = ∅` is not a necessary condition.

## Key Points

- Shared reads are safe; every cross-process overlap involving a write creates a possible dependence.

## Why the other options are incorrect

Options 1 and 2 prevent read-after-write and write-after-read dependence across the two processes. Option 4 prevents simultaneous writes to shared results. Those are genuine independence requirements; only read–read overlap is harmless.
