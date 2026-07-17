# Question 48

*UGC NET CS · 2015 Dec Paper 2 · Combinatorics · Stars and Bars with Lower Bounds*

How many integer solutions satisfy x+y+z+u=29, subject to x≥1, y≥2, z≥3, and u≥0?

- **1.** 4960
- **2.** 2600
- **3.** 23751
- **4.** 8855

> [!TIP]
> **Correct answer: 2. 2600**

## Solution

Remove the lower bounds by defining x'=x−1, y'=y−2, z'=z−3, and u'=u. These four variables are nonnegative and satisfy x'+y'+z'+u'=29−1−2−3=23. By stars and bars, the number of nonnegative solutions is C(23+4−1,4−1)=C(26,3)=26·25·24/6=2,600.

## Key Points

- Shift away lower bounds, then count nonnegative solutions to a sum with C(N+k−1,k−1).

## Why the other options are incorrect

The other numbers result from applying stars and bars before subtracting all lower bounds or using the wrong number of separators. Four variables require three separators.
