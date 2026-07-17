# Question 112

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · OSI and TCP/IP Layer Functions · Error Detection and Correction*

Consider the routing table of an organization's router as shown in the table given below Subnet Number Subnet Mask Next Hop 12.20.164.0 255.255.252.0 R1 R2 12.20.170.0 255.255.254.0 12.20.168.00 255.255.254.0 Interface O 255.255.254.0 Interface 1 12.20.166.0 R3 Default Which of the following prefixes in CIDR Notation can be collectively used to correctly aggregate all of the subnets in the routing table? A. 12.20.164.0/20 B. 12.20.164.0/22 C. 12.20.164.0/21 D. 12.20.168.0/22 Choose the correct answer from the options given below:

- **1.** A and B Only
- **2.** A and C Only
- **3.** C and D Only
- **4.** B and D Only

> [!TIP]
> **Correct answer: 4. B and D Only**

## Solution

12.20.164.0/22 covers third octets 164–167 (B). The /23 routes 168–169 and 170–171 combine as 12.20.168.0/22 (D). Together B and D exactly cover all listed subnets without unrelated ranges.

## Key Points

- Aggregate only equal adjacent aligned blocks; /22 advances by four in the third octet.

## Why the other options are incorrect

164.0 is not aligned for /21 or /20 and those summaries include addresses outside the given set.
