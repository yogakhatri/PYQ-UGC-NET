# Question 142

*UGC NET CS · 2023 Mar 11 Shift 2 Dec 2022 Session · Cloud Computing and IoT · Cloud and Database Storage*

l. No.92 BID:187092 An organization is granted the block 130.56.0.0/16. The administrator wants to create 1024 subnets. Find the subnet prefix.

- **1.** 130.56
- **2.** 136.0
- **3.** 136.255
- **4.** 136.56.255

> [!TIP]
> **Correct answer: 1. 130.56**

## Solution

The supplied block 130.56.0.0/16 has the fixed network prefix represented by its first two octets, 130.56. Creating 2^10 subnets extends the CIDR prefix from /16 to /26, but among the printed textual-prefix choices only 130.56 is meaningful.

## Key Points

- The original address prefix is 130.56; the subnetted CIDR prefix length is /26.

## Why the other options are incorrect

136.0, 136.255, and 136.56.255 are outside the granted 130.56.0.0/16 block.
