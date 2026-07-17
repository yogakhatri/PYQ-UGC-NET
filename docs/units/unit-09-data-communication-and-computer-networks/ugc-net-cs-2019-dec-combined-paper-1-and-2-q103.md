# Question 103

*UGC NET CS · 2019 Dec Paper 1 And 2 · IPv4 Addressing · Classful Address Classes*

Which of the following class of IP address has the last address as 223.255.255.255?

- **1.** Class A
- **2.** Class B
- **3.** Class C
- **4.** Class D

> [!TIP]
> **Correct answer: 3. Class C**

## Solution

In historical classful IPv4 addressing, Class C addresses have first octets from 192 through 223. Setting every remaining octet to 255 gives the last address in that class: 223.255.255.255. Therefore the address belongs to Class C, option 3.

## Key Points

- Classful first-octet ranges: A 1–126, B 128–191, C 192–223, D 224–239.

## Why the other options are incorrect

Class A uses first octets 1–126, Class B uses 128–191, and Class D multicast addresses begin at 224 and run through 239. None can have first octet 223.
