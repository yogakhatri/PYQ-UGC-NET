# Question 57

*UGC NET CS · 2018 Dec Paper 1 And 2 · Boolean Algebra · Boolean Expression Simplification*

The Boolean expression A̅B + AB̅ + AB is equivalent to:

- **1.** A̅B
- **2.** (A+B)̅
- **3.** AB
- **4.** A+B

> [!TIP]
> **Correct answer: 4. A+B**

## Solution

Simplify F=A̅B+AB̅+AB. Combine the last two terms: AB̅+AB=A(B̅+B)=A. Hence F=A+A̅B. Using absorption in the form X+X̅Y=X+Y gives F=A+B. Therefore option 4 is correct.

## Key Points

- Use complementarity and absorption: X(X̅+X)=X and X+X̅Y=X+Y.

## Why the other options are incorrect

A̅B and AB retain only one product term and miss valid input cases. (A+B)̅=A̅B̅ is the NOR function, not the given expression. A quick truth-table check at A=1 or B=1 confirms that the original function is 1 whenever A+B is 1.
