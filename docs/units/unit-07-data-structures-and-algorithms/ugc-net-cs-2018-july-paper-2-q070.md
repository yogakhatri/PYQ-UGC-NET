# Question 70

*UGC NET CS · 2018 July Paper 2 · Hashing · Closed Hashing and Table Construction*

Consider a hash table of size seven indexed from zero, with hash function h(x)=(7x+3) mod 4. Starting from an empty table, what are its contents after inserting 1, 3, 8, 10 using closed hashing? Here `__` denotes an empty slot.

- **1.** 3, 10, 1, 8, __ , __ , __
- **2.** 1, 3, 8, 10, __ , __ , __
- **3.** 1, __ , 3, __ , 8, __ , 10
- **4.** 3, 10, __ , __ , 8, __ , __

> [!TIP]
> **Correct answer: 1. 3, 10, 1, 8, __ , __ , __**

## Solution

Evaluate h(x)=(7x+3) mod 4 for each key. h(1)=10 mod 4=2, h(3)=24 mod 4=0, h(8)=59 mod 4=3, and h(10)=73 mod 4=1. These positions are all distinct, so no probing is needed. Slots 0 through 6 contain `[3, 10, 1, 8, __, __, __]`, which is option 1.

## Key Points

- Compute the printed hash value for every key first; use the closed-hashing probe rule only when a collision actually occurs.

## Why the other options are incorrect

Option 2 preserves insertion order instead of placing keys at hash indices. Option 3 spaces the keys as though using a different modulus. Option 4 omits keys. Although the table has seven slots, the printed hash function explicitly uses mod 4.
