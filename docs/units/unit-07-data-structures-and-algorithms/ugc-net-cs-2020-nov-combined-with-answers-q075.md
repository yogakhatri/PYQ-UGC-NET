# Question 75

*UGC NET CS · 2020 Nov With Answers · Performance Analysis and Recurrences · Input Size Solvable in Fixed Time*

Algorithms A and B take log₂(n) microseconds and √n microseconds, respectively. What largest problem sizes can they solve in one second?

- **1.** 2^(10^6) and 10^6
- **2.** 2^(10^6) and 10^12
- **3.** 2^(10^6) and 6×10^6
- **4.** 2^(10^6) and 6×10^12

> [!TIP]
> **Correct answer: 2. 2^(10^6) and 10^12**

## Solution

One second equals 10^6 microseconds. For A, require log₂n≤10^6, giving n≤2^(10^6). For B, require √n≤10^6; squaring yields n≤(10^6)²=10^12. Thus the largest sizes are 2^(10^6) and 10^12, option 2.

## Key Points

- Convert the time budget to microseconds, set each running time equal to it, and invert the function.

## Why the other options are incorrect

10^6 for B forgets to square after solving √n=10^6. Factors such as 6×10^6 or 6×10^12 incorrectly mix the number of microseconds with the exponent notation. A's logarithm must be inverted with a power of two.
