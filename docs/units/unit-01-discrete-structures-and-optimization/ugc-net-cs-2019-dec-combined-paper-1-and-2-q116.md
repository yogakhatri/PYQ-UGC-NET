# Question 116

*UGC NET CS · 2019 Dec Paper 1 And 2 · Group Theory · Element Orders and Cauchy's Theorem*

Consider: S1: If a finite group (G,*) has order n and a∈G satisfies a^m=e for some integer m≤n, then m must divide n. S2: If (G,*) has even order, then some a∈G satisfies a≠e and a*a=e. Which statement(s) are correct?

- **1.** Only S1
- **2.** Only S2
- **3.** Both S1 and S2
- **4.** Neither S1 nor S2

> [!TIP]
> **Correct answer: 2. Only S2**

## Solution

S1 is false because m is merely some exponent with a^m=e, not necessarily the order of a. In a group of order 6, take an element a of order 2: a^4=e and 4≤6, but 4 does not divide 6. Lagrange's theorem says the element order—not every multiple m producing e—divides the group order. S2 is true by Cauchy's theorem: because 2 divides an even group order, the group has an element of order 2, so a≠e and a²=e. Hence only S2 is correct, option 2.

## Key Points

- ord(a) divides |G|; an arbitrary m satisfying a^m=e is only required to be a multiple of ord(a).

## Why the other options are incorrect

Options 1 and 3 incorrectly replace 'some exponent m' with 'the least positive exponent,' which is the element order. Option 4 ignores Cauchy's theorem for the prime 2. The distinction between m and ord(a) is the entire trap.
