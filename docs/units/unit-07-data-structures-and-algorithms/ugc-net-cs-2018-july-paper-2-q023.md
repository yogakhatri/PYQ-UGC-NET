# Question 23

*UGC NET CS · 2018 July Paper 2 · Data Structures · Hashing with Linear Probing*

Using h(key)=key mod 7 with linear probing, insert 44,45,79,55,91,18,63 into a table indexed 0 through 6. Where is key 18 stored?

- **1.** 3
- **2.** 4
- **3.** 5
- **4.** 6

> [!TIP]
> **Correct answer: 3. 5**

## Solution

Insert in order. 44 hashes to 2; 45 to 3. 79 also hashes to 2, so probing places it at 4. 55 hashes to 6, and 91 to 0. Key 18 hashes to 4, but slot 4 holds 79, so linear probing advances to empty slot 5. Therefore key 18 is stored at location 5, option 3.

## Key Points

- Linear probing checks h(k), h(k)+1, h(k)+2,… modulo the table size until it finds the first empty slot.

## Why the other options are incorrect

Locations 3 and 4 are already occupied when 18 arrives, and the first free slot is 5, so probing never reaches 6. The later insertion of 63 cannot change 18's established location.
