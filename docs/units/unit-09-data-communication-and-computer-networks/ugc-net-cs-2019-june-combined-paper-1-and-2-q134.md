# Question 134

*UGC NET CS · 2019 June Paper 1 And 2 · OSI and TCP/IP Layer Functions · IPv4 Subnetting*

Using a Class B network, you need at least 500 subnets with about 100 usable host addresses in each. Which subnet mask should be assigned?

- **1.** 255.255.255.252 (/30)
- **2.** 255.255.255.128 (/25)
- **3.** 255.255.255.0 (/24)
- **4.** 255.255.254.0 (/23)

> [!TIP]
> **Correct answer: 2. 255.255.255.128 (/25)**

## Solution

A Class B network starts with a /16 prefix. At least 500 subnets require 9 borrowed bits because 2^8=256 is too small and 2^9=512. This leaves 16-9=7 host bits per subnet, giving 2^7-2=126 usable host addresses, enough for about 100 hosts. The resulting prefix is /25, whose dotted-decimal mask is 255.255.255.128.

## Key Points

- Choose borrowed subnet bits first, then verify remaining host bits: /16 + 9 = /25, leaving 126 usable addresses.

## Why the other options are incorrect

- **/30:** many subnets but only 2 usable hosts each.
- **/24:** 256 subnets from a /16, fewer than 500.
- **/23:** only 128 subnets from a /16.
