# Question 143

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · OSI and TCP/IP Layer Functions · Error Detection and Correction*

An organization is granted the block 130.56.0.0/16. The administrator wants to create 1024 subnets. Find first and last addresses of First subnet. 130.56.254.254

- **1.** 130.56.0.0
- **2.** 130.56.0.0 130.56.0.63 130.255.255.255
- **3.** 130.0.0.0 130.56.255.63
- **4.** 130.56.0.0

> [!TIP]
> **Correct answer: 2. 130.56.0.0 130.56.0.63 130.255.255.255**

## Solution

Each subnet contains 64 consecutive addresses. The first begins at 130.56.0.0 and spans offsets 0 through 63, so its last address is 130.56.0.63.

## Key Points

- A 64-address subnet advances in blocks of 64: .0–.63, .64–.127, .128–.191, .192–.255.

## Why the other options are incorrect

Other choices extend far beyond a 64-address /26 subnet or leave the granted block.
