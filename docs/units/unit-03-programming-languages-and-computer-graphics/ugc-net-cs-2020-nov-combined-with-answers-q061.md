# Question 61

*UGC NET CS · 2020 Nov With Answers · C Programming · Structure Alignment and Padding*

A machine uses 1-byte char, 2-byte short, 4-byte int, and 8-byte double. Every primitive must begin at an address divisible by its size; fields cannot be reordered and padding is inserted. How much space does `struct { short s; char c; short t; char d; double r; int i; } A[10];` consume?

- **1.** 150 bytes
- **2.** 320 bytes
- **3.** 240 bytes
- **4.** 200 bytes

> [!TIP]
> **Correct answer: 3. 240 bytes**

## Solution

Lay out one structure by offsets. short s occupies 0–1; char c uses 2; one padding byte moves short t to 4–5; char d uses 6. Seven must be padded so double r begins at offset 8 and occupies 8–15. int i occupies 16–19. Because each array element must preserve 8-byte alignment for its double, the structure receives four tail-padding bytes and has size 24. Ten elements consume 10×24=240 bytes, option 3.

## Key Points

- Align each field, then round total struct size up to the largest member alignment so every array element is valid.

## Why the other options are incorrect

Two hundred ignores tail/internal padding; 150 is merely the unpadded field-size total times ten. Three hundred twenty overpads each structure to 32 bytes even though the next multiple of the maximum 8-byte alignment after offset 20 is 24.
