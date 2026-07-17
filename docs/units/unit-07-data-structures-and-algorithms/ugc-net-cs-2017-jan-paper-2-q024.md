# Question 24

*UGC NET CS · 2017 Jan Paper 2 · Hashing · Universal Hashing and Expected Collisions*

If h is chosen from a universal collection of hash functions and is used to hash n keys into a table of size m, where n ≤ m, the expected number of collisions involving a particular key x is less than _______.

- **1.** 1
- **2.** 1/n
- **3.** 1/m
- **4.** n/m

> [!TIP]
> **Correct answer: 4. n/m**

## Solution

For every other stored key y, universality gives Pr[h(x)=h(y)]≤1/m. Let an indicator variable record whether y collides with x. By linearity of expectation, E[collisions involving x]≤(n−1)/m<n/m. The standard specific bound requested is therefore n/m, option 4.

## Key Points

- Universal hashing: sum at most n−1 collision probabilities, each at most 1/m, to obtain expected collisions below n/m.

## Why the other options are incorrect

1/n and 1/m are bounds for a single probability scale, not the sum over up to n−1 other keys. Because n≤m, the derived expectation is also less than 1, so option 1 is a weaker true statement; option 4 is the tight standard expression in terms of n and m.

## Additional Information

The choices are not logically exclusive: <n/m together with n≤m implies <1. For an MCQ, choose option 4 because it states the informative theorem-level bound; option 1 is only a consequence.
