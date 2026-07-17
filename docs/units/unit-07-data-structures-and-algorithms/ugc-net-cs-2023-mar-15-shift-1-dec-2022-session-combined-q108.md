# Question 108

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Performance Analysis and Recurrences · Time and Space Complexity*

For matrix multiplication, if we use divide and conquer algorithm, then A. the running time is T(n)=©(n) B. the running time is T(n) = 0(n? log n) C. The recurrence can be defined as T(n) = 8T(n/2) +©(n?) D. the recurrence relation is T(n) = 8(2n) +e(n-log n) E. Masters theorem, one of the cases is applicable Choose the most appropriate answer from the options given below:

- **1.** A, C, E only
- **2.** A, D, E only
- **3.** B, D, E only
- **4.** B, C, D only

> [!TIP]
> **Correct answer: 1. A, C, E only**

## Solution

Classical divide-and-conquer matrix multiplication performs eight n/2 multiplications plus Θ(n²) additions: T(n)=8T(n/2)+Θ(n²) (C). Master theorem has a=8,b=2, n^(log_b a)=n³, so T(n)=Θ(n³) (A), and the theorem applies (E).

## Key Points

- Eight half-size products preserve cubic time; Strassen reduces the number to seven.

## Why the other options are incorrect

B gives the wrong asymptotic time; D is not the correct subproblem recurrence.
