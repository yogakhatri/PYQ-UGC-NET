# Question 140

*UGC NET CS · 2019 June Paper 1 And 2 · Network Security · Digital Signatures*

RSA can apply the private-key operation to a message value and use the public-key operation to recover or verify it. This property is used in:

- **1.** intrusion detection systems C
- **2.** digital signatures
- **3.** data compression
- **4.** certification

> [!TIP]
> **Correct answer: 2. digital signatures**

## Solution

This is the core public-verification idea behind an RSA digital signature. The signer uses the private exponent on a properly encoded message digest, and anyone with the public key can verify that signature. Confidential encryption uses the opposite key direction: public key to encrypt, private key to decrypt.

## Key Points

- RSA confidentiality: public encrypts, private decrypts.
- RSA signature: private signs, public verifies.

## Why the other options are incorrect

Intrusion detection and data compression are unrelated to RSA key reversal. Certification binds an identity to a public key, but the direct cryptographic use described is a digital signature; certificates themselves are authenticated using signatures.
