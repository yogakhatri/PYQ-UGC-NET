# Question 93

*UGC NET CS · 2020 Nov With Answers · Pipeline and Vector Processing · Theoretical Pipeline Speedup*

Which statements about a k-segment pipeline are true? (A) The theoretical maximum speedup is k. (B) It is impossible to attain speedup exactly k for a finite workload in a k-segment pipeline. (C) All pipeline segments necessarily take the same computation time.

- **1.** (A) and (B) only
- **2.** (B) and (C) only
- **3.** (A) and (C) only
- **4.** (A), (B) and (C)

> [!TIP]
> **Correct answer: 1. (A) and (B) only**

## Solution

For n tasks in an ideal balanced k-stage pipeline with stage time t, sequential time is nkt while pipeline time is (k+n−1)t. Hence speedup S=nk/(k+n−1). Its limit as n grows is k, so A is true. For every finite n and k>1, k+n−1>n, which makes S<k; exact maximum speedup is not attained, so B is true. Pipeline stages need not inherently have equal computation delays—the clock is set by the slowest stage and balancing is a design objective—so C is false. Therefore option 1.

## Key Points

- The ideal speedup k is an asymptotic upper bound; equal stage times improve utilization but are not required by the definition of pipelining.

## Why the other options are incorrect

Options containing C treat an ideal simplifying assumption as a necessary property of every pipeline. Different stage delays are possible; they simply create idle slack in faster stages and reduce efficiency.
