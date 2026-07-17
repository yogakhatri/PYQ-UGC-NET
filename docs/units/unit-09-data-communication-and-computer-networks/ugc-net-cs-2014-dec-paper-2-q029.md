# Question 29

*UGC NET CS · 2014 Dec Paper 2 · Data Communication · Bit Rate versus Baud Rate*

An analog signal has a bit rate of 6000 bps and a baud rate of 2000 baud. How many data elements are carried by each signal element ?

- **A.** 0.336 bits/baud
- **B.** 3 bits/baud
- **C.** 120,00,000 bits/baud
- **D.** None of the above

> [!TIP]
> **Correct answer: B. 3 bits/baud**

## Solution

Bit rate counts data bits per second, while baud rate counts signal elements per second. The number of data elements carried by each signal element is 6000/2000=3 bits per baud. Equivalently, a signal element must select among 2³=8 distinguishable states.

## Key Points

- Bits per signal element = bit rate ÷ baud rate; M signal states carry log₂M bits.

## Why the other options are incorrect

0.336 approximately reverses the division. 12,000,000 multiplies rates with incompatible units. Since 3 is listed exactly, 'none' is false.
