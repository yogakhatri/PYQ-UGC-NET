# Question 50

*UGC NET CS · 2018 July Paper 2 · Network Security · Block Transposition Cipher*

Encrypt the Message “HELLO MY DEARZ” using Transposition Cipher w ith P lain Text 2 4 1 3Key Cipher Text 1 2 3 4   

- **1.** HLLEO YM AEDRZ
- **2.** EHOLL ZYM RAED
- **3.** ELHL MDOY AZER
- **4.** ELHL DOMY ZAER

> [!TIP]
> **Correct answer: 3. ELHL MDOY AZER**

## Solution

Remove the spaces and split `HELLOMYDEARZ` into four-character blocks: `HELL | OMYD | EARZ`. The key maps plaintext positions 2,4,1,3 into ciphertext positions 1,2,3,4. Thus `HELL`→`ELHL`, `OMYD`→`MDOY`, and `EARZ`→`AZER`. Restoring spaces between blocks gives `ELHL MDOY AZER`, option 3.

## Key Points

- For block transposition, partition first and then apply the same positional permutation independently to every block.

## Why the other options are incorrect

Each other choice uses a different permutation or preserves word boundaries instead of applying the printed four-position key to consecutive blocks. A reliable method is to label every character 1–4 and copy them in the exact order 2,4,1,3.
