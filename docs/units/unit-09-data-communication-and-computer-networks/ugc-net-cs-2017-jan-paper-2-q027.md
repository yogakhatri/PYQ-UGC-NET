# Question 27

*UGC NET CS · 2017 Jan Paper 2 · OSI and TCP/IP Layer Functions · TCP Byte Stream and Segmentation*

The maximum size of the data that the application layer can pass on to the TCP layer below is __________.

- **1.** 2¹⁶ bytes
- **2.** 2¹⁶ bytes + TCP header length
- **3.** 2¹⁶ bytes − TCP header length
- **4.** 2¹⁵ bytes

> [!TIP]
> **Correct answer: No listed option — an application can pass an arbitrarily long byte stream to TCP, which segments it for transmission**

## Solution

TCP presents a reliable byte-stream service rather than a one-application-write/one-segment message service. An application may supply a large stream; TCP buffers it and divides it into segments governed by the effective MSS and the network path. The 16-bit IPv4 Total Length field constrains one IPv4 datagram, not the total amount an application may pass to TCP. Therefore none of the four fixed sizes answers the question as written.

## Key Points

- Application write size, TCP segment payload (MSS), IP datagram size, and link MTU are different limits at different interfaces.

## Why the other options are incorrect

2¹⁶ and 2¹⁵ confuse per-packet header fields or historical window values with the application-to-TCP interface. Adding a TCP header is dimensionally backward for a payload limit, while subtracting only the TCP header ignores the IP header and still addresses one segment rather than the complete stream.

## Additional Information

This defective item repeats a well-known networking MCQ whose correct answer is 'any size,' but that choice is missing. Actual APIs may impose implementation-specific buffer or call-size limits, not the protocol-level 2¹⁶ choices shown here.

## References

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html)
