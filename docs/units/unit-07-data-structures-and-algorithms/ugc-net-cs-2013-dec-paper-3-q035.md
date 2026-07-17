# Question 35

*UGC NET CS · 2013 Dec Paper 3 · Divide and Conquer · Strassen Matrix Multiplication*

Let A and B be two n × n matrices. The efficient algorithm to multiply the two matrices has the time complexity

- **A.** O(n 3)
- **B.** O(n 2.81)
- **C.** O(n 2.67)
- **D.** O(n 2)

> [!TIP]
> **Correct answer: B. O(n 2.81)**

## Solution

Strassen's divide-and-conquer method partitions each matrix into four blocks but computes the block products using seven recursive multiplications instead of eight. Its recurrence is T(n)=7T(n/2)+O(n^2). By the Master theorem, T(n)=Theta(n^(log2 7)); since log2 7 is about 2.807, this is conventionally written O(n^2.81).

## Key Points

- Strassen: seven half-size multiplications lead to n^(log2 7) ≈ n^2.81.

## Why the other options are incorrect

O(n^3) is the classical three-loop algorithm, not the more efficient algorithm intended here. The listed O(n^2.67) is not Strassen's bound. O(n^2) would match the input/output size scale but is not achieved by Strassen and was not a known general matrix-multiplication bound in this exam context.
