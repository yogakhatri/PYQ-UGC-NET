# Question 10

*UGC NET CS · 2013 June Paper 3 · Storage Management · RAID 0-3 Organization*

Match the RAID levels: a. RAID 0; b. RAID 1; c. RAID 2; d. RAID 3. i. Bit-interleaved parity; ii. Nonredundant striping; iii. Mirrored disks; iv. Error-correcting codes.

- **A.** iv i ii iii
- **B.** iii iv i ii
- **C.** iii i iv ii
- **D.** iii ii iv i

> [!TIP]
> **Correct answer: No listed option is correct. The standard mapping is RAID 0→ii, RAID 1→iii, RAID 2→iv, RAID 3→i.**

## Solution

RAID 0 stripes data without redundancy, so a→ii. RAID 1 mirrors complete data copies, so b→iii. RAID 2 uses bit-level striping with Hamming-style error-correcting codes, so c→iv. RAID 3 uses bit/byte-interleaved data with a dedicated parity disk, matching bit-interleaved parity, so d→i. The required sequence ii, iii, iv, i does not appear among A-D.

## Key Points

- RAID mnemonic: 0=stripe, 1=mirror, 2=ECC, 3=dedicated interleaved parity.

## Why the other options are incorrect

A incorrectly assigns error-correcting codes to RAID 0. B, C and D all call RAID 0 mirrored disks, which is RAID 1. Although D correctly maps RAID 2 and RAID 3, it swaps the first two levels.
