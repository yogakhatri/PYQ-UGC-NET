# Question 55

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Data Representation · Number Systems and Conversion*

I. No.: BID: 8700 In 16-bit 2's Complementation representation, the decimal number 28 is

- **1.** 1111 1111 0001 1100
- **2.** 1111 1111 1111 0100
- **3.** 1111 1111 1110 0100
- **4.** 1111 1111 1110 0011

> [!TIP]
> **Correct answer: 3. 1111 1111 1110 0100**

## Solution

The listed patterns all have sign bit 1, so none represents positive 28. The apparent intended value is −28: +28 is 0000 0000 0001 1100; invert and add one to get 1111 1111 1110 0100, option 3.

## Key Points

- For −x in fixed-width two's complement, invert +x and add one.

## Why the other options are incorrect

Taken literally, positive 28 is absent. Options 1,2,4 encode other negative values.
