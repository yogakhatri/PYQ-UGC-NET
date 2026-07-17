# Question 25

*UGC NET CS · 2017 Jan Paper 3 · Multiple Access Protocols · Slotted ALOHA Success Probability*

Suppose there are n stations in a slotted LAN. Each station attempts to transmit with a probability P in each time slot. The probability that only one station transmits in a given slot is _______.

- **1.** nP̄(1−P)^(n−1)
- **2.** nP
- **3.** P(1−P)^(n−1)
- **4.** nP(1−P)^(n−1)

> [!TIP]
> **Correct answer: 4. nP(1−P)^(n−1)**

## Solution

Exactly one transmission requires choosing which one of the n stations transmits, probability factor n; that chosen station transmits with probability P; and each of the other n−1 stations remains silent with probability 1−P. Independence gives n·P·(1−P)^(n−1), which is option 4.

## Key Points

- Binomial exactly-one probability: C(n,1)P(1−P)^(n−1).

## Why the other options are incorrect

nP omits the requirement that all other stations be silent. P(1−P)^(n−1) describes success for one specified station but does not account for any of the n stations being the successful one. Option 1 uses the complemented probability for the selected station.
