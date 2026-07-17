# Question 86

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Data Communication · Digital and Analog Transmission*

In CRC coding if the data word is 111111. divisor is 1010 and the remainder is 110. Which of the following code is true?

- **1.** 011111101
- **2.** 001010110
- **3.** 111111110
- **4.** 110111111

> [!TIP]
> **Correct answer: 3. 111111110**

## Solution

A CRC codeword is formed by appending the r-bit remainder to the original dataword. Here the dataword is 111111 and the remainder is 110, so the transmitted codeword is 111111110.

## Key Points

- CRC transmission word = dataword followed by the modulo-2 division remainder.

## Why the other options are incorrect

The other bit strings do not preserve the six data bits followed by the stated three-bit remainder.
