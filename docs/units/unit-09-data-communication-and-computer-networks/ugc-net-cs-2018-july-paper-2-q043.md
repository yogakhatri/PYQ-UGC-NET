# Question 43

*UGC NET CS · 2018 July Paper 2 · IPv4 Addressing · Binary-to-Dotted-Decimal Conversion*

Convert the IPv4 address 10000001 00001011 00001011 11101111 from binary to dotted-decimal notation.

- **1.** 111.56.45.239
- **2.** 129.11.10.238
- **3.** 129.11.11.239
- **4.** 111.56.11.239

> [!TIP]
> **Correct answer: 3. 129.11.11.239**

## Solution

Convert each 8-bit octet independently. 10000001₂=128+1=129; 00001011₂=8+2+1=11; the third octet is also 11; and 11101111₂=128+64+32+8+4+2+1=239. Thus the address is 129.11.11.239, option 3.

## Key Points

- IPv4 dotted-decimal conversion is four separate unsigned binary-to-decimal conversions, each in 0–255.

## Why the other options are incorrect

The other choices misconvert at least one octet or mix bits across octet boundaries. Dotted-decimal always preserves the four groups of eight bits.
