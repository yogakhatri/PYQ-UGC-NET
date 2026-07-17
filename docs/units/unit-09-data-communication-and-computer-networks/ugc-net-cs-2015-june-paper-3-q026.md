# Question 26

*UGC NET CS · 2015 June Paper 3 · Transport Layer · TCP FIN Flag*

Which of the following control fields in TCP header is used to specify whether the sender has no more data to transmit ?

- **1.** FIN
- **2.** RST
- **3.** SYN
- **4.** PSH

> [!TIP]
> **Correct answer: 1. FIN**

## Solution

TCP sets the FIN flag when a sender has finished sending data in that direction and wants to close its half of the connection. FIN consumes one sequence number and is acknowledged, allowing an orderly full-duplex shutdown.

## Key Points

- SYN opens, FIN closes gracefully, RST aborts, and PSH requests prompt delivery.

## Why the other options are incorrect

RST aborts or resets a connection. SYN synchronizes initial sequence numbers during connection establishment. PSH asks the receiver to deliver buffered data promptly; it does not announce end of data.
