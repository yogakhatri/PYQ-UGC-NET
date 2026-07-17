# Question 1

*UGC NET CS · 2015 June Paper 3 · Data Representation and Error Control · Hamming-Code Syndrome and Error Location*

For the 8 - bit word 00111001, the check bits stored with it would be 0111. Suppose when the word is read from memory, the check bits are calculated to be 1101. What is the data word that was read from memory ?

- **1.** 10011001
- **2.** 00011001
- **3.** 00111000
- **4.** 11000110

> [!TIP]
> **Correct answer: 2. 00011001**

## Solution

The stored and recomputed check-bit patterns differ by `0111 XOR 1101 = 1010₂`. In a Hamming code, this syndrome is the binary index of the erroneous codeword bit, so bit position 10 is wrong. Positions 1, 2, 4, and 8 are check bits; position 10 is a data position and, under the usual least-significant-data-bit-first placement, corresponds to the third bit from the left of `00111001`. Flipping that 1 to 0 gives `00011001`.

## Key Points

- XOR stored and recomputed parity patterns; interpret the result as the one-based Hamming-code error position.

## Why the other options are incorrect

Option 1 flips the most significant data bit, and option 3 flips the least significant bit; neither corresponds to syndrome position 10. Option 4 changes several bits even though a nonzero Hamming syndrome identifies a single-bit error.
