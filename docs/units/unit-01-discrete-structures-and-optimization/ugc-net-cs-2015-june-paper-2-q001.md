# Question 1

*UGC NET CS · 2015 June Paper 2 · Counting, Mathematical Induction and Discrete Probability · Stars-and-Bars Digit Strings*

How many strings of 5 digits have the property that the sum of their digits is 7 ?

- **1.** 66
- **2.** 330
- **3.** 495
- **4.** 99

> [!TIP]
> **Correct answer: 2. 330**

## Solution

A five-digit string here means five positions, so leading zero is allowed. Let the digits be x₁,…,x₅. Because their sum is only 7, the upper digit bound 9 never becomes active. The number of nonnegative solutions of x₁+⋯+x₅=7 is the stars-and-bars count C(7+5−1,5−1)=C(11,4)=330.

## Key Points

- For r labeled positions summing to n with nonnegative entries, use C(n+r−1,r−1) when upper bounds do not bind.

## Why the other options are incorrect

66 and 99 do not count all distributions among five labeled positions. 495 is C(12,4), corresponding to the wrong total. If the question had said five-digit numbers, a leading-zero correction would be necessary; the word strings makes 330 correct.
