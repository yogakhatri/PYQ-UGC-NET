# Question 83

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · OSI and TCP/IP Layer Functions · MAC-address notation*

Given Ethernet address 01011010 00010001 01010101 00011000 10101010 00001111 in binary, what is the address in hexadecimal notation?

- **1.** 5A:88:AA:18:55:FO
- **2.** 5A:81:BA:81:AA:08
- **3.** 5A:18:5A:18:55:0F
- **4.** 5A:11:55:18:AA:OF

> [!TIP]
> **Correct answer: 4. 5A:11:55:18:AA:OF**

## Solution

Convert each 8-bit octet independently: 01011010=5A, 00010001=11, 01010101=55, 00011000=18, 10101010=AA, and 00001111=0F. Joining the six bytes gives 5A:11:55:18:AA:0F.

## Key Points

- Split a 48-bit MAC address into six bytes, then convert each group of four bits to one hexadecimal digit.

## Why the other options are incorrect

The other choices alter one or more byte values or reverse nibbles. Ethernet notation preserves the byte order shown and uses exactly two hexadecimal digits per byte.
