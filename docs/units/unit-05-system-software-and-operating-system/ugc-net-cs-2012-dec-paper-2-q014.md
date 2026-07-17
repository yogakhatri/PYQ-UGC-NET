# Question 14

*UGC NET CS · 2012 Dec Paper 2 · Memory Management · First-Fit Allocation*

Given memory partitions of 100 K, 500 K, 200 K, 300 K and 600 K (in order), and processes of 212 K, 417 K, 112 K and 426 K (in order), using first fit, in which original partition would the 426 K process be placed?

- **A.** 500 K
- **B.** 200 K
- **C.** 300 K
- **D.** 600 K

> [!TIP]
> **Correct answer: The 426 K process cannot be allocated; none of the listed partitions is correct**

## Solution

Apply first fit from the beginning for every process. The 212 K process goes into the 500 K hole, leaving 288 K. The 417 K process goes into the 600 K hole, leaving 183 K. The 112 K process then goes into the first sufficient remaining hole, the 288 K remainder, leaving 176 K. The free holes are now 100 K, 176 K, 200 K, 300 K and 183 K. None is large enough for 426 K, so that process must wait or allocation fails.

## Key Points

- First fit rescans holes in address order for each process and splits the selected hole.
- Track the remainder after every allocation; total free memory is irrelevant when no single hole is large enough.

## Why the other options are incorrect

The original 500 K and 600 K holes have already been used and their remainders are too small. The 200 K and 300 K holes were never large enough. Thus A-D are all false. This printed multiple-choice item is defective unless some unstated deallocation or different allocation rule is assumed.
