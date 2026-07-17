# Question 2

*UGC NET CS · 2013 Dec Paper 2 · OSI and TCP/IP Layer Functions · Presentation-Layer Encryption*

Encryption and Decryption is the responsibility of _______ Layer.

- **A.** Physical
- **B.** Network
- **C.** Application
- **D.** Datalink

> [!TIP]
> **Correct answer: Presentation layer; none of the listed options is correct**

## Solution

In the seven-layer OSI reference model, the presentation layer translates data representations and is conventionally responsible for encryption/decryption and compression. It prepares application data in a form suitable for transmission and reverses the transformations at the destination.

## Key Points

- OSI mnemonic: presentation layer handles translation, encryption and compression.

## Why the other options are incorrect

The physical layer transmits signals, the data-link layer handles frames on one link, and the network layer routes packets. Applications may themselves perform encryption in real systems, but 'Application' is not the standard OSI-layer answer to this textbook responsibility. The paper omits Presentation from its choices, so the item is defective.
