# Question 37

*UGC NET CS · 2012 Dec Paper 2 · Network Security · AES Key Sizes and Rounds*

AES is a round cipher based on the Rijndael algorithm using a 128-bit block. How many rounds are used with 128-, 192-, and 256-bit keys, respectively?

- **1.** 5, 7, 15
- **2.** 10, 12, 14
- **3.** 5, 6, 7
- **4.** 20, 12, 14

> [!TIP]
> **Correct answer: 2. 10, 12, 14**

## Solution

AES always uses a 128-bit data block, but the number of rounds depends on key length. AES-128 uses 10 rounds, AES-192 uses 12 rounds, and AES-256 uses 14 rounds. The initial AddRoundKey step is separate from this standard round count.

## Key Points

- Memorize AES key/round pairs: 128/10, 192/12, 256/14; block size remains 128 bits.

## Why the other options are incorrect

The other triples do not match the AES specification and do not follow its two-round increase as key size rises from 128 to 192 to 256 bits.
