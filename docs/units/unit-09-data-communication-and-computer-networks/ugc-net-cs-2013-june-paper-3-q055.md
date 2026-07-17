# Question 55

*UGC NET CS · 2013 June Paper 3 · Error Detection and Correction · Even-Parity Encoding*

Given code word 1110001010 is to be transmitted with even parity check bit. The encoded word to be transmitted for this code is

- **A.** 11100010101
- **B.** 11100010100
- **C.** 1110001010
- **D.** 111000101

> [!TIP]
> **Correct answer: A. 11100010101**

## Solution

The data word 1110001010 contains five 1s, which is odd. For even parity, append a parity bit 1 so that the transmitted word contains six 1s. Appending that bit gives 11100010101.

## Key Points

- Even parity chooses the added bit so the total number of 1s, including the parity bit, is even.

## Why the other options are incorrect

B appends 0, leaving the count of 1s odd. C adds no parity bit. D is shorter than the original data word and therefore cannot be the encoded word.
