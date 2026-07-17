# Question 120

*UGC NET CS · 2023 Mar 15 Shift 1 Dec 2022 Session · Memory Management · Enhanced second-chance page replacement*

Match List I with List II List I List Il A. (reference bit =0, modify bit =0) I. Must write out before replacement B. (reference bit =0, modify bit = 1) II. Probably will be used again soon and need to write out C. (reference bit =1, modify bit =0) III. Best page to replace D. (reference bit=1, modify bit = 1) IV. Probably will be used again soon Choose the correct answer from the options given below:

- **1.** A-I, B-I, C-II, D-IV
- **2.** A-ll, B-I, C-IV, D-III
- **3.** А-III, B-I, C-II, D-IV
- **4.** A-III, B-I, C-IV, D-II

> [!TIP]
> **Correct answer: 4. A-III, B-I, C-IV, D-II**

## Solution

In enhanced clock replacement, (0,0) is best (A–III); (0,1) is unused but dirty and must be written (B–I); (1,0) is likely reused soon but clean (C–IV); (1,1) is likely reused and also dirty (D–II).

## Key Points

- Prefer unreferenced clean pages; dirty pages incur write-back.

## Why the other options are incorrect

Other options confuse reference and modify-bit meanings.
