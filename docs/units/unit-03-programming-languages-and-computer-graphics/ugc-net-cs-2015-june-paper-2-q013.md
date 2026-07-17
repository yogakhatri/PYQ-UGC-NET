# Question 13

*UGC NET CS · 2015 June Paper 2 · Programming in C++ · Operator Precedence and Unsequenced Access*

In C++, given x=7.5, j=−1.0, n=1.0, and m=2.0, evaluate `--x + j == x > n >= m`.

- **1.** 0
- **2.** 1
- **3.** 2
- **4.** 3

> [!TIP]
> **Correct answer: Formally undefined behavior in the C++ version relevant to this paper. If the paper's assumed left operand is evaluated first, the intended result is option 1: 0.**

## Solution

Relational operators bind more tightly than equality and chain left-to-right, so the expression groups as `(--x+j) == ((x>n)>=m)`. Under the paper's intended evaluation, `--x` makes x=6.5 and the left side is 6.5−1=5.5. On the right, x>1 is true (1), then 1>=2 is false (0); 5.5==0 is false, represented as 0. However, the equality operands are not sequenced in the older C++ rules: one modifies x while the other reads x, making the actual program behavior undefined.

## Key Points

- Precedence determines grouping, not evaluation order; an unsequenced modification and read of the same scalar makes the expression undefined.

## Why the other options are incorrect

Values 1, 2, and 3 do not follow from the intended precedence calculation. More importantly, no numeric option describes undefined behavior. This is why real code must split the decrement into its own statement before using x elsewhere in the expression.
