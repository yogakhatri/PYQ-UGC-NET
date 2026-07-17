# Question 30

*UGC NET CS · 2016 July Paper 3 · Network Security · Block Transposition Cipher*

Encrypt the plain text Message “EXTRANET” using Transposition cipher technique with the following key : 3 5 2 1 4 (Cipher text) 1 2 3 4 5 (Plain text) Using ‘Z’ as bogus character.

- **1.** TAXERTZENZ
- **2.** EXTRANETZZ
- **3.** EZXZTRZANZET
- **4.** EXTZRANZETZ

> [!TIP]
> **Correct answer: 1. TAXERTZENZ**

## Solution

Pad EXTRANET with two Z characters to make two 5-character blocks: EXTRA and NETZZ. The key reads each block in plaintext-position order 3,5,2,1,4. EXTRA becomes T,A,X,E,R → TAXER. NETZZ becomes T,Z,E,N,Z → TZENZ. Concatenating gives TAXERTZENZ, option 1.

## Key Points

- For each fixed-size transposition block, pad first and then read characters in the exact key order.

## Why the other options are incorrect

Option 2 is merely the padded plaintext and performs no permutation. Options 3 and 4 have incorrect lengths or character orders. A block transposition changes positions but neither substitutes letters nor changes the final padded length of 10.
