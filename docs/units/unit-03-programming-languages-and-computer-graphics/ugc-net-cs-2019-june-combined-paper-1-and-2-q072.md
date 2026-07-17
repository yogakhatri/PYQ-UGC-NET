# Question 72

*UGC NET CS · 2019 June Paper 1 And 2 · Programming in C · Structures, unions and pointer arithmetic*

On a 32-bit x86 machine, define S as a struct containing union U {unsigned char a; unsigned short b;} followed by unsigned char c; S occupies 32 bits. Let S B[10], S *p=&B[4], S *q=&B[5], and assign p->U.b=0x1234. If M=q-p and N=((int)&(p->c))-((int)p), what is (M,N)?

- **1.** (1,1)
- **2.** (3,2)
- **3.** (1,2)
- **4.** (4,4)

> [!TIP]
> **Correct answer: 3. (1,2)**

## Solution

The union occupies two bytes because its largest member is unsigned short. Member c follows it at byte offset 2. The question states that S occupies 32 bits, or four bytes, after alignment. Pointer subtraction counts array elements rather than bytes, so q-p=1. The byte address of p->c is two bytes beyond p, so N=2. Therefore (M,N)=(1,2).

## Key Points

- Pointer subtraction returns an element count; a member-address difference returns its byte offset within the structure.

## Why the other options are incorrect

- **Option 1:** incorrectly places c at byte offset 1 and ignores the two-byte union.
- **Option 2:** pointer subtraction is 1, not the byte-size difference 3.
- **Option 4:** uses the structure size for both values instead of member offset and element distance.
