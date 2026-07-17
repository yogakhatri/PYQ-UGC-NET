# Question 44

*UGC NET CS · 2013 Dec Paper 3 · IPv4 Addressing · Classful Address Classes*

In IPV 4, the IP address 200.200.200.200 belongs to

- **A.** Class A
- **B.** Class B
- **C.** Class C
- **D.** Class D

> [!TIP]
> **Correct answer: C. Class C**

## Solution

Under historical classful IPv4 addressing, the first octet determines the class. Class C addresses begin with bit prefix 110 and have first-octet values 192 through 223. The address 200.200.200.200 begins with 200, which lies in that interval, so it is Class C.

## Key Points

- Classful first-octet ranges: A 1-126, B 128-191, C 192-223, D 224-239.

## Why the other options are incorrect

Class A uses first octets 1-126, Class B uses 128-191, and Class D multicast addresses use 224-239. None includes 200.
