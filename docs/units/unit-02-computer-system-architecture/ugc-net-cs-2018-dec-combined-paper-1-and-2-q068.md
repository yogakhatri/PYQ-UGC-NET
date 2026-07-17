# Question 68

*UGC NET CS · 2018 Dec Paper 1 And 2 · Memory Hierarchy · Disk Geometry and Sector Addressing*

Consider a disk pack with 32 surfaces, 64 tracks per surface and 512 sectors per track. Each sector stores 256 bytes serially. How many bits are required to specify a particular sector? (The source prints ‘512 sectors per pack’; the answer choices use the standard sectors-per-track interpretation.)

- **1.** 18
- **2.** 19
- **3.** 20
- **4.** 22

> [!TIP]
> **Correct answer: 3. 20**

## Solution

Under the disk-geometry interpretation required by the options, a sector address must choose one of 32 surfaces, one of 64 tracks on that surface, and one of 512 sectors on that track. These require log₂32=5, log₂64=6, and log₂512=9 bits. Total address bits=5+6+9=20, so option 3 is correct. The 256-byte sector capacity affects a byte-within-sector address, not the bits needed merely to identify the sector.

## Key Points

- For independent power-of-two address fields, add their logarithms: log₂(S·T·R)=log₂S+log₂T+log₂R.

## Why the other options are incorrect

The other totals omit or miscount one geometry field. The source literally says ‘512 sectors per pack,’ but that would make the surface and track counts irrelevant and yield 9 bits, which is not offered; the intended standard wording is sectors per track.
