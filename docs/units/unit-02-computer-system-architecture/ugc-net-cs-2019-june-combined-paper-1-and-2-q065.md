# Question 65

*UGC NET CS · 2019 June Paper 1 And 2 · Digital Logic Circuits and Components · Registers and Counters*

How many states are obtained when a MOD-2 counter is followed by a MOD-5 counter?

- **1.** 5
- **2.** 10
- **3.** 15
- **4.** 20

> [!TIP]
> **Correct answer: 2. 10**

## Solution

Cascading a MOD-2 counter with a MOD-5 counter divides the input sequence by 2 and then by 5. The combined modulus is the product 2×5=10, so the cascade passes through ten distinct combined states before repeating.

## Key Points

- For cascaded counters, the overall modulus is the product of the individual moduli when all combined states are used.

## Why the other options are incorrect

- **Option 1:** counts only the MOD-5 stage.
- **Options 3 and 4:** are not the product of the two counter moduli.
