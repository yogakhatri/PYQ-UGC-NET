# Question 32

*UGC NET CS · 2013 Dec Paper 3 · Network Security · AES Key Sizes and Cryptographic Key Types*

Find the false statement :

- **A.** In Modern Cryptography, symmetric key algorithms use same key both for Encryption and Decryption.
- **B.** The symmetric cipher DES (Data Encryption Standard) was widely used in the industry for security product.
- **C.** The AES (Advanced Encryption Standard) cryptosystem allows variable key lengths of size 56 bits and 124 bits.
- **D.** Public key algorithms use two different keys for Encryption and Decryption.

> [!TIP]
> **Correct answer: C. The AES (Advanced Encryption Standard) cryptosystem allows variable key lengths of size 56 bits and 124 bits.**

## Solution

AES supports three standardized key lengths: 128, 192 and 256 bits. It does not use 56-bit or 124-bit keys, so statement C is false. The distinction is easy to remember: 56 bits is associated with the effective key length of DES, not AES.

## Key Points

- Memorize the standard AES key sizes as 128/192/256 bits; DES uses a 56-bit effective key.

## Why the other options are incorrect

A correctly describes symmetric cryptography: the same secret key is used for encryption and decryption. B is historically correct because DES was widely deployed. D correctly describes public-key cryptography, which uses a related public/private key pair rather than one shared secret.
