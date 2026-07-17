# Question 58

*UGC NET CS · 2015 June Paper 3 · Approaches to AI · Branch-and-Bound Bounds and Dominance*

Which of the following statements is true for Branch - and - Bound search ?

- **1.** Underestimates of remaining distance may cause deviation from optimal path.
- **2.** Overestimates can't cause the right path to be overlooked.
- **3.** Dynamic programming principle can be used to discard redundant partial paths.
- **4.** All of the above

> [!TIP]
> **Correct answer: 3. Dynamic programming principle can be used to discard redundant partial paths.**

## Solution

Branch-and-bound may combine dominance with dynamic programming: if two partial paths reach the same subproblem state, a more expensive one is redundant and can be discarded because no continuation can make it better. Statement 3 is therefore true.

## Key Points

- Safe pruning needs valid lower bounds; dominance discards a costlier duplicate state without losing the optimum.

## Why the other options are incorrect

A lower bound that underestimates remaining cost is safe—it may delay pruning but does not remove the optimum—so statement 1 is false. An overestimate can make an optimal branch look too expensive and cause it to be overlooked, so statement 2 is also false. Consequently `All of the above` cannot be correct.
