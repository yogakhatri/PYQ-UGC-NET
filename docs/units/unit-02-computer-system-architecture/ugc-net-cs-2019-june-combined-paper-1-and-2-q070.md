# Question 70

*UGC NET CS · 2019 June Paper 1 And 2 · Pipeline and Vector Processing · Amdahl's law*

Suppose that a computer program takes 100 seconds of execution time on a computer, with the multiplication operation responsible for 80 seconds of this time. How much do you have to improve the speed of multiplication if you are asked to execute this program four times faster?

- **1.** 14 times faster
- **2.** 15 times faster
- **3.** 16 times faster
- **4.** 17 times faster

> [!TIP]
> **Correct answer: 3. 16 times faster**

## Solution

A fourfold speedup reduces total execution time from 100 seconds to 25 seconds. The non-multiplication part already consumes 20 seconds and is unchanged, leaving only 5 seconds for multiplication. The multiplication time must therefore fall from 80 seconds to 5 seconds, requiring a speedup of 80/5=16.

## Key Points

- Apply Amdahl's law to time: target total time minus the unchanged portion gives the allowed improved time.

## Why the other options are incorrect

With a 14× or 15× multiplication speedup, the total remains above 25 seconds. A 17× speedup is more than the minimum required. The exact factor is 16.
