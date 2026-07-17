# Question 26

*UGC NET CS · 2012 Dec Paper 2 · Data Structures · Hashing with Linear Probing*

A hash function f(key)=key mod 13 with linear probing is used to insert 55, 58, 68, 91, 27, and 145. What will be the location of 79?

- **1.** 1
- **2.** 2
- **3.** 3
- **4.** 4

> [!TIP]
> **Correct answer: Location 5; none of the listed options is correct**

## Solution

With table locations 0 through 12, insert in order using linear probing: 55 hashes to 3; 58 to 6; 68 hashes to occupied 3 and goes to 4; 91 goes to 0; 27 goes to 1; and 145 goes to 2. Now 79 mod 13=1. Locations 1, 2, 3 and 4 are occupied, so probing stops at the first free location, 5.

## Key Points

- Linear probing checks h(k), h(k)+1, h(k)+2, ...
- modulo the table size until the first empty slot.
- Never stop at an occupied option just because it is the original hash value.

## Why the other options are incorrect

Options 1 through 4 are exactly the occupied probe sequence, not the first available location. Starting table numbering at 1 instead of 0 does not repair the item: the same consecutive collision chain still leads to location 5. The printed option set is therefore defective.
