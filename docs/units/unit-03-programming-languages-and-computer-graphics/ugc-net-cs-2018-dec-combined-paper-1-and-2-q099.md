# Question 99

*UGC NET CS · 2018 Dec Paper 1 And 2 · Java Programming · Bitwise Operations and Bit Reversal*

What does the following Java function perform? Assume an int occupies four bytes. public static int f(int a) { int b = 0; for (int i = 0; i < 32; i++) { b = b << 1; b = b | (a & 1); a = a >>> 1; } return b; }

- **1.** Returns the int that has the binary representation of integer a.
- **2.** Return the int that has the reversed binary representation of integer a.
- **3.** Return the int that represents the number of 1's in the binary representation of integer a.
- **4.** Return the int that represents the number of 0s in the binary representation of integer a.

> [!TIP]
> **Correct answer: 2. Return the int that has the reversed binary representation of integer a.**

## Solution

Each iteration performs three steps: shift b left to make room for one bit, copy the current least-significant bit of a into that new position with b|(a&1), and logically shift a right so its next bit becomes the least-significant bit. Thus the original bits are read from right to left but appended to b from left to right. Repeating this exactly 32 times processes every bit of the four-byte int, so b is the 32-bit reversal of a. Therefore option 2 is correct.

## Key Points

- The standard bit-reversal pattern is: extract the source LSB, append it to the destination, then unsigned-shift the source.

## Why the other options are incorrect

Option 1 would require preserving the original bit positions, but the algorithm deliberately consumes the least-significant bit first. Options 3 and 4 would need a counter incremented according to bit value; this code instead builds a full 32-bit pattern by shifting b on every iteration.
