# Question 116

*UGC NET CS · 2019 June Paper 1 And 2 · Data Structures · Hashing*

Consider double hashing h(k,i)=(h1(k)+i*h2(k)) mod m, where h1(k)=k mod m, h2(k)=1+(k mod n), n=m-1 and m=701. For k=123456, what is the difference between the first and second probes in number of slots?

- **1.** 255
- **2.** 256
- **3.** 257
- **4.** 258

> [!TIP]
> **Correct answer: 3. 257**

## Solution

Consecutive probes differ by the second hash value h2(k), modulo the table size. Here n=m-1=700, so h2(123456)=1+(123456 mod 700). Since 123456=700x176+256, the remainder is 256 and h2=257. Therefore the second probe is 257 slots ahead of the first, cyclically modulo 701.

## Key Points

- In double hashing, the probe step is h2(k); compute the remainder first and then apply the formula's +1.

## Why the other options are incorrect

255 and 256 omit or mishandle the required +1. The value 258 adds one twice.
