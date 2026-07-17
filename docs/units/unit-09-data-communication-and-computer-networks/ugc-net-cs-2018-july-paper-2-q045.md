# Question 45

*UGC NET CS · 2018 July Paper 2 · Network Security · DES, IDEA, Blowfish and AES Parameters*

Match the following symmetric block ciphers with corresponding block and key sizes : List - I List - II (a) DES (i) block size 64 and key size ranges between 32 and 448 (b) IDEA (ii) block size 64 and key size 64 (c) BLOW FISH (iii) block size 128 and key sizes 128, 192, 256 (d) AES (iv) block size 64 and key size 128 Code : (a) (b) (c) (d)

- **1.** (iv) (ii) (i) (iii)
- **2.** (ii) (iv) (i) (iii)
- **3.** (ii) (iv) (iii) (i)
- **4.** (iv) (ii) (iii) (i)

> [!TIP]
> **Correct answer: 2. (ii) (iv) (i) (iii)**

## Solution

DES uses 64-bit blocks and a 64-bit supplied key (56 effective data bits plus parity), so a→ii. IDEA uses 64-bit blocks and a 128-bit key, so b→iv. Blowfish uses 64-bit blocks and variable keys from 32 to 448 bits, so c→i. AES uses 128-bit blocks and 128-, 192-, or 256-bit keys, so d→iii. The sequence (ii),(iv),(i),(iii) is option 2.

## Key Points

- DES 64/56-effective; IDEA 64/128; Blowfish 64/32–448; AES 128/128–256.

## Why the other options are incorrect

The other codes swap the unmistakable AES and Blowfish parameter sets or confuse DES with IDEA. Remember the DES convention: some tables say 64-bit key size while noting only 56 bits provide cryptographic key material.
