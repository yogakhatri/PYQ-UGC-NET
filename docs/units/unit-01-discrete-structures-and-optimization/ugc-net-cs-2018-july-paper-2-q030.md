# Question 30

*UGC NET CS · 2018 July Paper 2 · Boolean Algebra · Exhaustive Search over Truth Assignments*

For an arbitrary Boolean function of n variables, what is the worst-case order of exhaustive search to determine whether some input makes the function output 1?

- **1.** Logarithmic
- **2.** Linear
- **3.** Quadratic
- **4.** Exponential

> [!TIP]
> **Correct answer: 4. Exponential**

## Solution

There are 2ⁿ possible truth assignments to n Boolean variables. An exhaustive algorithm evaluates the function on assignments until it finds output 1; in the worst case, no satisfying assignment exists or the only one is last, so all 2ⁿ assignments must be checked. The running order is therefore exponential, option 4.

## Key Points

- Each Boolean variable doubles the assignment space, producing 2ⁿ possible inputs.

## Why the other options are incorrect

Logarithmic, linear, and quadratic bounds are polynomial and cannot describe enumeration of all 2ⁿ assignments. Special function representations or restricted formula classes may permit faster methods, but the arbitrary worst-case exhaustive test intended here is exponential.
