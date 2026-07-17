# Question 84

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Data Communication · Digital and Analog Transmission*

SI. N: 87034 In CRC coding if the data word is 111111, divisor is 1010 and the remainder is 110. Which of the following code is true?

- **1.** 011111101
- **2.** 001010110
- **3.** 111111110
- **4.** 110111111

> [!TIP]
> **Correct answer: 3. 111111110**

## Solution

Append the stated three-bit CRC remainder 110 to dataword 111111, producing codeword 111111110.

## Key Points

- CRC codeword = dataword || remainder.

## Why the other options are incorrect

Other strings do not consist of the unchanged dataword followed by the given remainder.
