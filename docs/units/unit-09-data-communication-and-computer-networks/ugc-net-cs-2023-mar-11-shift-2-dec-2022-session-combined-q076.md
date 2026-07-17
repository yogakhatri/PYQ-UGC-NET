# Question 76

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · OSI and TCP/IP Layer Functions · Error Detection and Correction*

Let n denote a positive integer. Suppose f(n) is defined as f(n) = 0 if n = 1, and f(n) = f(⌊n/2⌋) + 1 if n > 1. What is f(25), and what does this function find?

- **1.** 4, ⌊log₂ n⌋
- **2.** 14, ⌈log₂ n⌉
- **3.** 4, ⌈n/2⌉
- **4.** 14, ⌊n/2⌋

> [!TIP]
> **Correct answer: 1. 4, ⌊log₂ n⌋**

## Solution

Apply the recurrence repeatedly: f(25)=f(12)+1=f(6)+2=f(3)+3=f(1)+4=4. Each recursive step replaces n by ⌊n/2⌋, so the number of steps before reaching 1 is the position of the highest set bit minus one, namely ⌊log₂n⌋. For n=25, ⌊log₂25⌋=4.

## Key Points

- Repeated integer halving reaches 1 after ⌊log₂n⌋ steps.

## Why the other options are incorrect

The value is not 14; that would confuse the recurrence depth with an arithmetic reduction. The expressions involving n/2 give approximately half the input rather than the number of repeated halvings.

## Question Figure

![Question figure](../../assets/questions/ugc-net-2023-mar11-q76.png)
