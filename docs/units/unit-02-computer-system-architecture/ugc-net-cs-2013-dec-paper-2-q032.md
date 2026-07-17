# Question 32

*UGC NET CS · 2013 Dec Paper 2 · Programming the Basic Computer · Input-Output Programming*

Given that (292) 10 = (1204) x in some number system x. The base x of that number system is

- **A.** 2
- **B.** 8
- **C.** 10
- **D.** None of the above

> [!TIP]
> **Correct answer: D. None of the above**

## Solution

Interpret (1204) in base x: x^3+2x^2+0x+4=292. Testing x=6 gives 216+72+4=292, so the base is 6. The digit 4 is valid because a base must exceed its largest digit.

## Key Points

- A numeral d3d2d1d0 in base x has value d3x^3+d2x^2+d1x+d0; also require x greater than every digit.

## Why the other options are incorrect

Base 2 is impossible because digit 4 is not legal. Bases 8 and 10 give 1028 and 1204 respectively, not 292. Since the correct base 6 is not listed, 'none of the above' is correct.
