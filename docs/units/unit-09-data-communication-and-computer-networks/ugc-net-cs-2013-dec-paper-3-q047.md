# Question 47

*UGC NET CS · 2013 Dec Paper 3 · Data Communication · Asynchronous Serial Framing*

The start and stop bits are used in serial communication for

- **A.** error detection
- **B.** error correction
- **C.** synchronization
- **D.** slowing down the communication

> [!TIP]
> **Correct answer: C. synchronization**

## Solution

In asynchronous serial communication there is no continuously shared clock. A start bit announces the beginning of a character so the receiver can align its sampling times, and one or more stop bits mark the return to the idle state and provide separation before the next character. Their primary purpose is therefore character-level synchronization.

## Key Points

- Asynchronous serial frames use start/stop bits to synchronize each character without a shared clock line.

## Why the other options are incorrect

Start and stop bits do not calculate a parity or checksum, so they are not an error-detection code. They cannot reconstruct corrupted data, so they do not perform error correction. They add overhead and may reduce efficiency, but slowing communication is a consequence rather than their purpose.
