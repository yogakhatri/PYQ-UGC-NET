# Question 137

*UGC NET CS · 2018 Dec Paper 1 And 2 · IP Addressing · CIDR Block Subdivision and Alignment*

An Internet Service Provider (ISP) has following chunk of CIDR-based IP addresses available with it: 245.248.128.0/20. The ISP wants to give half of this chunk of addresses to organization A and a quarter to organization B while retaining the remaining with itself. Which of the following is a valid allocation of addresses to A and B?

- **1.** 245.248.136.0/21 and 245.248.128.0/22
- **2.** 245.248.128.0/21 and 245.248.128.0/22
- **3.** 245.248.132.0/22 and 245.248.132.0/21
- **4.** 245.248.136.0/24 and 245.248.132.0/21

> [!TIP]
> **Correct answer: 1. 245.248.136.0/21 and 245.248.128.0/22**

## Solution

The /20 block contains 2^(32-20)=4096 addresses, covering 245.248.128.0 through 245.248.143.255. Half is 2048 addresses, a /21; one valid aligned half is 245.248.136.0/21, covering third-octet values 136–143. A quarter is 1024 addresses, a /22; 245.248.128.0/22 covers 128–131. These blocks are aligned, lie inside the /20, and do not overlap, leaving 132–135 for the ISP. Hence option 1.

## Key Points

- For CIDR subdivision, check all three: required prefix length, boundary alignment, and non-overlap within the parent block.

## Why the other options are incorrect

Option 2 makes B's /22 a subset of A's 128.0/21, so allocations overlap. Option 3 assigns the wrong sizes/order and 132.0 is not a valid /21 boundary. Option 4 gives A only a /24 and gives B a /21, reversing the required half/quarter sizes; its /21 start is also misaligned.
