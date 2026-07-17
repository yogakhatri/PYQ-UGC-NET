# Question 10

*UGC NET CS · 2017 Jan Paper 2 · Data Representation · Octal-to-Hexadecimal Conversion*

The hexadecimal equivalent of the octal number 2357 is :

- **1.** 2EE
- **2.** 2FF
- **3.** 4EF
- **4.** 4FE

> [!TIP]
> **Correct answer: 3. 4EF**

## Solution

Convert through binary because each octal digit represents three bits: 2→010, 3→011, 5→101, 7→111. Thus (2357)₈=(010011101111)₂. Regroup into four-bit hexadecimal nibbles: 0100 1110 1111, which map to 4, E, F. Hence the hexadecimal number is 4EF, option 3.

## Key Points

- Octal↔binary uses 3-bit groups; hexadecimal↔binary uses 4-bit groups.

## Why the other options are incorrect

2EE, 2FF, and 4FE result from incorrect bit grouping or digit conversion. The grouping must preserve the original bit order and proceed in groups of four from the radix point.
