# Question 63

*UGC NET CS · 2019 June Paper 1 And 2 · Boolean Algebra · Boolean Functions and their Representation*

How many different Boolean functions of degree n are there?

- **1.** 2^(2^n)
- **2.** (2^n)^n
- **3.** 2^(2^n)-1
- **4.** 2^n

> [!TIP]
> **Correct answer: 1. 2^(2^n)**

## Solution

A Boolean function of n variables assigns either 0 or 1 to every possible n-bit input. There are 2^n possible inputs, and the function independently chooses one of two output values for each input. Therefore the total number of functions is 2 raised to the number of inputs: 2^(2^n).

## Key Points

- A Boolean function is a complete assignment of one output bit to each of the 2^n input rows.

## Why the other options are incorrect

- **Option 2:** does not count independent output assignments to the truth-table rows.
- **Option 3:** incorrectly removes one valid Boolean function.
- **Option 4:** counts input combinations, not functions over those inputs.
