# Question 4

*UGC NET CS · 2015 June Paper 3 · Data Representation · Octal-to-Hexadecimal Conversion*

The equivalent hexadecimal notation for octal number 2550276 is :

- **1.** FADED
- **2.** AEOBE
- **3.** ADOBE
- **4.** ACABE

> [!TIP]
> **Correct answer: 3. ADOBE**

## Solution

Convert through binary because each octal digit represents three bits: `2550276₈ = 010 101 101 000 010 111 110₂`. Pad on the left and regroup in fours: `0000 1010 1101 0000 1011 1110₂ = 0 A D 0 B E₁₆`. Dropping the leading zero gives `AD0BE`, printed in option 3 as the word-like `ADOBE` with the letter O standing where the hexadecimal digit 0 belongs.

## Key Points

- Octal → 3-bit groups → regroup into 4-bit groups → hexadecimal; the exact result is AD0BE.

## Why the other options are incorrect

The other strings do not result from preserving the binary bit pattern while regrouping from three-bit octal digits to four-bit hexadecimal digits. Hexadecimal has no digit `O`, so the mathematically correct notation is `AD0BE`.
