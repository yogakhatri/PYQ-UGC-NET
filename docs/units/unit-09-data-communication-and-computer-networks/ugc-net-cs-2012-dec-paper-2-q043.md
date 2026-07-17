# Question 43

*UGC NET CS · 2012 Dec Paper 2 · Network Security · Encryption and Confidentiality*

Data-encryption techniques are particularly used for:

- **1.** protecting data in a data-communication system
- **2.** reducing storage-space requirements
- **3.** enhancing data integrity
- **4.** decreasing data integrity

> [!TIP]
> **Correct answer: 1. protecting data in a data-communication system**

## Solution

Encryption transforms readable plaintext into ciphertext using a key so that an unauthorized party intercepting communication cannot understand the data. Its primary security service is confidentiality, which is why encryption is especially important in data-communication systems.

## Key Points

- Encryption primarily provides confidentiality.
- Integrity and authenticity require an additional or authenticated cryptographic mechanism.

## Why the other options are incorrect

Compression, not encryption, is intended to reduce storage space. Encryption alone does not guarantee integrity because an attacker may alter ciphertext; integrity normally requires a MAC, digital signature or authenticated-encryption mode. It is certainly not intended to decrease integrity.
