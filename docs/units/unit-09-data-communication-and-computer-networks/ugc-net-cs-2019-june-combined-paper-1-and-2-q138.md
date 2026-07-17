# Question 138

*UGC NET CS · 2019 June Paper 1 And 2 · OSI and TCP/IP Layer Functions · Classful IPv4 Addressing*

What percentage of the IPv4 address space do all Class C addresses consume?

- **1.** 12.5%
- **2.** 25%
- **3.** 37.5%
- **4.** 50%

> [!TIP]
> **Correct answer: 1. 12.5%**

## Solution

A classful Class C address starts with the fixed three-bit prefix 110. The remaining 29 bits can vary, so Class C occupies 2^29 of the 2^32 possible IPv4 bit patterns. Its fraction is 2^29/2^32=1/8=12.5%.

## Key Points

- A fixed k-bit class prefix represents 1/2^k of the full address space when exactly one prefix pattern belongs to that class.

## Why the other options are incorrect

25%, 37.5% and 50% do not match the one-out-of-eight three-bit prefix pattern allocated to Class C.
