# Question 139

*UGC NET CS · 2018 Dec Paper 1 And 2 · Application-Layer Protocols · DNS, TCP Handshake and HTTP Request Order*

Identify the correct sequence in which the following packets are transmitted on the network by a host when a browser requests a webpage from a remote server, assuming that the host has just been restarted.

- **1.** HTTP GET request, DNS query, TCP SYN
- **2.** DNS query, HTTP GET request, TCP SYN
- **3.** TCP SYN, DNS query, HTTP GET request
- **4.** DNS query, TCP SYN, HTTP GET request

> [!TIP]
> **Correct answer: 4. DNS query, TCP SYN, HTTP GET request**

## Solution

Among the three listed packet types, a freshly restarted host first sends a DNS query to translate the server's hostname into an IP address. After learning the address, it starts a TCP connection by sending SYN. Only after the TCP handshake establishes the byte stream can the browser send the HTTP GET request. The sequence is DNS query → TCP SYN → HTTP GET, option 4.

## Key Points

- Resolve name first, establish transport second, send application request third.

## Why the other options are incorrect

Options 1 and 2 place the application request before the transport connection exists. Option 3 sends TCP SYN before resolving the remote server's hostname. Other startup traffic such as DHCP or ARP may also occur in reality, but among the three packet types named, only option 4 has the required dependency order.
