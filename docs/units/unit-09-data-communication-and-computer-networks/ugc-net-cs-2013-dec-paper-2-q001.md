# Question 1

*UGC NET CS · 2013 Dec Paper 2 · Data-Link-Layer Protocols · Piggybacked Acknowledgements*

When data and acknowledgement are sent in the same frame, this is called as

- **A.** Piggy packing
- **B.** Piggy backing
- **C.** Back packing
- **D.** Good packing

> [!TIP]
> **Correct answer: B. Piggy backing**

## Solution

In bidirectional data transfer, a receiver can delay its acknowledgement briefly and attach it to a data frame travelling in the reverse direction. Sending the data and acknowledgement together avoids a separate acknowledgement-only frame. This efficiency technique is called piggybacking.

## Key Points

- Piggybacking combines an acknowledgement with an outgoing data frame in the reverse direction to reduce protocol overhead.

## Why the other options are incorrect

'Piggy packing', 'back packing' and 'good packing' are not the data-link protocol term. The name comes from the acknowledgement riding on, or piggybacking on, reverse-direction data.
