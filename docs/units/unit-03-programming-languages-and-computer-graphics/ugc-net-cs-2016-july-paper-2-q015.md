# Question 15

*UGC NET CS · 2016 July Paper 2 · Programming in C · Recursive Functions and Arithmetic Series*

Treat the printed C-like function as pseudocode: f(0)=0 and, for n>0, f(n)=n+f(n−2). What value does f(100) return?

- **1.** 2550
- **2.** 2556
- **3.** 5220
- **4.** 5520

> [!TIP]
> **Correct answer: 1. 2550**

## Solution

Expanding the recurrence gives f(100)=100+98+96+⋯+2+f(0). This is the sum of the first 50 positive even integers: 2(1+2+⋯+50)=2·[50·51/2]=50·51=2550. Therefore option 1 is correct.

## Key Points

- Turn a simple additive recursion into an arithmetic series before calculating.

## Why the other options are incorrect

The other numbers result from an incorrect term count, stopping point, or arithmetic-series sum. The base call contributes f(0)=0, and there are exactly 50 positive even terms. Strictly, the source's use of the word 'then' is not valid C syntax; the calculation follows its clearly intended pseudocode.
