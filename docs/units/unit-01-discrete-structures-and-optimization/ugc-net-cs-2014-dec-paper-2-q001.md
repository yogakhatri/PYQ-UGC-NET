# Question 1

*UGC NET CS · 2014 Dec Paper 2 · Counting and Discrete Probability · Inclusion-Exclusion Principle*

Consider A={1,2,3,…,1000}. How many members of A are divisible by 3 or by 5 or by both?

- **A.** 533
- **B.** 599
- **C.** 467
- **D.** 66

> [!TIP]
> **Correct answer: C. 467**

## Solution

Use inclusion-exclusion. Among 1,…,1000 there are floor(1000/3)=333 multiples of 3 and floor(1000/5)=200 multiples of 5. Multiples of both were counted twice; they are the multiples of lcm(3,5)=15, of which there are floor(1000/15)=66. Therefore the union contains 333+200−66=467 numbers.

## Key Points

- For 'divisible by a or b,' add the two counts and subtract multiples of lcm(a,b).

## Why the other options are incorrect

533 simply adds the first two counts and double-counts multiples of 15. 66 counts only the overlap. 599 adds rather than subtracts that overlap. Inclusion-exclusion gives 467.
