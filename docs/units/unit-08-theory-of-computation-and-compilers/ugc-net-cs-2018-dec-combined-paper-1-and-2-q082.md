# Question 82

*UGC NET CS · 2018 Dec Paper 1 And 2 · Finite Automata · Unary Multiples and Minimum DFA States*

For a fixed positive integer n, consider the unary language L={2^(nk) | k>0}. What is the minimum number of states in a DFA accepting L?

- **1.** n
- **2.** n+1
- **3.** n(n+1)/2
- **4.** 2^n

> [!TIP]
> **Correct answer: 2. n+1**

## Solution

The language contains unary strings whose positive lengths are n,2n,3n,…; the empty string is excluded because k>0. Construct a DFA with a nonaccepting start state q₀, followed by q₁,…,qₙ. Reading the first n copies of `2` moves q₀→q₁→…→qₙ, where qₙ is accepting. Thereafter the n states q₁,…,qₙ form a cycle, so exactly every further multiple of n returns to qₙ. This uses n+1 states. The start and accepting remainder-zero situations cannot be merged because ε must be rejected at the start but accepted after n symbols. Hence option 2.

## Key Points

- Excluding the zero multiple adds one transient start state to the usual n-state modulo-n cycle.

## Why the other options are incorrect

n states would work for multiples including length 0, but k>0 excludes ε and requires a distinct initial state. The quadratic and exponential counts are unnecessary because only a unary length residue plus the first-cycle distinction must be remembered.
