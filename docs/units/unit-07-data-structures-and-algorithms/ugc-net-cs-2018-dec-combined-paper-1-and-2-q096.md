# Question 96

*UGC NET CS · 2018 Dec Paper 1 And 2 · Algorithm Analysis · Loop Invariants and Partial Correctness*

Let m be a nonnegative integer, and consider the following pseudocode: p = 0; k = 0; while (k < m): p = p + 2^k; k = k + 1; end while. Which of the following is a loop invariant?

- **1.** p = 2^k - 1 and 0 <= k < m
- **2.** p = 2^(k+1) - 1 and 0 <= k < m
- **3.** p = 2^k - 1 and 0 <= k <= m
- **4.** p = 2^(k+1) - 1 and 0 <= k <= m

> [!TIP]
> **Correct answer: 3. p = 2^k - 1 and 0 <= k <= m**

## Solution

After k iterations, p contains the geometric sum 2^0+2^1+...+2^(k-1)=2^k-1. Initially k=0 and p=0=2^0-1. For maintenance, assume p=2^k-1 at the loop head with k<m. The body first makes p=(2^k-1)+2^k=2^(k+1)-1 and then increments k, so the same relation holds for the new k. Also, k begins at 0, increases by one, and can reach m when the guard is tested for the final time. Hence 0≤k≤m, not merely k<m. The invariant is therefore p=2^k-1 and 0≤k≤m, option 3.

## Key Points

- A loop invariant must hold at initialization, after every iteration, and again when the loop terminates; include the final k=m state.

## Why the other options are incorrect

Options 2 and 4 have an off-by-one exponent: at k=0 they require p=1 although p=0. Option 1 has the right sum but excludes the termination-state guard evaluation k=m, so it is not true at every loop head.
