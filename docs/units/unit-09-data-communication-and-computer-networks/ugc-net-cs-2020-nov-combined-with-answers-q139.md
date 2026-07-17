# Question 139

*UGC NET CS · 2020 Nov With Answers · Network Security · Caesar Cipher and Diffie–Hellman Key Exchange*

Statement I: In the Caesar cipher, each plaintext letter is replaced by another letter for encryption. Statement II: The Diffie–Hellman algorithm is used to establish a shared secret key. Choose the correct evaluation.

- **1.** Both Statement I and Statement II are true
- **2.** Both Statement I and Statement II are false
- **3.** Statement I is correct but Statement Il is false
- **4.** Statement I is incorrect but Statement II is true

> [!TIP]
> **Correct answer: 1. Both Statement I and Statement II are true**

## Solution

The Caesar cipher is a monoalphabetic substitution cipher: each plaintext letter is replaced by the letter a fixed number of alphabet positions away, so Statement I is true. Diffie–Hellman lets two parties use public values and private exponents to derive the same shared secret over an insecure channel, so Statement II is true in the exam's sense of secret-key establishment. Therefore option 1 is correct.

## Key Points

- Caesar is fixed-shift substitution; Diffie–Hellman is shared-secret key agreement.

## Why the other options are incorrect

Options 2–4 reject one or both true descriptions. More precisely, Diffie–Hellman agrees on a shared secret rather than transmitting the secret itself, and it needs authentication to prevent man-in-the-middle attacks; neither qualification makes the statement false in this context.
