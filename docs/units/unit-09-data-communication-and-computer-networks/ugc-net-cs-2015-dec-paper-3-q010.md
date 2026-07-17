# Question 10

*UGC NET CS · 2015 Dec Paper 3 · Transport Layer · Socket Addresses and Transport Endpoints*

The combination of an IP address and a port number is known as ___________.

- **1.** network number
- **2.** socket address
- **3.** subnet mask number
- **4.** MAC address

> [!TIP]
> **Correct answer: 2. socket address**

## Solution

A transport endpoint is identified by an IP address plus a port number. This pair is called a socket address, commonly written as `IP:port`; it identifies the host/interface and the application endpoint on that host.

## Key Points

- Socket address = network-layer IP address + transport-layer port.

## Why the other options are incorrect

A network number identifies an IP network prefix, a subnet mask separates network and host bits, and a MAC address identifies a link-layer interface. None includes the transport port.
