# Question 30

*UGC NET CS · 2014 Dec Paper 3 · Network Security · Public and Private Keys*

Which one of the following is true for asymmetric-key cryptography ?

- **A.** Private key is kept by the receiver and public key is announced to the public.
- **B.** Public key is kept by the receiver and private key is announced to the public.
- **C.** Both private key and public key are kept by the receiver.
- **D.** Both private key and public key are announced to the public.

> [!TIP]
> **Correct answer: A. Private key is kept by the receiver and public key is announced to the public.**

## Solution

In public-key cryptography, each receiver generates a mathematically related key pair. The public key is distributed openly so senders can encrypt for that receiver or verify the receiver's signatures. The private key remains secret with its owner so only that owner can decrypt the corresponding ciphertext or create the signature. Therefore A states the required ownership and publication pattern.

## Key Points

- Publish the public key; protect the private key.
- Which key performs an operation depends on encryption versus signing, but secrecy roles never reverse.

## Why the other options are incorrect

B reverses the secrecy roles and would expose the key that must remain private. C prevents senders or verifiers from obtaining the public key. D publishes the private key and destroys confidentiality and authentication. A alone preserves the asymmetric trust model.
