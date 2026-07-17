# Question 25

*UGC NET CS · 2021 Nov With Answers · Recurrence Relations · Fibonacci Stair-Climbing Count*

Let us assume a person climbing the stairs can take one stair or two stairs at a time. How many ways can this person climb a flight of eight stairs?

- **1.** 21
- **2.** 24
- **3.** 31
- **4.** 34

> [!TIP]
> **Correct answer: 4. 34**

## Solution

Let W(n) be the number of ways to climb n stairs. The final move is either one stair, leaving any W(n−1) route, or two stairs, leaving W(n−2), so W(n)=W(n−1)+W(n−2). With W(0)=1 and W(1)=1, the sequence is 1,1,2,3,5,8,13,21,34. Thus W(8)=34, option 4.

## Key Points

- Condition on the last step; the stair count is a Fibonacci recurrence.

## Why the other options are incorrect

21 is W(7), not W(8), while 24 and 31 do not satisfy the recurrence. Counting only the number of one- and two-steps without arranging them misses distinct orders.
