# Question 48

*UGC NET CS · 2018 July Paper 2 · Network Security · Caesar Cipher Decryption*

Decrypt the message “WTAAD” using the Caesar Cipher with key = 15.

- **1.** LIPPS
- **2.** HELLO
- **3.** OLLEH
- **4.** DAATW

> [!TIP]
> **Correct answer: 2. HELLO**

## Solution

With Caesar encryption key 15, ciphertext letters are shifted 15 places forward, so decryption shifts each letter 15 places backward modulo 26. W→H, T→E, A→L, A→L, and D→O. The plaintext is therefore `HELLO`, option 2.

## Key Points

- Caesar decryption uses P=(C−k) mod 26; wrap negative positions around the alphabet.

## Why the other options are incorrect

`LIPPS` is what `HELLO` becomes under a different forward shift of 4, `OLLEH` reverses the decoded word, and `DAATW` is not obtained by subtracting 15. Always state the shift direction before doing modular arithmetic.
