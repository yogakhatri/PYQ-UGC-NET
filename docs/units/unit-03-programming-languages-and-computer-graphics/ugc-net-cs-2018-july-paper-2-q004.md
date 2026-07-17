# Question 4

*UGC NET CS · 2018 July Paper 2 · Programming in C · Union Storage and Little-Endian Byte Order*

What is the output of the following ‘C’ program ? (Assuming little - endian representation of multi-byte data in which Least Significant Byte (LSB) is stored at the lowest memory address.) #include <stdio.h> #include <stdlib.h> /* Assume short int occupies two bytes of storage */ int main ( ) { union saving { short int one; char two[2]; }; union saving m; m.two [0] = 5; m.two [1] = 2; printf(’’%d, %d, %d\n”, m.two [0], m.two [1], m.one); }/* end of main */

- **1.** 5, 2, 1282
- **2.** 5, 2, 52
- **3.** 5, 2, 25
- **4.** 5, 2, 517

> [!TIP]
> **Correct answer: 4. 5, 2, 517**

## Solution

Both union members share the same storage. On a little-endian machine, `two[0]` occupies the least-significant byte of the 16-bit `short` and receives 5=05h; `two[1]` is the most-significant byte and receives 2=02h. Reading the two bytes as `one` therefore gives 0205h=2×256+5=517. The output is `5, 2, 517`, option 4.

## Key Points

- Little-endian multi-byte value = low-address byte + 256×next byte; here 5+256×2=517.

## Why the other options are incorrect

1282 reverses the byte significance: 0502h=1282. The values 52 and 25 concatenate decimal digits instead of interpreting two base-256 bytes. The question explicitly supplies size and endianness assumptions needed for this representation-dependent example.
