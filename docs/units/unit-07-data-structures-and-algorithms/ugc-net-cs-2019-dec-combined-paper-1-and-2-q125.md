# Question 125

*UGC NET CS · 2019 Dec Paper 1 And 2 · Parallel Algorithms · Work, Span and Parallelism*

A multithreaded algorithm pTrans(X,Y,N) computes a matrix transpose in parallel: for N=1 it copies one entry; otherwise it partitions X and Y into four (N/2)×(N/2) submatrices and spawns pTrans independently on all four corresponding pairs. What is its asymptotic parallelism T1/T∞?

- **1.** Θ(N²/log N)
- **2.** Θ(N/log N)
- **3.** Θ(log N/N²)
- **4.** Θ(log N/N)

> [!TIP]
> **Correct answer: 1. Θ(N²/log N)**

## Solution

The total work satisfies T1(N)=4T1(N/2)+Θ(1), because all four subproblems must eventually execute; therefore T1(N)=Θ(N²). With unlimited processors, the four spawned calls at a level run concurrently, so only one recursive chain lies on the critical path: T∞(N)=T∞(N/2)+Θ(1)=Θ(log N). Parallelism is T1/T∞=Θ(N²/log N), option 1.

## Key Points

- Work counts every spawned branch; span follows only the longest dependent branch.
- Divide Θ(N²) by Θ(log N).

## Why the other options are incorrect

Option 2 uses only linear work even though every one of the N² matrix entries is copied. Options 3 and 4 invert work and span, producing quantities that shrink toward zero; available parallelism cannot be less than one for this growing computation.
