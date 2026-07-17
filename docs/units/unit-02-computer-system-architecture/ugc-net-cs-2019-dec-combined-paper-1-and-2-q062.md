# Question 62

*UGC NET CS · 2019 Dec Paper 1 And 2 · Data Representation · Mixed-Base Number Equations*

Given (142)_b + (112)_(b-2) = (75)_8, find the base b.

- **1.** 3
- **2.** 6
- **3.** 7
- **4.** 5

> [!TIP]
> **Correct answer: 4. 5**

## Solution

Convert each numeral to an algebraic value. (142)_b=b²+4b+2. Also (112)_(b−2)=(b−2)²+(b−2)+2=b²−3b+4. The right side (75)_8=7·8+5=61. Hence 2b²+b+6=61, or 2b²+b−55=0=(2b+11)(b−5). A base must be positive and exceed every digit used, so b=5 is valid while −11/2 is not. Thus option 4.

## Key Points

- Expand positional numerals as polynomials in their bases, solve the resulting equation, then enforce digit-validity constraints.

## Why the other options are incorrect

Bases 3 and 4 would not even permit digit 4 in (142)_b; 4 is not listed anyway. Substituting b=6 or 7 does not satisfy the value equation. The secondary base b−2 must also exceed digit 2, reinforcing b>4.
