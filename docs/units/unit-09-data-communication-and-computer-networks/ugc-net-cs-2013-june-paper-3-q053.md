# Question 53

*UGC NET CS · 2013 June Paper 3 · Data Communication · Binary Symmetric Channel*

Binary symmetric channel uses

- **A.** Half duplex protocol
- **B.** Full duplex protocol
- **C.** Bit oriented protocol
- **D.** None of the above

> [!TIP]
> **Correct answer: D. None of the above**

## Solution

A binary symmetric channel is an abstract discrete memoryless channel with binary input and output. Each transmitted bit is independently flipped with crossover probability p, with the same probability for 0→1 and 1→0. It is a probabilistic channel model, not a half-duplex protocol, full-duplex protocol or bit-oriented data-link protocol. Therefore none of A–C applies.

## Key Points

- BSC means symmetric independent bit-flip probabilities, not a duplex or framing protocol.

## Why the other options are incorrect

Half duplex and full duplex describe allowed transmission directions. Bit-oriented describes how a data-link protocol frames and controls bit sequences. None of these defines the binary symmetric channel's probabilistic error behavior.
