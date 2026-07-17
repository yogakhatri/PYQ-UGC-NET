# Question 11

*UGC NET CS · 2015 Dec Paper 2 · C Programming · Iterative Series Computation*

A C program initializes term = 1 and sum = 0, then repeats for i = 1 through inp: term = term × x / i; sum = sum + term. Which series does it compute?

- **1.** x + x²/2 + x³/3 + x⁴/4 + ...
- **2.** x + x²/2! + x³/3! + x⁴/4! + ...
- **3.** 1 + x²/2 + x³/3 + x⁴/4 + ...
- **4.** 1 + x²/2! + x³/3! + x⁴/4! + ...

> [!TIP]
> **Correct answer: 2. x + x²/2! + x³/3! + x⁴/4! + ...**

## Solution

Initially term=1. After iteration i=1, term=x and sum=x. If before iteration i the term is x^(i−1)/(i−1)!, the update term←term·x/i makes it x^i/i!. Therefore successive additions are x, x²/2!, x³/3!, …, x^inp/inp!. Since sum starts at 0 and the program never adds the initial term 1, the computed series is option 2, the truncated expansion of e^x−1.

## Key Points

- Trace the loop invariant: after iteration i, term=x^i/i!.

## Why the other options are incorrect

Options 1 and 3 use denominators i rather than i!, ignoring the cumulative division in the recurrence. Option 4 wrongly includes the constant term 1.
