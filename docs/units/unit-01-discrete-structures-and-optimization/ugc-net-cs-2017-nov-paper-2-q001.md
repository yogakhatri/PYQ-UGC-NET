# Question 1

*UGC NET CS · 2017 Nov Paper 2 · Mathematical Foundations · Modular Arithmetic and Clock Problems*

If the time is now 4 O’clock, what will be the time after 101 hours from now ?

- **1.** 9 O’clock
- **2.** 8 O’clock
- **3.** 5 O’clock
- **4.** 4 O’clock

> [!TIP]
> **Correct answer: 1. 9 O’clock**

## Solution

Clock readings repeat every 12 hours, so only the remainder after division by 12 matters. Since 101 = 8×12 + 5, advancing 101 hours is the same as advancing 5 hours. Starting from 4 o'clock gives 4+5=9 o'clock. Therefore option 1 is correct.

## Key Points

- For a 12-hour clock, compute elapsed time modulo 12: new hour ≡ current hour + elapsed hours (mod 12).

## Why the other options are incorrect

The distractors arise from using the quotient, subtracting the remainder, or failing to reduce 101 modulo 12. A 12-hour clock never requires us to count all 101 hours one by one.
