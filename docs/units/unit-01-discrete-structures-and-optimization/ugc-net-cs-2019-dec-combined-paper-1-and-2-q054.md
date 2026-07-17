# Question 54

*UGC NET CS · 2019 Dec Paper 1 And 2 · Sets and Relations · GLB and LUB in Divisibility Posets*

In the poset (Z+, divides), what are the greatest lower bound (GLB) and least upper bound (LUB) of A={3,9,12} and B={1,2,4,5,10}?

- **1.** A: GLB=3, LUB=36; B: GLB=1, LUB=20
- **2.** A: GLB=3, LUB=12; B: GLB=1, LUB=10
- **3.** A: GLB=1, LUB=36; B: GLB=2, LUB=20
- **4.** A: GLB=1, LUB=12; B: GLB=2, LUB=10

> [!TIP]
> **Correct answer: 1. A: GLB=3, LUB=36; B: GLB=1, LUB=20**

## Solution

Under divisibility, a lower bound must divide every element, so the greatest lower bound of a finite set is its gcd. An upper bound must be divisible by every element, so the least upper bound is its lcm. For A, gcd(3,9,12)=3 and lcm(3,9,12)=36. For B, gcd(1,2,4,5,10)=1 and lcm(1,2,4,5,10)=20. This is option 1.

## Key Points

- In (positive integers, divides), meet/GLB is gcd and join/LUB is lcm.

## Why the other options are incorrect

Twelve is not an upper bound of A because 9 does not divide 12. Ten is not an upper bound of B because 4 does not divide 10. Two is not a lower bound of B because 2 does not divide 1 or 5. These checks eliminate options 2–4.
