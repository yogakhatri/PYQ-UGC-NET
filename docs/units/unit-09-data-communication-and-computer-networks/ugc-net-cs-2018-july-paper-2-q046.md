# Question 46

*UGC NET CS · 2018 July Paper 2 · Computer Networks · Circuit, Packet and Message Switching*

Which of the following statements are true ? (a) Three broad categories of Networks are (i) Circuit Switched Networks (ii) Packet Switched Networks (iii) Message Switched Networks (b) Circuit Switched Network resources need not be reserved during the set up ph ase. (c) In packet switching there is no resource allocation for packets.

- **1.** (a) and (b) only
- **2.** (b) and (c) only
- **3.** (a) and (c) only
- **4.** (a), (b) and (c)

> [!TIP]
> **Correct answer: 3. (a) and (c) only**

## Solution

Statement (a) is true: the standard switching-technique classification includes circuit switching, packet switching, and message switching. Statement (b) is false because a circuit-switched connection reserves an end-to-end path and its resources during call setup. Statement (c) is true in the usual packet-switching contrast: packets share links and buffers on demand rather than receiving a dedicated reservation. Thus only (a) and (c) are true, which is option 3.

## Key Points

- Circuit switching reserves a path before transfer; packet and message switching share store-and-forward resources.

## Why the other options are incorrect

Options 1, 2, and 4 all include statement (b), which reverses the defining setup behavior of circuit switching. Packet networks can schedule and buffer packets, but that is not the dedicated per-connection reservation meant by the question.
