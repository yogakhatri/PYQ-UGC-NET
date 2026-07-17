# Question 75

*UGC NET CS · 2019 Dec Paper 1 And 2 · Network Security · Cryptography*

Which of the following is not needed by an encryption algorithm used in Cryptography?

- **1.** KEY
- **2.** Message
- **3.** Ciphertext
- **4.** User details

> [!TIP]
> **Correct answer: 4. User details**

## Solution

An encryption transformation operates on a plaintext message under a key and produces ciphertext. It does not need personal user details as part of the cryptographic transformation. Therefore option 4 is the item not needed by the encryption algorithm.

## Key Points

- Core encryption model: ciphertext C = E_K(plaintext M); user metadata is outside E.

## Why the other options are incorrect

The message is the data being encrypted, and the key controls the transformation. Ciphertext is the required output of encryption and the input to decryption. User identity or profile data may matter to an application or key-management system, but not to the encryption function itself.
