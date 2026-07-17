# Question 144

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · OSI and TCP/IP Layer Functions · Error Detection and Correction*

An organization is granted the block 130.56.0.0/16. The administrator wants to create 1024 subnets. Find first and last addresses of last subnet. 130.56.254.255

- **1.** 130.56.0.0 130.56.255.255
- **2.** 130.56.255.0
- **3.** 130.56.0.192 130.255.255.255
- **4.** 130.56.255.192 130.56.255.255

> [!TIP]
> **Correct answer: 4. 130.56.255.192 130.56.255.255**

## Solution

The last /24-sized octet region is 130.56.255.x, and its last /26 block begins at the final multiple of 64, 192. It therefore runs from 130.56.255.192 through 130.56.255.255.

## Key Points

- The final /26 within any /24 is .192–.255.

## Why the other options are incorrect

The other ranges either begin at the first subnet, cross the block boundary, or do not contain exactly 64 addresses.
