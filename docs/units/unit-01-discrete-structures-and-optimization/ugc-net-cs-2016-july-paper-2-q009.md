# Question 9

*UGC NET CS · 2016 July Paper 2 · Boolean Algebra · Boolean Algebraic Simplification*

Simplify the Boolean expression (AB̄ + AB̄C + AC)(ĀC̄ + B̄).

- **1.** AB̄
- **2.** AB̄C
- **3.** ĀB
- **4.** ABC

> [!TIP]
> **Correct answer: 1. AB̄**

## Solution

First use absorption: AB̄+AB̄C=AB̄, so the first factor is A(B̄+C). Then A(B̄+C)(ĀC̄+B̄)=A(B̄+C)ĀC̄+A(B̄+C)B̄. The first term is zero because AĀ=0; the second becomes AB̄ by absorption, since (B̄+C)B̄=B̄. Therefore the expression simplifies to AB̄.

## Key Points

- Core laws: X+XY=X, X(X+Y)=X, and X·X̄=0.

## Why the other options are incorrect

AB̄C is too restrictive because AB̄ is true whether C is 0 or 1. ĀB has the opposite A/B polarities, and ABC contradicts the required B̄ factor. Direct substitution also distinguishes each from AB̄.
