# Question 68

*UGC NET CS · 2019 June Paper 1 And 2 · Data Representation · Number Systems and Conversion*

Consider the equation (146)_b + (313)_(b-2) = (246)_8. Which of the following is the value of b?

- **1.** 8
- **2.** 7
- **3.** 10
- **4.** 16

> [!TIP]
> **Correct answer: 2. 7**

## Solution

Convert each number to an algebraic value. (146)b=b^2+4b+6. Also, (313)(b-2)=3(b-2)^2+(b-2)+3=3b^2-11b+13. Their sum is 4b^2-7b+19. The octal number (246)8 equals 2·64+4·8+6=166. Thus 4b^2-7b-147=0, whose valid positive solution is b=(7+49)/8=7. The other root is negative.

## Key Points

- Translate each positional numeral into a polynomial in its base, equate the values, and reject roots that are invalid bases.

## Why the other options are incorrect

Substituting 8, 10 or 16 does not make the two sides equal. The base must also exceed every digit used; b=7 makes b-2=5, in which digit 3 is valid.
