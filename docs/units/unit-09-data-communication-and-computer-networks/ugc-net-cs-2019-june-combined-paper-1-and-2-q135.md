# Question 135

*UGC NET CS · 2019 June Paper 1 And 2 · OSI and TCP/IP Layer Functions · IPv4 Loopback Address*

Consider the following two statements with respect to IPv4 in computer networking : P: The loopback (IP) address is a member of class B network. Q: The loopback (IP) address is used to send a packet from host to itself. What can you say about the statements P and Q?

- **1.** P-True; Q-False
- **2.** P-False; Q-True
- **3.** P-True; Q-True
- **4.** P-False; Q-False

> [!TIP]
> **Correct answer: 2. P-False; Q-True**

## Solution

The IPv4 loopback block is 127.0.0.0/8, most commonly used as 127.0.0.1. Under classful addressing, a first octet from 1 through 126 is Class A, and 127 is reserved from that part of the address space for loopback; it is not Class B. A packet sent to a loopback address is returned within the same host. Hence P is false and Q is true.

## Key Points

- 127/8 is the reserved IPv4 loopback block used for local host communication and testing.

## Why the other options are incorrect

Options 1 and 3 incorrectly classify loopback as Class B. Option 4 incorrectly denies its host-to-itself purpose.
