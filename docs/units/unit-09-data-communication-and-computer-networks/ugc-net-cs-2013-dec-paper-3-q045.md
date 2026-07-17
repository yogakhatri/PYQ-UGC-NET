# Question 45

*UGC NET CS · 2013 Dec Paper 3 · OSI and TCP/IP Layer Functions · Transport Segmentation and Reassembly*

Which layer of OSI reference model is responsible for decomposition of messages and generation of sequence numbers to ensure correct re-composition from end to end of the network ?

- **A.** Physical
- **B.** Data-link
- **C.** Transport
- **D.** Application

> [!TIP]
> **Correct answer: C. Transport**

## Solution

The transport layer provides end-to-end delivery between processes. It segments a large message into smaller transport units, numbers or otherwise tracks them, and reassembles them in the correct order at the destination. These are exactly the decomposition, sequencing and end-to-end recomposition functions in the question.

## Key Points

- Transport is the end-to-end layer for segmentation, sequencing, reliability and reassembly.

## Why the other options are incorrect

The physical layer transmits raw bits. The data-link layer frames data for a single link rather than providing end-to-end message reassembly. The application layer supplies network services to applications but delegates segmentation and sequencing to transport.
