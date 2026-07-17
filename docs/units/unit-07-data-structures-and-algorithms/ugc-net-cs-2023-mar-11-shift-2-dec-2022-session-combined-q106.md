# Question 106

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Performance Analysis and Recurrences · Time and Space Complexity*

Circuit satisfiability problem: Given a Boolean combinatorial circuit composed of AND, OR and NOT gates, is it satisfiable? A one output Boolean combinatorial circuit is satisfiable means for the given inputs the output will be 1. A. The circuit satisfiability problem belongs to class NP B. The circuit satisfiability problem is at least as hard as any language in NP C. The circuit satistiability is NP-Complete D. The size of the circuit is O(K2+1) E. If P#NP, this situation would contradict the NP-Completeness of the problem. Choose the correct answer from the options given below:

- **1.** A, C, D Only
- **2.** B, D, E Only
- **3.** A. B. C Only
- **4.** B, C, D Only

> [!TIP]
> **Correct answer: 3. A. B. C Only**

## Solution

Circuit-SAT is in NP because an assignment is checked in polynomial time (A), and it is NP-hard—at least as hard as every NP language (B). Hence it is NP-complete (C). D is not a general size law, and P≠NP is consistent with, not contradictory to, NP-completeness, so E is false.

## Key Points

- Circuit-SAT is a canonical NP-complete decision problem.

## Why the other options are incorrect

Every other choice includes D or E and/or omits one of A–C.
