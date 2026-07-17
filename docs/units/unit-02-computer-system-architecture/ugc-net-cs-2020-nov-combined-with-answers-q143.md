# Question 143

*UGC NET CS · 2020 Nov With Answers · Memory Hierarchy · Disk Cylinders and Block Size*

Statement I: The disk has 2,000 cylinders. Statement II: 51,200 bytes is not a valid block size for the disk. Choose the correct evaluation.

- **1.** Both statements are true
- **2.** Both statements are false
- **3.** Statement I is true but Statement II is false
- **4.** Statement I is false but Statement II is true

> [!TIP]
> **Correct answer: 3. Statement I is true but Statement II is false**

## Solution

A cylinder consists of all equal-radius tracks across the recording surfaces. Since each surface has 2,000 tracks, the disk has 2,000 cylinders; Statement I is true. In the logical-block model used by this exercise, a valid block size must be a whole multiple of the 512-byte sector size. Because 51,200=100×512, it is a valid block size even though it spans more than one 50-sector track. Statement II is therefore false, so option 3 is correct.

## Key Points

- Cylinder count equals tracks per surface; a logical block must contain an integral number of sectors and may span tracks in this model.

## Why the other options are incorrect

Options 2 and 4 incorrectly deny the cylinder count. Options 1 and 4 impose a one-track maximum that the source exercise does not impose on a logical block. Do not confuse a sector-alignment requirement with a track-boundary restriction.

## References

- [Database Management Systems exercise solutions — disk geometry and valid block sizes](https://www.cs.princeton.edu/courses/archive/spr2000/cs425/soln_from_text_midterm.pdf)
