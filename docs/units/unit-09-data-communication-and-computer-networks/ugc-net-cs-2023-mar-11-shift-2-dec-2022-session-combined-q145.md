# Question 145

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Cloud Computing and IoT · Cloud and Database Storage*

An organization is granted the block 130.56.0.0/16. The administrator wants to create 1024 subnets. Find subnet mask.

- **1.** 130.255.255.255
- **2.** 130.56.255.255
- **3.** 130.56.0.255
- **4.** 130.56.155.192

> [!TIP]
> **Correct answer: No listed option — the subnet mask is 255.255.255.192 (/26)**

## Solution

Creating 1024=2^10 subnets from /16 borrows ten bits, yielding /26. A /26 mask has 26 leading ones: 255.255.255.192. Every printed option incorrectly begins with part of the network address rather than a valid mask.

## Key Points

- New prefix = old prefix + log2(number of equal subnets).

## Why the other options are incorrect

A subnet mask must be contiguous one bits followed by zero bits; none of the displayed 130.56... values is the /26 mask.
