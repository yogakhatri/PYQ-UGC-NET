# Question 27

*UGC NET CS · 2017 Jan Paper 3 · Data-Link Layer · CRC Factors and Odd-Error Detection*

Let G(x) be the generator polynomial used for CRC checking. Which condition makes every odd number of bit errors detectable?

- **1.** (1 + x) is factor of G(x)
- **2.** (1−x) is a factor of G(x)
- **3.** (1+x²) is a factor of G(x)
- **4.** x is factor of G(x)

> [!TIP]
> **Correct answer: 1. (1 + x) is factor of G(x)**

## Solution

For a binary CRC, evaluate an error polynomial E(x) at x=1. Any error affecting an odd number of bits has E(1)=1 in GF(2). If G(x) contains the factor x+1, then every multiple of G has value 0 at x=1, so no odd-weight error polynomial can be divisible by G; every odd number of bit errors is detected. The conventional answer is option 1.

## Key Points

- A CRC generator divisible by x+1 detects every error pattern with odd Hamming weight.

## Why the other options are incorrect

Neither x nor 1+x² alone provides the general odd-weight guarantee. There is a flaw in the choices: over GF(2), subtraction equals addition, so 1−x=1+x and option 2 is algebraically identical to option 1. Also, a CRC detects such errors; it does not by itself correct them. Option 1 is the exam-intended notation, but the item has no mathematically unique choice.
