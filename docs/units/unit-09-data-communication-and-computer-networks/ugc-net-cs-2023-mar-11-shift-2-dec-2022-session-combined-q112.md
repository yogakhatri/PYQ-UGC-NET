# Question 112

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · OSI and TCP/IP Layer Functions · TCP silly-window-syndrome prevention*

Soption 1D-395431 51. No.62 BID:18706: The Solution to Silly Window Syndrome problem is are: A. Nagle's Algorithm B. Clark's Algorithm C. Jacobson's Algorithm D. Piggy backing Algorithm Choose the correct answer from the options given below:

- **1.** A and B Only
- **2.** A and COnly
- **3.** C and D Only
- **4.** B and D Only

> [!TIP]
> **Correct answer: 1. A and B Only**

## Solution

Nagle's algorithm prevents a sender from emitting many tiny segments, while Clark's solution prevents a receiver from advertising tiny window increments. Together they address sender- and receiver-created silly-window syndrome.

## Key Points

- SWS: Nagle at the sender, Clark at the receiver.

## Why the other options are incorrect

Jacobson's work concerns TCP timing/congestion; piggybacking combines acknowledgements with reverse data. Neither is the standard SWS pair.
