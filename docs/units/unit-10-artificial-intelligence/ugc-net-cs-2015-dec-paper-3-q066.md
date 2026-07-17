# Question 66

*UGC NET CS · 2015 Dec Paper 3 · Fuzzy Sets · Generalized Bell Membership Function*

Which formula is the generalized bell-shaped fuzzy membership function with parameters (a,b,c)?

- **1.** 1 / (1 + ((x−c)/a)^b)
- **2.** 1 / (1 + ((x−c)/a)^(2b))
- **3.** 1 + ((x−c)/a)^b
- **4.** 1 − ((x−c)/a)^(2b)

> [!TIP]
> **Correct answer: 2. 1 / (1 + ((x−c)/a)^(2b))**

## Solution

The generalized bell membership function is μ(x)=1/[1+|((x−c)/a)|^{2b}]. Parameter c fixes the center where membership is 1, |a| controls the width, and b controls the slope of the sides. The paper suppresses the absolute-value bars, but its second expression has the defining reciprocal form and exponent 2b.

## Key Points

- Generalized bell: reciprocal of 1 plus an even-powered normalized distance from center c.

## Why the other options are incorrect

Option 1 uses exponent b and can lose the required left-right bell symmetry. Options 3 and 4 are not reciprocal bounded bell functions: they can exceed 1 or become negative, violating the membership-value range [0,1].
