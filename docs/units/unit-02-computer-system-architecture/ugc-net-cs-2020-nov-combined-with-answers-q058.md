# Question 58

*UGC NET CS · 2020 Nov With Answers · Data Representation · Radix from Polynomial Roots*

In an unknown radix b, the quadratic equation x²−(10)_b x+(26)_b=0 has roots x=4 and x=7. What is b?

- **1.** 8
- **2.** 9
- **3.** 10
- **4.** 11

> [!TIP]
> **Correct answer: 4. 11**

## Solution

Interpret the numerals in base b: (10)_b=b and (26)_b=2b+6. For a monic quadratic with roots 4 and 7, Vieta's formulas give root sum 4+7=11 and root product 4×7=28. The coefficient of x equals the root sum, so b=11. The product check also works: 2b+6=22+6=28. Therefore the radix is 11, option 4.

## Key Points

- Convert base-b coefficients to values, then apply Vieta: sum=b and product=2b+6.

## Why the other options are incorrect

Bases 8, 9, and 10 make the numeral (10)_b equal 8, 9, or 10, none matching the required root sum 11. Substitution into the constant term gives the same rejection.
